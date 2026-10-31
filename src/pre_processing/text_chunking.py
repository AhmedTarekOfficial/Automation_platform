from langchain_text_splitters import RecursiveCharacterTextSplitter


def splitting_content(content : str) -> str : 

        content_after_split = RecursiveCharacterTextSplitter(
            chunk_size = 100 , 
            chunk_overlap = 50 
                
        )
        return content_after_split.split_text(content)

text = """Technology has become one of the most important parts of modern life, influencing the way people communicate, learn, work, and solve problems every day.
Over the past few decades, technological developments have transformed societies and created opportunities that previous generations could hardly imagine.
Today, people can access enormous amounts of information through the internet, communicate with individuals across the world within seconds, and complete complicated tasks using computers and smartphones.
These developments have made life more convenient, but they have also introduced new challenges that require people to develop different skills and adapt to constant changes.
One of the most significant technologies shaping the future is artificial intelligence, which allows computer systems to perform tasks that traditionally required human intelligence, such as recognizing patterns, understanding language, making predictions, and supporting decision making.
Artificial intelligence is already being used in healthcare, education, transportation, agriculture, manufacturing, and many other industries.
For example, healthcare professionals can use intelligent systems to analyze medical images and identify possible signs of disease, while teachers can use educational platforms to provide personalized learning experiences for students with different abilities and interests.
Similarly, businesses can analyze customer behavior, improve their services, and make better decisions through data analysis and machine learning.
However, the increasing use of technology does not mean that human abilities are becoming less important.
In fact, creativity, critical thinking, communication, teamwork, and problem solving are becoming even more valuable because technology works best when people understand how to use it responsibly and effectively.
A person who wants to succeed in the modern world must therefore develop both technical knowledge and essential personal skills.
Learning should not be viewed as an activity that ends after graduation, because new technologies, scientific discoveries, and professional requirements continue to appear throughout life.
Continuous learning allows individuals to remain competitive, discover new interests, and improve their understanding of the world.
Fortunately, the internet has made education more accessible than ever before.
Students can watch educational videos, attend online courses, read digital books, participate in international communities, and practice their skills through practical projects without needing to travel to another country.
Nevertheless, having access to information is not the same as understanding it.
Real learning requires patience, practice, discipline, curiosity, and the willingness to make mistakes.
Many beginners become frustrated when they encounter difficult concepts, especially in subjects such as mathematics, programming, engineering, or artificial intelligence.
They sometimes believe that successful people understand everything immediately, but this assumption is incorrect.
Most experts have spent years studying fundamental concepts, solving problems, making errors, and gradually improving their abilities through consistent effort.
For instance, someone learning programming may initially struggle to understand variables, loops, functions, and data structures, but regular practice eventually makes these concepts more familiar.
After developing a strong foundation, that person can begin building applications, analyzing datasets, developing intelligent systems, and contributing to real projects.
The same principle applies to learning foreign languages, studying mathematics, developing communication skills, and pursuing almost any meaningful goal.
Progress usually happens through small improvements repeated over a long period rather than through sudden moments of extraordinary achievement.
Another important aspect of personal development is learning how to manage time effectively.
Modern life contains countless distractions, including social media, entertainment platforms, notifications, and unnecessary activities that can consume valuable hours without producing meaningful results.
Although relaxation and entertainment have their place, individuals need to establish clear priorities and allocate sufficient time to education, professional responsibilities, physical health, and relationships.
Creating a realistic daily schedule can help people maintain balance and reduce unnecessary stress.
It is also useful to divide large goals into smaller tasks because completing manageable steps provides motivation and makes challenging projects feel less overwhelming.
For example, a student who wants to become an artificial intelligence engineer should not attempt to master every technology simultaneously.
Instead, the student can begin with programming fundamentals, strengthen mathematical knowledge, study statistics and probability, understand machine learning algorithms, and gradually explore advanced topics such as deep learning, natural language processing, computer vision, and intelligent agents.
Building practical projects throughout this journey is particularly important because projects connect theoretical knowledge with real problems and encourage independent thinking.
Collaboration also plays an essential role in professional development.
When people work together, they exchange perspectives, share responsibilities, identify mistakes, and often discover solutions that would be difficult to develop individually.
Effective teamwork requires respect, honesty, clear communication, and the ability to accept constructive criticism.
These qualities help create productive environments where everyone can contribute according to their strengths while continuing to improve weaker areas.
At the same time, technological progress raises serious ethical questions about privacy, fairness, employment, misinformation, and the responsible use of powerful systems.
Developers and organizations must consider the possible consequences of their decisions rather than focusing exclusively on performance, efficiency, or financial benefits.
Responsible innovation should aim to improve human well being, protect individual rights, and make opportunities available to people from different backgrounds.
Ultimately, the future will not belong simply to those who possess the most advanced tools, but to those who combine knowledge with wisdom, technical competence with ethical responsibility, and ambition with consistent effort.
Every individual has the opportunity to learn something valuable, contribute to society, and create meaningful improvements in their own life.
Success does not require perfection, unlimited resources, or immediate mastery of difficult subjects.
It requires a clear direction, the courage to begin, and the determination to continue learning even when progress seems slow.
By developing useful skills, maintaining curiosity, supporting others, and approaching challenges with patience and confidence, people can prepare themselves for an increasingly complex world and turn technological changes into opportunities for lasting personal and professional growth."""


print(splitting_content(text))

