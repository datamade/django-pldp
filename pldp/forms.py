from django.utils.translation import ugettext as _

# This is just a stubbed out module to get the beginnings of how we might want
# to handle form validation together. Originally I had some of this logic in
# the models and it was really not working over there and it seemed like the
# forms might be a better place for it.
#
# The thinking here is that, when a survey component is created, we'll save the
# kind of component and the level of detail that we'll want to capture in the
# responses. The catch is that, sometimes there is only one choice so we'll
# need to make sure that when we are doing the form validation, we are using
# the correct list of choices. The logic for that should live downstream of
# this app. My feeling is that this app should only provide the basic tools for
# storing info about a survey and data collected from a survey and if you want
# to make a tool that makes surveys, you'll need to implement that logic in
# your app.

# Survey metadata
SURVEY_TIME_CHARACTER_CHOICES = [
    ('None', _('None')),
    ('cultural/communal event', _('Cultural/Communal Event')),
    ('political/religious activity', _('Political/Religious Activity')),
    ('commercial event', _('Commercial Event')),
    ('national/local holiday', _('National/Local Holiday')),
    ('accident/emergency', _('Accident/Emergency')),
    ('roadwork/construction', _('Roadwork/Construction'))
]

SURVEY_REPRESENTATION_CHOICES = [
    ('absolute', _('Absolute')),
    ('relative', _('Relative'))
]

SURVEY_MICROCLIMATE_CHOICES = [
    ('sun - exposed', _('Sun - Exposed')),
    ('sun - shaded', _('Sun - Shaded')),
    ('light clouds', _('Light Clouds')),
    ('heavy clouds', _('Heavy Clouds')),
    ('light rain', _('Light Rain')),
    ('heavy rain', _('Heavy Rain')),
    ('fog', _('Fog')),
    ('light wind', _('Light Wind')),
    ('heavy wind', _('Heavy Wind')),
    ('thunder', _('Thunder')),
    ('light snow', _('Light Snow')),
    ('heavy snow', _('Heavy Snow')),
]

SURVEY_METHOD_CHOICES = [
    ('analog', _('Analog')),
    ('video', _('Video')),
    ('motion sensor', _('Motion sensor')),
    ('pressure sensor', _('Pressure sensor')),
    ('Wi-Fi signal', _('Wi-Fi signal')),
    ('GPS', _('GPS')),
    ('radar', _('Radar')),
    ('cell tower', _('Cell tower')),
    ('digital application', _('Digital application')),
    ('drone', _('Drone')),
    ('road tubes', _('Road tubes')),
]

# Choices for gender_observational question
GENDER_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
]

GENDER_BASIC_CHOICES = [
    ('male', _('Male')),
    ('female', _('Female')),
    ('unknown', _('Unknown')),
]

# Choices for age_observational question
AGE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
    ('complex', _('Complex choices')),
]
AGE_BASIC_CHOICES = [
    ('0-14', _('0-14')),
    ('15-24', _('15-24')),
    ('25-64', _('25-64')),
    ('65+', _('65+')),
]
AGE_DETAILED_CHOICES = [
    ('0-4', _('0-4')),
    ('5-14', _('5-14')),
    ('15-24', _('15-24')),
    ('25-44', _('25-44')),
    ('45-64', _('45-64')),
    ('65-74', _('65-74')),
    ('75+', _('75+')),
]
AGE_COMPLEX_CHOICES = [
    ('0-4', _('0-4')),
    ('5-9', _('5-9')),
    ('10-14', _('10-14')),
    ('15-17', _('15-17')),
    ('18-24', _('18-24')),
    ('25-34', _('25-34')),
    ('35-44', _('35-44')),
    ('45-54', _('45-54')),
    ('55-64', _('55-64')),
    ('65-74', _('65-74')),
    ('75+', _('75+')),
]

# Choices for mode_observational question
MODE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
]

MODE_BASIC_CHOICES = [
    ('pedestrian', _('Pedestrian')),
    ('bicyclist', _('Bicyclist')),
    ('animal', _('Moving by animal')),
    ('snow', _('Moving in snow')),
    ('water', _('Moving by water')),
    ('vehicle', _('Moving by vehicle')),
]

