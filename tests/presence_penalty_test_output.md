🧪 PRESENCE PENALTY VARIATION TESTING
Testing context diversity with different presence penalty values
Words: 4 | Configurations: 4
================================================================================

📊 CONFIGURATION: Low Presence Penalty (Baseline)
Temperature: 1.2 | Top_p: 0.9
Frequency Penalty: 0.0 | Presence Penalty: 0.0
================================================================================

1. Spanish - 'pantano'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: weather/environment
   'As the rain poured endlessly, the flat landscape transformed into a vast pantano, making navigation nearly impossible for the explorers.'

2. Context: General/Other
   'The villagers warned of dangerous creatures lurking in the pantano, hidden among the thick fog and tangled vegetation.'

3. Context: nature/outdoor
   'After a long trek through the forest, they finally reached the pantano, where the ground was soft and waterlogged underfoot.'

4. Context: weather/environment
   'The pantano was teeming with life, from croaking frogs to swarming insects, thriving in the wet and murky environment.'

5. Context: General/Other
   'They had to cross the pantano, a swampy area with muddy waters and reeds, to reach the old cabin on the other side.'

----------------------------------------

2. Spanish - 'colina'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'As the sun dipped below the horizon, shadows lengthened across the verdant colina, whispering secrets of ancient tales.'

2. Context: morning/routine
   'The morning mist clung to the colina, its presence softening the outline of what the village folk called their gentle giant.'

3. Context: General/Other
   'Children ran laughing, their feet barely touching the earth as they chased each other up and down the grassy colina that rose just outside town.'

4. Context: General/Other
   'On a clear day, you could see the entire valley from the top of the colina, a favorite spot for picnics and contemplation.'

5. Context: home/family
   'The old farmhouse sat proudly at the foot of the colina, surrounded by lush greenery and vibrant wildflowers that painted the landscape.'

----------------------------------------

3. Spanish - 'zancudo'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'In the twilight, a zancudo darted silently around the flickering porch light, an elusive shadow against the evening sky.'

2. Context: General/Other
   'As we lounged by the riverbank, a persistent zancudo buzzed by our ears, disrupting the tranquil afternoon with its annoying hum.'

3. Context: weather/environment
   'Swatting at the air, she exclaimed in frustration as another zancudo landed on her arm, ready to feast on her exposed skin.'

4. Context: General/Other
   'While camping in the humid jungle, our nights were filled with the irritating drone of zancudos seeking a warm-blooded meal.'

5. Context: nature/outdoor
   'To avoid the itchy welts left by the pesky zancudo, we diligently applied repellent before venturing outdoors at dusk.'

----------------------------------------

4. German - 'Schlafmütze'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'Despite the early start, Anton was the last to arrive, earning him the nickname schlafmütze among his punctual colleagues.'

2. Context: work/office
   'As the meeting commenced, everyone turned to Brian, who had forgotten his notes yet again, prompting Sarah to mutter "schlafmütze" under her breath.'

3. Context: morning/routine
   'The coach often used the term schlafmütze to describe players who lagged behind during morning practice sessions, much to their chagrin.'

4. Context: home/family, morning/routine
   '"Come on, you schlafmütze, we can't afford to wait for you to wake up every morning," Jane teased as her roommate hit snooze for the third time.'

5. Context: home/family, social/leisure
   'Even as the sun reached its zenith, Liam remained in bed, a classic schlafmütze, ignoring the day's activities until his friends eventually roused him.'


📊 CONFIGURATION: Medium Presence Penalty (Target)
Temperature: 1.2 | Top_p: 0.9
Frequency Penalty: 0.0 | Presence Penalty: 0.3
================================================================================

1. Spanish - 'pantano'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'The explorer's journal was full of tales from distant lands, one describing a pantano that swallowed all who dared tread upon its murky depths.'

2. Context: General/Other
   'Legends spoke of treasures hidden beneath the reeds of the pantano, guarded by creatures lurking just below the surface.'

3. Context: nature/outdoor
   'As they trudged through the dense forest, the humidity thickened and soon the trail led them to a pantano, its stagnant waters reflecting the twilight sky.'

4. Context: weather/environment
   'Farmers often warned newcomers about venturing too close to the pantano during the rainy season, as the land would transform into a sprawling mire.'

5. Context: General/Other
   'The guide pointed out the distinct sound of frogs and buzzing insects that thrived in the pantano, making it clear that this wetland was teeming with life.'

