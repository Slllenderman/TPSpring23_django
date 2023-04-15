from django.core.management.base import BaseCommand
from ...models import User, Profile, Tag, Question, Answer
import random
from nickname_generator import generate
from RandomWordGenerator import RandomWord

lorem_samples = [
    #lorem5
    'Lorem ipsum dolor sit amet.', 
    #lorem7
    'Lorem ipsum dolor sit amet contetur adicing.'
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

    def generate_tag(self, word_generator):
        try:
            tag = Tag()
            tag.name = word_generator.generate()
            tag.save()
            return tag
        except:
            return self.generate_tag()

    def generate_profile(self, user):
        profile = Profile()
        profile.nickname = generate()
        profile.user = user
        profile.save()
        return profile

    def generate_question(self, profile, tags):
        question = Question()
        question.author = profile
        question.title = lorem_samples[0]
        question.description = lorem_samples[random.randint(0, 1)]
        question.content = lorem_samples[random.randint(2, 6)]
        question.rating = 0
        question.save()
        tags_num = random.randint(1, 3)
        for i in range(tags_num):
            try:
                tag = random.choice(tags)
                question.tags.add(tag)
            except:
                pass
        return question

    def generate_answer(self, question, profiles):
        answer = Answer()
        try:
            answer.author = random.choice(profiles)
        except:
            answer.author = random.choice(profiles)
        answer.content = lorem_samples[random.randint(3, 6)]
        answer.question = question
        answer.rating = 0
        answer.save()
        return answer

    def generate_rating(self, profile, answers, questions):
        try:
            answer = random.choice(answers)
            question = random.choice(questions)
            answer.rating += 1
            answer.rated.add(profile.user)
            question.rating += 1
            question.rated.add(profile.user)
            answer.save()
            question.save()
        except:
            pass

    def handle(self, *args, **options):
        ratio = options['ratio']
        word_generator = RandomWord(max_word_size=15, include_digits=True, special_chars=True)
        tags = list()
        answers = list()
        profiles = list()
        questions = list()

        for i in range(ratio):
            user = self.generate_user()
            profile = self.generate_profile(user)
            profiles.append(profile)
            tags.append(self.generate_tag(word_generator))
            for i in range(10):
                question = self.generate_question(profile, tags)
                questions.append(question)
                for i in range(10):
                    answers.append(self.generate_answer(question, profiles))
                for i in range(20):
                    self.generate_rating(profile, answers, questions)

        
            
                

