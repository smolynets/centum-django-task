# from django.db.models.signals import pre_save
# from django.core.exceptions import ValidationError
# from django.dispatch import receiver

# from quiz.models import Questionare, Question, Answer

# @receiver(pre_save, sender=Questionare)
# def check_minimum_questions(sender, instance, **kwargs):
#     if instance.pk is not None and instance.questions.count() < 5:
#         raise ValidationError("Each Questionare must have at least 5 questions.")


# def validate_answers(sender, instance, **kwargs):
#     if instance.answers.count() != 4:
#         raise ValidationError("Кожне запитання повинно мати рівно 4 варіанти відповідей.")
#     if instance.answers.filter(is_correct=True).count() != 1:
#         raise ValidationError("Має бути рівно одна правильна відповідь на запитання.")


# def validate_answer(sender, instance, **kwargs):
#     if instance.is_correct:
#         raise ValidationError("Кожне запитbjhbjhbjнти відповідей.")


# pre_save.connect(check_minimum_questions, sender=Questionare)
# pre_save.connect(validate_answers, sender=Question)
# pre_save.connect(validate_answer, sender=Answer)