----------------------------------------

2. Spanish - 'colina'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'In the distance, the sun slowly disappeared behind a mysterious colina, casting shadows over the valley below.'

2. Context: General/Other
   'She sat quietly on the edge of the colina, contemplating the town nestled at its base, wondering how life might differ on flatter lands.'

3. Context: General/Other
   'The winding path led them up the grassy colina, where a lone tree stood as a sentinel at the top.'

4. Context: General/Other
   'As they ascended the colina, the panoramic view of the countryside revealed lush fields stretching to the horizon.'

5. Context: General/Other
   'The children rolled down the gentle slope of the colina, laughing as they raced each other to the bottom.'

----------------------------------------

3. Spanish - 'zancudo'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'As she sat quietly by the campfire, the persistent zancudo found its way to her exposed arm, causing a slight itch.'

2. Context: weather/environment
   'He swatted at the air in frustration as the annoying buzz of the zancudo hovered near his ear.'

3. Context: weather/environment
   'The tropical climate seemed to attract more than just tourists; each night, a zancudo would sneak into their bungalow, leaving bites.'

4. Context: nature/outdoor, weather/environment
   'While exploring the rainforest, they realized they should have packed repellent as the zancudo bites quickly covered their legs.'

5. Context: General/Other
   'On summer nights by the lake, they often complained about the pesky zancudo, commonly known for spreading itchy welts and diseases.'

----------------------------------------

4. German - 'Schlafmütze'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: work/office, home/family
   'The board meeting dragged on endlessly, but Thomas, our habitual schlafmütze, seemed blissfully unaware of the urgency in the room.'

2. Context: General/Other
   'Even during the most vibrant festivals, Jana remains a true schlafmütze, never fully embracing the excitement buzzing around her.'

3. Context: nature/outdoor
   'While everyone scrambled to catch the bus, Mark's schlafmütze nature made him lose track of time, resulting in another missed ride.'

4. Context: morning/routine
   'Despite the early morning joggers and chirping birds, Emily hit snooze for the third time, proving once again that she is quite the schlafmütze.'

5. Context: General/Other
   'In the heart of the bustling city, amidst honking horns and crowded sidewalks, Max continued to wander slowly, a true schlafmütze lost in his own world.'


📊 CONFIGURATION: High Presence Penalty (Max Diversity)
Temperature: 1.2 | Top_p: 0.9
Frequency Penalty: 0.0 | Presence Penalty: 0.6
================================================================================

1. Spanish - 'pantano'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: home/family
   'The novel’s eerie setting described an isolated pantano, shrouded in perpetual mist and the calls of unseen creatures.'

2. Context: weather/environment
   'As the sun set, the researchers realized their camp was perilously close to the edge of a pantano known for its shifting terrain.'

3. Context: travel/transport
   'Navigating through the dense jungle, the explorers carefully avoided the pantano, mindful of its deep, murky waters and hidden dangers.'

4. Context: weather/environment
   'During the rainy season, the fields near the village often transformed into a pantano, trapping vehicles and livestock in its thick mud.'

5. Context: General/Other
   'The children were warned not to play near the pantano, where water lilies floated on the surface of the swampy, still water.'

----------------------------------------

2. Spanish - 'colina'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: nature/outdoor, weather/environment
   'The castle ruins, barely visible from the edge of the dense forest, sat atop a lone colina, its stones weathered by centuries of rain and wind.'

2. Context: General/Other
   'As the sun began to set, she enjoyed the vibrant colors that painted the sky while standing on the colina overlooking the small village.'

3. Context: General/Other
   'After a long day of hiking, they finally reached the crest of the colina and were rewarded with a panoramic view of the sprawling countryside.'

4. Context: home/family
   'The sheep grazed peacefully on the lush grass of the colina, undisturbed by the occasional gentle breeze that swept across the landscape.'

5. Context: General/Other
   'From the playground, children rolled down the slope of the colina, laughing and tumbling all the way to the bottom.'

----------------------------------------

3. Spanish - 'zancudo'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: travel/transport
   'During our trip through the dense jungle, we heard the distinct hum of a zancudo near our ears.'

2. Context: General/Other
   'As dusk settled in, Maria warned us to use repellent or risk being bitten by a zancudo.'

3. Context: General/Other
   'Despite the tropical breeze, we couldn't escape the persistence of the zancudo buzzing around our campsite.'

