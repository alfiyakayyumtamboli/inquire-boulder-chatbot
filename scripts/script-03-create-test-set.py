#!/usr/bin/env python3
# Create datafram for testing model accuracy.

import pandas as pd

test = pd.DataFrame([
                        ['I live on the corner of Bear Mountain Drive and Scrub Oak Circle, and would like the City enforce the speed limit on Bear Mountain Drive. Despite a limit of 25 mph, I routinely observe vehicles traveling well above that speed in both directions (especially in the mornings and early evening). There are a ton of kids in this neighborhood, as well as a blind curve in the road between several crosswalks. It baffles me to see so much enforcement on Lehigh (with the regular presence of a photo van) and only the very occasional patrol car on Bear Mountain Drive. It would be great if the photo van or other officers could regularly make an appearance on Bear Mountain.',
                        'Speeding on Residential Streets'],
                        ['Can you please mow the grass in the park. It is becoming difficult to find the dog poop and dog owners are just leaving it in the grass.',
                        'Park Maintenance Issues'],
                        ['Are there grizzlies in Boulder?',
                        'Do we have grizzly bears in Colorado?'],
                        ['Where do I report being hit by a bicycle?',
                        'Have you had a close call with a bicycle, pedestrian or motorist? For example: Were you in a crosswalk (on foot, bike, skateboard) and a car almost hit you? Were you riding your bike on the right side of the road and a car almost hit you? Did you bike through a red light and a car almost hit you? Were you walking on the sidewalk and a bike almost hit you?'],
                        ['How much time do I have to wait for my income certification for affordable housing?',
                        'How long does it take to become income-certified?'],
                        ['my water pipes froze and now they are leaking. how do i turn off the water??',
                        'How can I prevent and thaw frozen water pipes?'],
                        ["Hello, There are a group of Gambel Oak Trees with Tree ID #'s 38820-38825 that I would like to be pruned up in order to keep them away from the Rec Center wall and to keep them in good, trimmed health. I also would like Tree ID 38825 to be pruned away from the American Flag so it will not come in contact with the tree, from the nearby flag pole. Thank you very much and if you have any questions or concerns, feel free to give me a call.",
                        'Public Tree Issues'],
                        ['There are constantly dogs off leash in the children playgrounds of columbine school. Even though the playgrounds are fenced and have a sign stating dogs should not go in. You can see some dog owners do not even pick their dog shit.',
                        'Dogs on Open Space and Mountain Parks'],
                        ['I parked in the garage on 11th and Walnut on Sunday 12/23 starting at 5 PM and left at 12:35 AM that Monday 12/24. I was charged $1.25 but it should have still been free since charged parking doesnâ€™t start till 7 AM on Mondays , I park here all the time and I am confused as to why it says I owed $1.25. Is there a glitch in the system ?',
                        'Contact Parking Services'],
                        ['Where do I apply for building permits?',
                        'How do I get a building permit?'],
                        ['Do black bears ever attack people?',
                        'What are the risks to humans from bears?'],
                        ["I don't have a composting bin at my house. How do I get one?",
                        'Composting and Recycling'],
                        ['There is a dead cat on Baseline Rd. Someone needs to remove it.',
                        'Debris, Trash and Road Kill'],
                        ['Why did the tulips on Pearl St. get removed?',
                        'Why does the city dig up the tulips every year?'],
                        ['Where do I go to pay a parking ticket in person?',
                        'What do I do if I receive a parking ticket?'],
                        ['Are prairie dogs endangered?',
                        'What is the status of the black-tailed prairie dog as a species?'],
                        ['What can I do to reduce household electricity use?',
                        'How can I save energy in my home?'],
                        ['What is the cost for disposable plastic bags?',
                        'How much is the fee?'],
                        ['Is the Pearl St. pedestrian area dog-friendly?',
                        'Are dogs allowed on the mall?'],
                        ['What is the non-emergency phone number?',
                        'Emergency Alerts, Numbers and Warnings']
                    ],
                    columns=['test_question', 'match_question'])

test.to_csv('../data/test/test-questions.csv', index=False)
