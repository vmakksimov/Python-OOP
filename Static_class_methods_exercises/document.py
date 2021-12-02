from Static_and_Class_methods.Static_class_methods_exercises.category import Category
from Static_and_Class_methods.Static_class_methods_exercises.topic import Topic


class Document:
    def __init__(self, id, category_id, topic_id, file_name):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []


    @classmethod
    def from_instances(cls, id:int, category: Category, topic: Topic, file_name:str):
        return cls(id, category.id, topic.id, file_name)


    def add_tag(self, tag_content):
        if tag_content not in self.tags:
            self.tags.append(tag_content)
            return

    def remove_tag(self, tag_content):
        for tag in self.tags:
            if tag == tag_content:
                self.tags.remove(tag)
                return

    def edit(self, file_name):
        self.file_name = file_name
        return

    def __repr__(self):
        return f'Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {", ".join([el for el in self.tags])}'