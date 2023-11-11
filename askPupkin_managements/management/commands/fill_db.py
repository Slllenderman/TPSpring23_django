from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from askPupkin_models.models import User, Profile, Tag, Question, Answer, Like
import random
from nickname_generator import generate

lorem_samples = [
    #lorem5
    'Lorem ipsum dolor sit amet.', 
    #lorem7
    'Lorem ipsum dolor sit amet contetur adicing.',
    #lorem10
    'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus, distinctio.',
    #lorem15
    'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic ut, debitis fugit delectus facere quam.',
    #lorem20
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque ut quas sed suscipit temporibus incidunt quam cum voluptatibus placeat ullam.',
    #lorem30
    'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Deserunt possimus atque repellendus illum quas, dignissimos eius veniam ducimus magnam eveniet labore! Ducimus rerum vero harum tempore ipsa iste cumque eaque odio, ea provident nobis consectetur labore aperiam. Qui, minima illum!',
    #lorem50
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium vitae autem, molestiae, omnis blanditiis quia saepe inventore iste mollitia odio odit dolore ipsum illum, eius alias velit deleniti nihil nemo. Odit aliquid esse similique alias sint exercitationem perspiciatis voluptate doloribus itaque. Voluptatem quo nisi corrupti illo alias veniam inventore asperiores.',
    #lorem100
    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui, aperiam aliquam? Quaerat libero iusto necessitatibus, accusantium veritatis, unde aperiam, ducimus reiciendis tempora mollitia corporis quos? Sunt soluta quae quis alias cumque aperiam facere vel in nisi, numquam perspiciatis voluptatibus repellendus accusantium natus reiciendis iusto corrupti voluptas aliquam, laborum maxime repellat veritatis aut mollitia? Quos enim similique voluptas exercitationem id at doloribus quae nesciunt, ea sit voluptates atque iure aliquam incidunt ducimus saepe corrupti porro cumque dolorum quasi officiis. Dolorem vero blanditiis pariatur nobis quidem itaque aliquam velit rem. Sit delectus commodi odio consequuntur vitae corporis magni totam, accusantium est exercitationem.'
]

mail_samples = [
    '@mail.ru', 
    '@yandex.ru',
    '@gmail.com',
    '@bmstu.ru'
]

tag_samples = [
    'csh',
    'cpp',
    'python',
    'ruby',
    'go',
    'mysql',
    'technopark',
    'vk',
    'mail',
    'pascal'
]

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'ratio',
            nargs='?',
            type=int,
        )

    def generate_user(self):
        try:
            username = generate()
            password = generate()
            email = username + random.choice(mail_samples)
            return User.objects.create_user(username=username, password=password, email=email)
        except:
            return self.generate_user()

    def generate_profile(self, user):
        profile = Profile()
        profile.nickname = generate()
        profile.user = user
        profile.save()
        return profile

    def generate_tags(self):
        tags = list()
        for tag in tag_samples:
            new_tag = Tag()
            new_tag.name = tag
            new_tag.save()
            tags.append(new_tag)
        return tags

    def generate_question(self, profile, tags):
        question = Question()
        question.author = profile
        question.title = lorem_samples[random.randint(0, 3)]
        question.description = lorem_samples[random.randint(1, 4)]
        question.content = lorem_samples[random.randint(3, 7)]
        question.save()
        tags_num = random.randint(1, 3)
        for i in range(tags_num):
            tag = random.choice(tags)
            question.tags.add(tag)
        return question

    def generate_answer(self, question, profiles):
        answer = Answer()
        answer.author = random.choice(profiles)
        answer.content = lorem_samples[random.randint(2, 6)]
        answer.question = question
        isIncorrect = random.randint(0, 9)
        if not isIncorrect:
            answer.correctness = True
        answer.save()
        return answer

    def generate_rating(self, profile, objects):
        object = random.choice(objects)
        object_type = ContentType.objects.get_for_model(object)
        try:
            Like.objects.create(content_type=object_type, object_id=object.id, user=profile.user)
            object.rating += 1
            object.author.rating += 1
            object.save()
            object.author.save()
        except:
            pass

    def handle(self, *args, **options):
        ratio = options['ratio']
        tags = self.generate_tags()
        answers = list()
        profiles = list()
        questions = list()
        for i in range(ratio):
            user = self.generate_user()
            profile = self.generate_profile(user)
            profiles.append(profile)
            for i in range(10):
                question = self.generate_question(profile, tags)
                questions.append(question)
                for i in range(10):
                    answers.append(self.generate_answer(question, profiles))
                for i in range(10):
                    self.generate_rating(profile, answers)
                    self.generate_rating(profile, questions)

        
            
                

