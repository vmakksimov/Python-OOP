from Static_and_Class_methods.Static_class_methods_exercises.customer1 import Customer
from Static_and_Class_methods.Static_class_methods_exercises.equipment import Equipment
from Static_and_Class_methods.Static_class_methods_exercises.exercise_plan import ExercisePlan
from Static_and_Class_methods.Static_class_methods_exercises.subscription import Subscription
from Static_and_Class_methods.Static_class_methods_exercises.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []


    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
            return

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            return

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            return

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
            return

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            return

    def __get_obj_by_id(self, objects, objects_id):
        for obj in objects:
            if obj.id == objects_id:
                return obj

    def subscription_info(self, subscription_id: int):
        result = ''
        subscription = self.__get_obj_by_id(self.subscriptions, subscription_id)
        customer = self.__get_obj_by_id(self.customers, subscription.customer_id)
        trainer = self.__get_obj_by_id(self.trainers, subscription.trainer_id)
        plan = self.__get_obj_by_id(self.plans, subscription.exercise_id)
        equipment = self.__get_obj_by_id(self.equipment, plan.equipment_id)

        result += str(subscription) + '\n'
        result += str(customer) + '\n'
        result += str(trainer) + '\n'

        result += str(equipment) + '\n'
        result += str(plan) + '\n'



        return result





