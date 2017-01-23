import requests
import json

first_name = "Rikesh"
last_name = "Thapa"
email = "rthapa@u.rochester.edu"
phone = "718-473-5360"
cover_letter = """I am a developer with a strong understanding of web technologies.
                I have been designing, implementing, evaluating, and managing projects
                for over 8 years, and particularly enjoy challenging projects with fasted paced, agile
                development timelines. I have broad range of experiences in many web technologies and stacks
                and am a fast eager learner, always interested in finding the best solution-- not just the easiest one.
                I care not only about quality of work for in terms of the user but also in terms of the
                other developers who will also be working on my code. I prode myself in writing clean,
                readable, maintainable and reusable code."""
URL = ["https://www.linkedin.com/in/rikeshthapa"]
headers = {'Content-Type': 'application/json'}

payload = {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone,
           'cover_letter': cover_letter, 'urls': URL}

r = requests.post('https://app.close.io/hackwithus/', headers = headers, data=json.dumps(payload))
print(r.text)