MODE_DETAILED_CHOICES = [
    ('pedestrian_walking', _('Pedestrian walking')),
    ('pedestrian_running', _('Pedestrian running')),
    ('pedestrian_supported', _('Pedestrian supported (e.g. by cane, crutches, \
        or a wheelchair)')),
    ('pedestrian_carried', _('Pedestrian carried (e.g. by stroller, cart, \
        or another pedestrian)')),
    ('pedestrian_rolling', _('Pedestrian rolling (e.g. with a scooter, \
        skateboard, or rollerblades)')),
    ('bicyclist_private_individual', _('Bicyclist, private individual')),
    ('bicyclist_private_multiple', _('Bicyclist, private multiple \
        (e.g. tandem bike)')),
    ('bicyclist_commercial_individual', _('Bicyclist, commercial individual \
        (e.g. bikeshare)')),
    ('bicyclist_commercial_multiple', _('Bicyclist, commercial multiple \
        (e.g. pedicab, rickshaw)')),
    ('animal_riding', _('Riding an animal')),
    ('animal_carriage', _('Moving by animal carriage')),
    ('snow_manual', _('Moving in snow manually (e.g. by ski, snowboard, or \
        sled)')),
    ('snow_powered', _('Moving in a powered snow vehicle \
        (e.g. by snowmobile)')),
    ('water_no_vessel', _('Moving by water, no vessel (e.g. swimming)')),
    ('water_small_vessel', _('Moving by water, small vessel (e.g. by canoe, \
        kayak, or surfboard)')),
    ('water_medium_vessel', _('Moving by water, medium vessel (e.g. by \
        sailboat or motorboat)')),
    ('water_large_vessel', _('Moving by water, large vessel (e.g. by ship, \
        yacht, or ferry)')),
    ('vehicle_private', _('Moving by private vehicle (e.g. by automobile \
        or motorcycle)')),
    ('vehicle_commercial', _('Moving by commercial vehicle (e.g. by taxi or \
        rideshare)')),
    ('vehicle_public', _('Moving by public vehicle (e.g. by bus or train)')),
]

# Choices for posture_observational question
POSTURE_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
]

POSTURE_BASIC_CHOICES = [
    ('standing', _('Standing')),
    ('sitting_formal', _('Sitting formally (in places intended for sitting)')),
    ('sitting_informal', _('Sitting informally (in places not intended for \
        sitting)')),
    ('lying', _('Lying')),
    ('multiple', _('In multiple postures')),
]

POSTURE_DETAILED_CHOICES = [
    ('standing', _('Standing')),
    ('leaning', _('Leaning')),
    ('sitting_formal_commercial', _('Sitting on furniture owned by a commercial \
        establishment.')),
    ('sitting_formal_private', _('Sitting on privately owned furniture')),
    ('sitting_formal_office', _('Sitting on furniture owned by a company and intended \
        for use by its employees')),
    ('sitting_formal_support', _('Sitting on a stroller, wheelchair, or \
        walker')),
    ('sitting_formal_public_fixed', _('Sitting on a fixed object intended as seating \
        and provided for the general public such as a bench or picnic table')),
    ('sitting_formal_public_movable', _('Sitting on a movable object intended as seating \
        and provided for the general public such as a chair')),
    ('sitting_informal_ground', _('Sitting on the ground')),
    ('sitting_informal_object', _('Sitting on objects not designed for \
        sitting')),
    ('sitting_informal_architecture', _('Sitting on pieces of architecture not \
        designed for sitting')),
    ('lying_ground', _('Lying down on the ground')),
    ('lying_furniture', _('Lying down on a piece of furniture')),
    ('multiple_light', _('In multiple postures due to a light amount of \
        physical activity (e.g. walking dog, gardening)')),
    ('multiple_heavy', _('In multiple postures due to a heavy amount of \
        physical activity (e.g. exercising, playing)')),
]

# Choices for activity_observational question
ACTIVITY_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
    ('detailed', _('Detailed choices')),
]

ACTIVITY_BASIC_CHOICES = [
    ('commercial', _('Buying or selling goods')),
    ('consuming', _('Consuming food or drink')),
    ('conversing', _('Conversing with another person')),
    ('cultural', _('Participating in or observing a cultural activity of either \
        artistic, communal, political, or religious character')),
    ('disruptive', _('Displaying abusive behavior, intoxication, or visibly \
        ingesting alcohol or drugs')),
    ('electronic_engagement', _('Engaging with technology or electronics')),
    ('living_public', _('Engaging in otherwise private sanitary activities \
        within the public realm or encamping, lying, or sleeping in an \
        undesignated camping/sleeping location')),
    ('recreation_active', _('Active recreation (e.g. exercising or playing)')),
    ('recreation_passive', _('Passive recreation (e.g. reading, painting, or \
        sightseeing)')),
    ('smoking', _('Smoking')),
    ('soliciting', _('Soliciting')),
    ('waiting_transfer', _('Waiting for transportation')),
    ('waiting_other', _('Waiting, other')),
    ('working_civic', _('Working to upkeep or take care of the public space')),
]

