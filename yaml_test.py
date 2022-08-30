data = """

- title: "John Doe"
  views: 33
  published: 1234
- title: "another video"
  views: 20
  published: 1224
"""

import yaml

my_data = yaml.load(data, Loader=yaml.FullLoader)
print(my_data)

yml_data = open("youtube.yaml", "r").read()
print(yml_data)
validate = yaml.load(yml_data, Loader=yaml.SafeLoader)
print(validate)
rerender = yaml.dump(validate, default_flow_style=False)
print(rerender)