# The data for your website
import json

user_id = 2;
curr_id = 7;
data = {
    "users":[
        {
            'id': 1,
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
        }
    ],
    "recipes":[
        {
            "id": 1,
            "name": 'Beauty School Knockout',
            "description": '''  When my sister and I were thinking of soda fountain creations, our ideas revolved around iconic flavors and colors of the 1950s. After brainstorming the myriad of soda fountain treats, we couldn't think of a more fitting indulgence than the classic ice cream sundae. We settled on one of our favorite ice cream flavors, peppermint, which also happens to be a lovely shade of Cadillac pink- sure to win the Pink Ladies' approval''',
            "preperation": '''  Heat the milk, cream and peppermint candy in a large pot over medium heat, until the peppermints are dissolved, and the mixture is steamy.
                                Meanwhile, beat the egg yolks, sugar and salt in an electric mixer fitted with the whisk attachment for about five minutes (the yolks should be very thick, pale and glossy).
                                When the milk mixture is ready, add a small amount of it to the egg mixture, whisking all the while so as to not scramble the eggs. Add the rest of the liquid gradually as the mixer continues to run, creating a homogenous mixture.
                                Pour the mixture back into the pot, and cook slowly over medium heat--stirring constantly--until the mixture registers 170 degrees on a candy thermometer. Whatever you do, do not let the mixture boil.
                                As soon as the custard is ready, pour it through a fine mesh sieve into a bowl, in order to remove any coagulated egg bits.
                                Stir in the peppermint extract, and allow to cool. Chill until very cold, at least four hours.
                                Churn in an ice cream maker, according to manufacturer's instructions.
                                During the last minute of churning, gently fold in the broken cookie pieces.
                                Devilish Hot Fudge Sauce
                                Heat the butter and cream to a boil in a small saucepan.
                                Add the sugars and corn syrup, stirring constantly.
                                Add the cocoa and salt. Stir well.
                                Add the chocolate chips and mix until melted.
                                Off the heat, add the vanilla extract.
                                Sundae time! Also have ready: Freshly whipped cream (cream, a spot of confectioner's sugar and vanilla). Extra chocolate cookies, for garnish. Dark chocolate curls, for garnish. Peppermint sticks, for garnish. For assembly: Alternate scoops of ice cream with fudge sauce, and broken chocolate cookies. Crown with a cloud of whipped cream, drizzle with a few ribbons of fudge, and sprinkle with an abundance of chocolate curls. Complete the look by parking a swirly, twirly peppermint stick in the top. Now try not to inhale''',
            "ingredients": '''  Pink Peppermint Ice Cream
                                2 cups whole milk
                                1 1/4 cups heavy cream
                                5 large egg yolks
                                1/2 cup sugar
                                roughly 1/2 cup of chopped peppermint candies (We like King Leo peppermint sticks)
                                1 pinch salt
                                1 teaspoon peppermint extract (the best quality you can find)
                                about 1/3 of a package of chocolate cookies (We like Nabisco's Famous Chocolate Wafers), roughly broken
                                Devilish Hot Fudge Sauce
                                5 tablespoons heavy cream
                                1 tablespoon butter
                                2 tablespoons granulated sugar
                                2 1/2 tablespoons dark brown sugar
                                1 pinch sea salt
                                2 tablespoons corn syrup
                                1/4 cup Dutch processed cocoa powder
                                1 1/2 ounces of chopped dark chocolate (chocolate chips work fine too-about 1/4 cup)
                                1 splash pure vanilla extract''',
            "image": 'images/recipies/dish1.jpg',
            "video": 'https://www.youtube.com/embed/SWEli_xReo8',
            "category": 'Desserts',
            "author": 'Scott Tsoie'
        },
        {
            "id": 2,
            "name": 'Ricotta, Feta and Mint Layers with Honeyed Blood Oranges',
            "description": '''I love the sweetness and tanginess of these ingredients. Sometimes, if I’m really impatient, I’ll skip the ricotta and the loaf pan, chunk the feta and mix it with torn mint and the honeyed oranges, and serve it in small bowls. It’s almost a dessert. Or a great cheese course for sweet dessert eaters like me. My recipe is adapted from Ricotta and Caprino Layered with Fresh Basil Leaves, from the cookbook My Italian Garden by Viana La Place.''',
            "preperation": '''  In a shallow bowl or dish, mash the feta with the back of a fork. Add the ricotta and stir together very well.
                                Lightly oil a 3” x 6” mini loaf pan with olive oil.
                                Spread 1/3 of the cheese mixture into the bottom of the pan. Cover with a single layer of mint leaves, and gently press them into the cheese. Drizzle with olive oil and sprinkle with sea salt. Continue with another layer of cheese, followed by a layer of mint leaves, drizzle of olive oil and sprinkle of sea salt. Spread the last layer of cheese on top, another drizzle of olive oil and a sprinkle of sea salt. Place a piece of plastic wrap on the top layer of cheese to keep it moist.
                                Combine the honey and chopped orange segments in a bowl. Squeeze the juice from the reserved membrane onto the segments. Stir together gently.
                                Remove the plastic wrap from the cheese. Invert the mini loaf pan onto a serving dish. Spoon the honeyed oranges over top.
                                Garnish with additional fresh mint leaves. Serve with pita chips, pita bread wedges, or crostini.''',
            "ingredients": '''  4 ounces feta
                                4 ounces ricotta
                                large bunch of fresh mint leaves
                                olive oil
                                sea salt
                                4 tablespoons buckwheat honey
                                2 blood oranges, segmented and chopped, membranes reserved''',
            "image": 'images/recipies/dish2.jpg',
            "video": 'https://www.youtube.com/embed/4Ap4vmefetc',
            "category": 'Desserts',
            "author": 'More Nelson'
        },
        {
            "id": 3,
            "name": 'Strawberry-Fennel Ice Cream',
            "description": '''  I haven't been very active on Food52 of late as I've been on a rather intense journey discovering the benefits of raw milk, lacto-fermentation and ancient grains—perhaps a bit out there for this crowd? But I came up with this recipe using raw cream, eggs straight from the farm, agave nectar and fennel pollen that tastes just like spring. The beautiful pink color comes from a puree of strawberries but there are also chunks of whole berry to add texture to the creamy base. - gluttonforlife —gluttonforlife''',
            "preperation": '''  Combine cream, zest, fennel pollen and salt in a heavy saucepan and bring to a boil. Remove from heat and discard zest.
                                Whisk eggs with 2/3 cup agave nectar in a bowl, then add hot cream in a slow stream, whisking constantly. Pour back into saucepan and cook over moderately low heat, stirring constantly, until slightly thickened and an instant-read thermometer registers 170°. Do not boil!
                                Immediately pour custard through a fine sieve into a metal bowl, then cool to room temperature, stirring occasionally. Cover and chill until cold, at least 2 hours and up to 1 day.
                                While custard is chilling, purée strawberries with lemon juice and remaining 3 tablespoons agave nectar until smooth, then force through fine sieve to remove seeds (or not, this step is optional) into chilled custard. Stir purée into custard.
                                Freeze in ice-cream maker. About ¾ of the way through (time varies depending on your machine), stir in strawberry chunks. Finish freezing, then transfer to an airtight container and put in freezer to harden.''',
            "ingredients": '''  13/4 cup heavy raw or organic cream
                                3 fat strips of lemon zest
                                1/2 teaspoon fennel pollen
                                1/8 teaspoon sea salt
                                2 large free-range eggs
                                2/3 cup plus 3 tablespoons agave nectar, separated
                                3 cups ripe strawberries, trimmed and halved
                                1 cup strawberries, trimmed and cut into chunks
                                juice of 1/2 lemon''',
            "image": 'images/recipies/dish3.jpg',
            "video": 'https://www.youtube.com/embed/xDW-BZuEIns',
            "category": 'Desserts',
            "author": 'Jacobs Walker'
        },
        {
            "id": 4,
            "name": '''Craig Claiborne's Pasta con Asparagi''',
            "description": '''A mashup of all the best pasta sauces—tomato, asparagus, and carbonara—with surprisingly harmonious results. Adapted slightly from The New New York Times Cookbook (Crown, 1979) —Genius Recipes''',
            "preperation": '''  Have all the ingredients for this recipe prepared and ready to cook before beginning. Bring about 3 quarts of water to a boil and have it ready for the pasta.
                                Cut the asparagus into lengths about 2 inches long. If the stalks are thick, cut them in half or quarter them. Leave the tips in tact. Heat the butter in a large, deep skillet and add the asparagus pieces, salt, and pepper to taste. Cook for 4 to 5 minutes, or until crisp-tender and lightly browned. Transfer the asparagus to a plate and reserve.
                                In the same pan, add the oil and garlic. Cook until lightly browned and remove and discard garlic. Add the tomatoes, parsley, basil, salt and pepper to taste. Cook, stirring, for about 10 minutes.
                                Meanwhile, add the pasta and salt to the water and, when it returns to a boil, cook for about 7 minutes or until tender. Do not overcook.
                                Just before the pasta is done, turn off the heat under the tomatoes and add the beaten eggs, stirring vigorously so that they blend without curdling. Do not boil the sauce after the eggs are added. (If you are nervous about curdling the eggs, you may temper them in, by stirring a ladleful of the hot tomato sauce into the eggs, then whisking the mixture back into the pan.)
                                Add the asparagus to the tomato sauce and stir to blend.
                                Drain the pasta immediately. Add the tomato sauce and asparagus, and toss with half the cheese. Serve piping hot with the remaining cheese on the side.''',
            "ingredients": '''  1 1/2 pounds fresh asparagus
                                3 tablespoons butter
                                1 pinch salt and freshly ground pepper
                                2 1/2 tablespoons olive oil
                                2 cloves garlic
                                2 cups canned Italian plum tomatoes, put through a sieve or grated coarsely
                                1 tablespoon finely chopped fresh parsley
                                1 tablespoon finely chopped fresh basil
                                3/4 pound penne, rigatoni, or other tubular pasta
                                2 eggs, plus one yolk, beaten well with a fork
                                1/2 cup grated parmesan''',
            "image": 'images/recipies/dish4.jpg',
            "video": 'https://www.youtube.com/embed/jsUQ7WOntDc',
            "category": 'Pasta',
            "author": 'Harris Hill'
        },
        {
            "id": 5,
            "name": 'Miso Peanut Pasta Salad',
            "description": '''This is not your average macaroni salad. —mrslarkin''',
            "preperation": '''  Cook pasta to al dente. Reserve about a cup of the pasta water for the sauce and set aside. Drain pasta. Set aside in a large mixing bowl.
                                In a medium mixing bowl, place peanut butter, miso, vinegar, chili garlic sauce, ginger, garlic, honey, and sesame oil. Add pasta water in 1/8-cup increments and stir until you reach a smooth, sauce-like consistency. It should be loose, but not watery, so add the water slowly. Taste for seasoning.
                                Pour half of the sauce over the pasta and mix well. Reserving a bit of each vegetable and herb for garnishing, toss the remaining vegetables, cilantro, and sauce into the pasta, and mix well. Taste for seasoning.
                                Garnish with reserved vegetables, cilantro, and peanuts. Serve at room temperature.''',
            "ingredients": '''  1 pound whole-wheat elbow pasta, or your favorite shape
                                1/2 cup creamy peanut butter (I used natural unsweetened, which is more gritty, but use what you like)
                                1 heaping tablespoon white miso
                                2 tablespoons apple cider vinegar, or rice wine vinegar
                                2 teaspoons chili garlic sauce, plus more to taste (get a jar of the Huy Fong and stash it in the fridge -- it's ridiculously good)
                                2 teaspoons chopped ginger
                                1 garlic clove, minced
                                2 tablespoons honey (or less, if using sweetened peanut butter)
                                4 dashes sesame oil, plus more to taste
                                1 bunch scallions, trimmed and sliced
                                1/2 large watermelon radish, cut into 2-inch sticks
                                1 medium carrot, peeled and cut into 2-inch sticks
                                1 cup broccoli florets, blanched or lightly steamed, chopped
                                8 sprigs fresh cilantro, chopped, legs and all, plus extra for garnish
                                1/2 cup roasted peanuts, for garnish''',
            "image": 'images/recipies/dish5.jpg',
            "video": 'https://www.youtube.com/embed/xSW_sEnLygI',
            "category": 'Pasta',
            "author": 'John Baker'
        },
        {
            "id": 6,
            "name": '''Dandelion Greens Salad''',
            "description": '''One of the vendors at the Farmer's Market just started getting dandelion greens a couple of weeks ago, and I will say I was happy to see them! When I walked over to get them yesterday she asked me "are you ready for these?" and so - fair warning - they are an intense green. Strong and bitter, but I think balanced with some sweet and salt and richness they are absolutely delicious. - aargersi —aargersi''',
            "preperation": '''  Clean the dandelions: remove the thick part of the stems and gently tear the leaves into bite size pieces. Wash them and dry them very thoroughly. Put them in a big bowl that you can toss the salad in.
                                Prepare the leeks: I used the chop first, rinse second method, and then took them for a spin in the salad spinner to dry. It worked great! Use white and light green parts only and chop faily small - I quartered the leek and cut 1/4 inch strips. Put a large pot of salted water on and get it started for poaching the eggs, add a splash of white vinegar to the pot as well. Crack each egg into an individual dish.
                                Now cook the bacon in a skillet until crisp. Remove it to drain and turn the heat to medium. I didn't remove any fat from the pan but bacon differs - if you have a deep layer of fat in the pan maybe remove a little. Add the leeks and cook them until they are quite soft. Turn off the heat and add the vinegar, stirring to get the good bits up off the pan. Pour the leeks and all of the liquid into a small bowl, grind some pepper in and add the oilve oil and maple syrup. Whisk the dressing and taste - mine had plenty of salt from the bacon but add more if you need it. Also test acidity, you may want another splash of vinegar. Crumble the bacon onto the greens. Toss the warm dressing with the dandelion greens and bacon.
                                Poach the eggs: slide each one into the boiling water and let them poach for 3-4 minutes. While they are poaching go ahead and toss the greens a few more times (the warm dressing will wilt them ever so slightly) and then portion them onto 4 plates. Make sure that each plate gets equal amount of bacon or fights will break out.
                                Top each salad with a poached egg, grind a bit more pepper over the top, and serve. Enjoy the springtime!!!''',
            "ingredients": '''  1 big bunch of dandelion greens, about 4 heaping cups when cleaned
                                1 large leek (or 2 small ones)
                                6 strips bacon (some of the bacon inevitably gets swiped during the cooking process)
                                1/3 cup red wine vinegar
                                2 tablespoons maple syrup
                                1/4 cup olive oil
                                Pepper
                                4 eggs
                                A pot of salted water with a splash of white vinegar for poaching.''',
            "image": 'images/recipies/dish6.jpg',
            "video": 'https://www.youtube.com/embed/Yrw3rR7-Wy0',
            "category": 'Salad',
            "author": 'Adam Morgan'
        }
    ],
}

def get_data(params):
    try:
        index = int(params.pop('_index', 0))
        length = int(params.pop('_length', 0))
        collection = params.pop('_collection')
    except:
        print(1)
    if 'username' in params and 'password' in params:
        fd = list(filter(lambda user: params['username'] in user['username'] and params['password'] == user['password'], data['users']))
        if fd:
            return fd[0]['id']
        return None

    if '_title' in params and '_category' in params:
        cat = params.pop('_category')
        title = params.pop('_title')
        fd = list(filter(lambda element: title in element['name'] and cat == element['category'], data[collection]))
        return fd

    if '_category' in params:
        cat = params.pop('_category')
        fd = list(filter(lambda element: cat == element['category'], data[collection]))
        return fd

    if '_id' in params:
        id = params.pop('_id')
        fd = list(filter(lambda element: int(id) == element['id'], data[collection]))
        return fd

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]

def add_data(params):
    global curr_id
    global user_id

    if len(params) == 3:
        params['id'] = user_id
        user_id += 1
        data['users'].append(params)
        return user_id - 1

    if  len(params) > 3:
        params['id'] = curr_id
        curr_id += 1
        params['video'] = 'https://www.youtube.com/embed/' + params['video'].split('=')[-1]
        data['recipes'].append(params)