ACTIVITY_DETAILED_CHOICES = [
    ('commercial_providing', _('Selling goods')),
    ('commercial_participating', _('Buying goods or observing goods being \
        sold')),
    ('consuming', _('Consuming food or drink')),
    ('conversing', _('Conversing with another person')),
    ('cultural_providing', _('Participating in a cultural activity of either \
        artistic, communal, political, or religious character')),
    ('cultural_participating', _('Observing a cultural activity of either \
        artistic, communal, political, or religious character')),
    ('disruptive_aggressive', _('Displaying abusive behaviour towards another \
        person or to no one in particular.')),
    ('disruptive_intoxicated', _('Visibly ingesting alcohol or drugs in an \
        unsanctioned context or showing clear signs of uncontrolled \
        intoxication')),
    ('electronic_engagement_introverted', _('Engaging with technology or \
        electronics in an introverted fashion (e.g. listening to music with \
        earbuds, typing on a computer, or charging a device)')),
    ('electronic_engagement_extroverted', _('Engaging with technology or \
        electronics in an extroverted fasion (e.g. playing audio from \
        speakers or taking photos)')),
    ('living_public_sanitising', _('Engaging in otherwise private sanitary activities \
        within the public realm (e.g. urinating or showering)')),
    ('living_public_encamping', _('Encamping, lying, or sleeping in an \
        undesignated camping/sleeping location')),
    ('recreation_active_exercising', _('Exercising')),
    ('recreation_active_playing', _('Physically active playing')),
    ('recreation_passive_observing', _('Actively or intentionally observing \
        other people, activities, landmarks, buildings, nature, landscape, or \
        other')),
    ('recreation_passive_playing', _('Playing passive, analogue, stationary \
        games, like a board  or card game')),
    ('recreation_passive_affectionate', _('Showing physical affection towards \
        another person.')),
    ('recreation_passive_reading', _('Reading a printed newspaper or book or \
        writing in a notebook')),
    ('recreation_passive_creating', _('Engaging in a creative activity for \
        personal use or purpose, like creating a drawing or painting, or \
        playing music for one\'s personal enjoyment')),
    ('recreation_passive_resting', _('Sleeping, relaxing, or hanging out \
        for recreational purposes and in areas designated for resting like a \
        beach, park, or street bench')),
    ('smoking', _('Smoking')),
    ('soliciting_begging', _('Begging')),
    ('soliciting_campaigning', _('Campaigning')),
    ('soliciting_sex_work', _('Requesting or providing sex work')),
    ('waiting_transfer_public', _('Waiting for public transportation')),
    ('waiting_transfer_private', _('Waiting for private transportation \
        (e.g. a car)')),
    ('waiting_transfer_commercial', _('Waiting for a taxi or rideshare')),
    ('waiting_other_interrupted', _('Waiting for traffic or at a red light, \
        midblock, or other, in order to continue a journey through the \
        space')),
    ('waiting_other_wayfinding', _('Waiting to find a route or destination')),
    ('working_civic', _('Working to upkeep or take care of the public space')),
]

# Choices for objects_observational question
OBJECTS_TYPE_CHOICES = [
    ('basic', _('Basic choices')),
]

OBJECTS_BASIC_CHOICES = [
    ('animal', _('People carrying or watching over a domestic animal')),
    ('bag_carried', _('People carrying a bag or larger personal belonging')),
    ('clothing_cultural_symbols', _('People wearing or carrying clothing of \
        perceived religious character')),
    ('clothing_activity_symbols', _('People wearing or carrying clothing of \
        perceived active character')),
    ('goods_carried', _('People carrying or delivering goods, typically \
        moving house or delivering to a private or commercial \
        establishment')),
    ('equipment_construction', _('People carrying equipment for use in a \
        construction project')),
    ('equipment_recreational', _('People carrying equipment for recreational \
        use')),
    ('equipment_sport', _('People carrying equipment that is perceived to be for use \
        when exercising or playing')),
    ('protection_safety', _('People wearing a piece of safety equipment \
        (e.g. a bike helmet, construction helmet, or gas mask)')),
    ('protection_weather', _('People carrying an object that is intended to \
        protect from weather-related discomfort (e.g. umbrella or snow \
        shovel)')),
    ('furniture_carried', _('People carrying a piece of furniture')),
    ('transportation_carried', _('People carrying (not riding) a personal \
        conveyance (e.g. a skateboard, rollerblades, or bicycle)')),
    ('transportation_stationary', _('People using an object of transpiration \
        for stationary support (e.g. a walker, wheelchair, or shopping \
        cart)')),
]
