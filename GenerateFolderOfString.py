import sublime, sublime_plugin

import os, os.path

class GenerateFolderCore:
	def gen(self, path):
		settings = sublime.load_settings('GenerateFolderOfString.sublime-settings')
		if settings.get('start_level') is None:
			self.start_level = 1
		else:
			self.start_level = int(settings.get('start_level'))

		if settings.get('prefix_character') is None:
			self.prefix_character = "...."
		else:
			self.prefix_character = str(settings.get('prefix_character'))

		return '\n'.join(self.get_files(path, self.start_level))

	def get_files(self, path, level):
		all_file = []
		files = os.listdir(path)
		files.sort(key=self.file_comp)
		for file_name in files:
			all_file.append((self.prefix_character * level) + file_name)

			full_path = os.path.join(path, file_name)
			if os.path.isdir(full_path):
				all_file.extend(self.get_files(full_path, level + 1))

		return all_file

	def file_comp(self, path):
		if path.find(".") > 0:
			return 1
		else:
			return 0


class GenerateFolderOfStringCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel(
			"folder path(empty to the open folders):",
			"",
			self.on_write_path,
			None,
			None)
		pass

	def on_write_path(self, write_path):

		if len(write_path) > 0:
			if os.path.exists(write_path):
				if not os.path.isdir(write_path):
					write_path = os.path.dirname(write_path)
			else:
				sublime.error_message('folder not exist!')
				return

		if len(write_path) == 0 and len(self.window.folders()) > 0:
			write_path = self.window.folders()[0]

		if len(write_path) == 0:
			sublime.error_message('folder not exist!')
			return

		try:
			if(self.window.active_view()):
				self.window.active_view().run_command(
                    "do_generate_folder_of_string", {
                    	"write_path": write_path
                    })
		except ValueError:
			pass


class DoGenerateFolderOfStringCommand(sublime_plugin.TextCommand):
	def run(self, edit, write_path = ""):
		if len(write_path) == 0:
			if self.view.file_name() is None:
				sublime.error_message('folder not exist!')
				return
			else:
				write_path = os.path.dirname(self.view.file_name())

		self.view.insert(edit, 0, GenerateFolderCore().gen(write_path))
