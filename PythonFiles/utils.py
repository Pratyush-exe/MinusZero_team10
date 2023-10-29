import openai
import json
import os
openai.api_key="API-KEY"

def input_to_config(input_prompt):
  config=  openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content":f"""
  ## CONTEXT:
  You are given a human written input prompt in INPUT_PROMPT. Take this input and map to the json config called ASSET_CONFIG. Return the final json config as output only.

  ## INPUT_PROMPT:
  {input_prompt}

  ## ASSET_CONFIG:
  ```json """+"""{
    "weather": int // range: 0 is sunny, 1 for evening, 2 for foggy, 3 for rainy, 4 for snowy
    "density": float //range: 0-1: where 0 is least dense (minimum) and 1 is most dense(maximum),
    "animals": float //range: 0-1: where 0 is least number of animals (no animals) and 1 is many animals(a lot of animls),
    "people": float //range: where 0 is least number of people (no people) and 1 is many people(a lot of people),
    "houses": float //range: where 0 is least number of houses (no houses) and 1 is many houses(a lot of houses),
    "lanes": int //range: 1-6,
    "dead_end": int //choices 0 where there are no dead ends, or 1 with a dead end,
    "traffic_lights_status": int //choice 0 where there are no traffic lights, or 1 with a traffic light,
    "traffic_light":int //range: -1 - 1: where -1 is red, 0 is yellow and 1 is green,
    "potholes": float //range 0 - 1,
    "intersection_type":int //range 0-4: where 0 is no intersection, 1 is a right turn, 2 is a left turn, 3 is a t-shaped intersection,4 is a cross shaped or ring intersection,
    "speed_breaker":int //choices 0 or 1: where 0 is no speed breaker and 1 is that a speed breaker exists
  }
  ```
  """
  }])
  return config

def prompt_to_json(prompt):
  try:
    config=input_to_config(prompt)
    config=str(config.choices[0].message).replace('\n','')
    config=eval(config)
    config=eval(config['content'].replace("\n", ""))
    file_path = 'unity_config.json'
    with open(file_path, 'w') as json_file:
        json.dump(config, json_file, indent=4)
  except:
    print("Retrying")
    prompt_to_json(prompt)
  return config


# "weather": int // range: 0 is for rainy, 1 is for snowing, 2 is for foggy,3 is for cloudy,4 is for sunny, 5 is for evening,
