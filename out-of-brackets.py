import sublime, sublime_plugin

class OutOfBracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# remove current line if its empty
		# dont remove it if next line contains code other than brackets
		# (i.e. this line is delimiter between code blocks)
		for sel in self.view.sel():
			if sel.empty():
				pos = sel.b
				line = self.view.substr(self.view.line(pos))
				line = line.replace(' ', '').replace('\t', '')
				if len(line) <= 0:
					next_line_pos = self.view.line(pos).b + 1
					next_line = self.view.substr(self.view.line(next_line_pos))
					next_line = next_line.replace(' ', '').replace('\t', '')
					if len(next_line) <= 0 or next_line[0] == "}":
						self.view.erase(edit, self.view.line(pos))
						self.view.run_command("left_delete")

		# move out of brackets
		for sel in self.view.sel():
			if sel.empty():
				self.view.run_command("move_to", {
					"to": "brackets"
				})
				self.view.run_command("move_to", {
					#"extend": false, 
					"to": "eol"
				})

		# insert ; when required
		for sel in self.view.sel():
			if sel.empty():
				pos = sel.b

				prev_char = self.view.substr(pos - 1)

				if prev_char != ";" and prev_char != "}":
					self.view.insert(edit, pos, ";\n")
				else:
					self.view.insert(edit, pos, "\n")

				self.view.run_command("reindent")

		# remove next line if empty
		for sel in self.view.sel():
			if sel.empty():
				pos = sel.b
				line = self.view.line(pos)
				next_line_pos = line.b + 1
				next_line = self.view.substr(self.view.line(next_line_pos))
				next_line = next_line.replace(' ', '').replace('\t', '')
				if len(next_line) <= 0:
					self.view.erase(edit, self.view.full_line(next_line_pos))
