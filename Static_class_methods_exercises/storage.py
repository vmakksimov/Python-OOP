from Static_and_Class_methods.Static_class_methods_exercises.category import Category
from Static_and_Class_methods.Static_class_methods_exercises.document import Document
from Static_and_Class_methods.Static_class_methods_exercises.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []


    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)
            return

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)
            return

    def add_document(self, document:Document):
        if document not in self.documents:
            self.documents.append(document)
            return

    def edit_category(self, category_id, new_name):

        for category in self.categories:
            category.id = category_id
            category.name = new_name
            return


    def edit_topic(self, topic_id, new_topic, new_storage_folder):

        for topic in self.topics:
            topic.id = topic_id
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder
            return

    def edit_document(self, document_id, new_file_name):

        for document in self.documents:
            document.id = document_id
            document.file_name = new_file_name
            return


    def delete_category(self, category_id):
        for el in self.categories:
            if el.id == category_id:

                self.categories.remove(el)
                return

    def delete_topic(self, topic_id):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)
                return

    def delete_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)
                return


    def get_document(self, document_id):

        for document in self.documents:
            if document.id == document_id:
                return document.__repr__()



    def __repr__(self):
        result = ''

        for document in self.documents:
            result += document.__repr__()
            result += '\n'

        return result


