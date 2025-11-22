
keys = ['tvShow', 'sensoryHijack', 'timeSink', 'adPressure', 'frictionToIntent', 'cognitiveCaptureNegative', 'educational', 'quality', 'moralLesson', 'theme', 'cognitiveNutrition', 'notes', 'total']
images = ['the-goonies.jpg', 'star-wars-rebels.jpg', 'paw-patrol.jpg', 'peppa-pig.jpg', 'doc-mcstuffins.jpg', 'my-little-pony.jpg', 'transformers-prime.jpg', 'transformers-roll-out.jpg', 'teen-titans-go.jpg', 'the-amazing-world-of-gumball.jpg', 'coco-melon.jpg', 'miss-rachel.jpg', 'bluey.jpeg', 'sponge-bob.png', 'phineas-and-ferb.jpg', 'mickey-mouse-clubhouse.jpg', 'tom-and-jerry.jpg', 'dora-the-explorer.jpg', 'doc-mcstuffins.jpg', 'gravity-falls.jpg', 'adventure-time.jpg', 'steven-universe.jpg', 'backyardigan.jpg', 'octonauts.jpg', 'wild-kratts.jpg', 'magic-school-bus.jpg', 'arthur.jpg', 'the-loud-house.jpg', 'curious-George.jpg', 'courage-the-cowardly-go.jpg', 'mr-bean.jpg', 'owl-house.png', 'steven-universe.jpg', 'masha-and-the-bear.jpg', 'fairly-odd-parents.jpg', 'shaun-the-sheep.jpg', 'sesame-street.jpg', 'avatar-the-last-air-bender.jpg', 'horrid-henry.jpg', 'craig-of-the-creek.jpg', 'big-city-green.jpg', 'thomas-and-friends.jpg', 'bob-the-builder.jpg', 'spirited-away.jpg', 'larva.jpg', 'mr-beast.jpg']
records = []
with open('input.txt', 'r') as f:
    records = f.readlines()
with open('output.txt', 'w') as f:
    for i in range(len(records)):
        records[i] = records[i].split(",")
        records[i] = [ '"' + records[i][0] + '"' ] + records[i][1:-1] + [ str(float(records[i][5])+float(records[i][10])) ]
        f.write("{\nid: " + f"{i+1},\n")
        f.write("image: " + f'"{images[i]}",\n')
        f.write("\n".join([f"{a}: {b if b else 0}," for a, b in zip(keys,records[i])]))
        f.write("\n},\n")