4. Context: nature/outdoor
   'Every evening by the river, children playfully swat away zancudos as they enjoy their summer nights outdoors.'

5. Context: weather/environment
   'The humid air of the swamp was perfect for the zancudo, which often left itchy bites on our skin.'

----------------------------------------

4. German - 'Schlafmütze'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'During our climb up the mountain, Alan lagged behind like a true schlafmütze, oblivious to the rest of us reaching the summit.'

2. Context: home/family, morning/routine
   'Even when the alarm blared loudly, she remained in bed, earning her the nickname schlafmütze from her exasperated roommate.'

3. Context: work/office
   'At the office meeting, Mark's tardiness was excused as him being a bit of a schlafmütze, which made everyone chuckle knowingly.'

4. Context: General/Other
   'Jenny, known for her schlafmütze tendencies, missed the bus again because she couldn't resist hitting the snooze button.'

5. Context: General/Other
   'Despite having three cups of coffee, Tom continued to yawn through the presentation, living up to his reputation as the team's resident schlafmütze.'


📊 CONFIGURATION: Balanced with Frequency Penalty
Temperature: 1.2 | Top_p: 0.9
Frequency Penalty: 0.2 | Presence Penalty: 0.3
================================================================================

1. Spanish - 'pantano'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'The explorers trudged through the dense foliage, each step sucking into the thick mud of the pantano as they pushed deeper into the uncharted territory.'

2. Context: General/Other
   'As the evening mist rose from the surface of the pantano, eerie calls of unseen creatures echoed across the waterlogged landscape.'

3. Context: General/Other
   'Lost in thought, Maria sat by the edge of the pantano, watching as a heron delicately balanced on one leg amidst the murky waters.'

4. Context: weather/environment
   'The guide warned us to stick to the trail, as venturing too far could lead us into the treacherous terrain of the pantano, known for its unpredictable and dangerous footing.'

5. Context: General/Other
   'On our hike, we came upon a pantano, a large swampy area where water lilies floated serenely and alligators could sometimes be seen sunning themselves on fallen logs.'

----------------------------------------

2. Spanish - 'colina'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'He looked out over the horizon and watched as the sun dipped behind the distant colina.'

2. Context: General/Other
   'The old cottage sat alone atop the colina, offering a panoramic view of the valley below.'

3. Context: General/Other
   'As we hiked upward, the path wound around the colina, revealing a landscape dotted with wildflowers.'

4. Context: General/Other
   'Children often played on the gentle slope of the colina, rolling down its grassy sides with laughter.'

5. Context: General/Other
   'From the top of the colina, we could see both the city skyline and the vast open countryside stretching far and wide.'

----------------------------------------

3. Spanish - 'zancudo'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'At night, the persistent buzz of a zancudo kept me from enjoying the silence by the riverbank.'

2. Context: General/Other
   'While camping in the humid jungle, we realized a zancudo had slipped into our tent unnoticed.'

3. Context: weather/environment
   'We tried various sprays and nets to fend off the pesky zancudo that thrived in the muggy summer air.'

4. Context: General/Other
   'The children complained about itchy red bumps on their arms after a zancudo bit them while playing outside.'

5. Context: General/Other
   'As we sat by the bonfire, she slapped her arm and sighed, "Another zancudo got me; these mosquitoes are relentless!"'

----------------------------------------

4. German - 'Schlafmütze'
--------------------------------------------------
✅ Generated 5 sentences

1. Context: General/Other
   'Despite the lively chatter around the campfire, Alex sat there like a schlafmütze, seemingly lost in a world of his own.'

2. Context: weather/environment
   'During the team's intense brainstorming session, Mia's schlafmütze demeanor earned her a few concerned glances from her peers.'

3. Context: weather/environment
   'At the bustling train station, he stood still as a schlafmütze, oblivious to the flurry of commuters rushing past him.'

4. Context: morning/routine
   'After staying up late watching movies, Sarah became such a schlafmütze that morning that she barely responded when her alarm blared.'

5. Context: morning/routine
   '"Wake up, you schlafmütze!" his sister yelled playfully as she shook him awake from his prolonged nap on the couch.'


📈 CONTEXT DIVERSITY ANALYSIS
================================================================================
Context diversity analysis would go here...

✅ Testing complete!
Check the output above to see how presence penalty affects context diversity.
