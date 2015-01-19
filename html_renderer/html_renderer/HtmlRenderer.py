__author__ = 'reinschs@fh-brandenburg.de | patrick.walther.1989@gmx.de | mommert@fh-brandenburg.de'

import shutil
import os.path


class HtmlRenderer:

    steps = []
    tab_navigation = basestring
    tab_content = basestring
    copy_path = basestring
    title = 'Das ist der Titel.'
    text = 'Das ist der Text.'

    def __init__(self):
        # sets default path for the rendered html
        self.set_copy_path(os.path.dirname(__file__) + '\\..\\rendered_html')
        print('init html renderer')

    # add a step with the image path, title and text
    def add_step(self, image_path, title, text):
        entry = {'image_path': image_path, 'title': title, 'text': text}
        self.steps.append(entry)

    def set_copy_path(self, new_path):
        self.copy_path = new_path

    # changes the path where rendered html will be created
    def get_copy_path(self):
        return self.copy_path

    def copy_needed_files(self):
        os.path.dirname(__file__)
        shutil.copytree(os.path.dirname(__file__) + '\\needed_data', self.get_copy_path())

    def get_index_html_path(self):
        return self.get_copy_path() + '\\index.html'

    def set_title(self, new_title):
        self.title = new_title

    def get_title(self):
        return self.title

    def set_text(self, new_text):
        self.title = new_text

    def get_text(self):
        return self.text

    def truncate_file(self, file):
        file.seek(0)
        file.truncate()

    def fill_tab_navigation(self):
        tab_navigation = ''
        count = 1
        for step in self.steps:
            if count == 1:
                tab_navigation += '<li class="active"><a href="#step' \
                                  + str(count) \
                                  + '" data-toggle="tab">Schritt ' \
                                  + str(count) \
                                  + '</a></li>'
            else:
                tab_navigation += '<li><a href="#step' \
                                  + str(count) \
                                  + '" data-toggle="tab">Schritt ' \
                                  + str(count) \
                                  + '</a></li>'
            count += 1

        self.tab_navigation = '<ul class="nav nav-tabs">' + tab_navigation + '</ul>'

    def get_image(self, image_path, count):
        os.rename(image_path, self.get_copy_path() + '\\data\\img\\step' + str(count) + '.jpg')

    def fill_tab_content(self):
        tab_content = ''
        count = 1
        for step in self.steps:
            self.get_image(step['image_path'], count)
            if count == 1:
                tab_content += '<div class="tab-pane active" id="step' \
                               + str(count) \
                               + '">' \
                               + '<img src="data\\img\\step' \
                               + str(count) \
                               + '.jpg">' \
                               + '<h3>' \
                               + step['title'] \
                               + '</h3>' \
                               + '<p>' \
                               + step['text'] \
                               + '</p></div>'
            else:
                tab_content += '<div class="tab-pane" id="step' \
                               + str(count) \
                               + '">'\
                               + '<img src="data\\img\\step' \
                               + str(count) \
                               + '.jpg">' \
                               + '<h3>' \
                               + step['title'] \
                               + '</h3>' \
                               + '<p>' \
                               + step['text'] \
                               + '</p></div>'
            count += 1

        self.tab_content = '<div class="tab-content">' + tab_content + '</div>'

    def fill_tabs(self):
        self.fill_tab_content()
        self.fill_tab_navigation()

    def get_tab_navigation(self):
        return self.tab_navigation

    def get_tab_content(self):
        return self.tab_content

    def replace_data(self, data):
        data = data.replace('{default_title}', self.get_title())
        data = data.replace('{default_text}', self.get_text())
        data = data.replace('{tab_navigation}', self.get_tab_navigation())
        data = data.replace('{tab_content}', self.get_tab_content())
        return data

    def render_html(self):
        # removes already existing rendered html
        if os.path.isdir(self.get_copy_path()):
            shutil.rmtree(self.get_copy_path())
        self.copy_needed_files()
        self.fill_tabs()
        index_html_path = self.get_index_html_path()
        with open(index_html_path, "r+") as myfile:
            data = myfile.read().replace('\n', '')
            print(index_html_path)
            data = self.replace_data(data)

            self.truncate_file(myfile)

            myfile.write(data)
            print(data)
