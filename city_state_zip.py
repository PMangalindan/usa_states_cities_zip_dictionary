state_city_zipcode = {'Alabama':{'Birmingham': ['35203', '35204', '35205', '35206', '35207'],
                              'Montgomery': ['36104', '36105', '36106', '36107', '36108'],
                              'Huntsville': ['35801', '35802', '35803', '35805', '35806'],
                              'Mobile': ['36602', '36603', '36604', '36605', '36606'],
                              'Tuscaloosa': ['35401', '35404', '35405', '35406']},
                  'Alaska':{'Anchorage': ['99501', '99502', '99503', '99504', '99507'],
                              'Fairbanks': ['99701', '99709', '99712', '99790'],
                              'Juneau': ['99801'],
                              'Sitka': ['99835'],
                              'Wasilla': ['99623', '99654']},
                  'Arizona':{'Phoenix': ['85003', '85004', '85006', '85007', '85008'],
                            'Tucson': ['85701', '85704', '85705', '85706', '85708'],
                            'Mesa': ['85201', '85202', '85203', '85204', '85205'],
                            'Chandler': ['85224', '85225', '85226', '85248', '85249'],
                            'Scottsdale': ['85250', '85251', '85254', '85255', '85256']},
                  'Arkansas':{'Little Rock': ['72201', '72202', '72204', '72205', '72206'],
                            'Fort Smith': ['72901', '72903', '72904', '72908', '72916'],
                            'Fayetteville': ['72701', '72703', '72704'],
                            'Springdale': ['72762', '72764'],
                            'Jonesboro': ['72401', '72404', '72405']},
                  'California':{'Los Angeles': ['90001', '90002', '90003', '90004', '90005'],
                              'San Diego': ['92101', '92102', '92103', '92104', '92105'],
                              'San Jose': ['95101', '95110', '95111', '95112', '95113'],
                              'San Francisco': ['94101', '94102', '94103', '94104', '94105'],
                              'Fresno': ['93650', '93701', '93702', '93703', '93704']},
                  'Colorado': {'Denver': ['80202', '80203', '80204', '80205', '80206'],
                              'Colorado Springs': ['80902', '80903', '80904', '80905', '80906'],
                              'Aurora': ['80010', '80011', '80012', '80013', '80014'],
                              'Fort Collins': ['80521', '80524', '80525', '80526', '80528'],
                              'Lakewood': ['80722']},
                  'Connecticut': {'Bridgeport': ['06604', '06605', '06606', '06607', '06608'],
                              'New Haven': ['06510', '06511', '06513', '06515', '06519'],
                              'Hartford': ['06101', '06103', '06105', '06106', '06112'],
                              'Stamford': ['06901', '06902', '06903', '06905', '06906'],
                              'Waterbury': ['06701', '06702', '06704', '06705', '06706']},
                  'Delaware': {'Wilmington': ['19801', '19802', '19803', '19804', '19805'],
                              'Dover': ['19901', '19904', '19906'],
                              'Newark': ['19702', '19711', '19713', '19716', '19717'],
                              'Middletown': ['19709'],
                              'Smyrna': ['19977']},
                  'Florida': {'Jacksonville': ['32099', '32202', '32204', '32205', '32206'],
                              'Miami': ['33122', '33125', '33126', '33127', '33128'],
                              'Tampa': ['33602', '33603', '33604', '33605', '33606'],
                              'Orlando': ['32801', '32803', '32804', '32805', '32806'],
                              'St. Petersburg': ['33701', '33702', '33703', '33704', '33705']},
                  'Georgia': {'Atlanta': ['30303', '30304', '30305', '30306', '30307'],
                              'Augusta': ['30901', '30904', '30905', '30906', '30907'],
                              'Columbus': ['31901', '31903', '31904', '31906', '31907'],
                              'Savannah': ['31401', '31404', '31405', '31406', '31408'],
                              'Athens': ['30601', '30605', '30606', '30607']},
                  'Hawaii': {'Honolulu': ['96813', '96814', '96815', '96816', '96817'],
                              'Pearl City': ['96782'],
                              'Hilo': ['96720'],
                              'Kailua': ['96734'],
                              'Waipahu': ['96797']},
                  'Idaho': {'Boise': ['83702', '83703', '83704', '83705', '83706'],
                              'Meridian': ['83642', '83646'],
                              'Nampa': ['83651', '83686', '83687'],
                              'Idaho Falls': ['83401', '83402', '83404', '83406'],
                              'Pocatello': ['83201', '83202', '83204']},
                  'Illinois': {'Chicago': ['60601', '60602', '60603', '60604', '60605'],
                              'Aurora': ['60502', '60503', '60504', '60505', '60506'],
                              'Rockford': ['61101', '61102', '61103', '61104', '61107'],
                              'Joliet': ['60431', '60432', '60433', '60435', '60436'],
                              'Naperville': ['60540', '60563', '60564', '60565']},
                  'Indiana': {'Indianapolis': ['46201', '46202', '46203', '46204', '46205'],
                              'Fort Wayne': ['46802', '46803', '46804', '46805', '46806'],
                              'Evansville': ['47708', '47710', '47711', '47712', '47713'],
                              'South Bend': ['46601', '46613', '46614', '46615', '46616'],
                              'Carmel': ['46032', '46033']},
                  'Iowa':     {'Des Moines': ['50307', '50308', '50309', '50310', '50311'],
                              'Cedar Rapids': ['52401', '52402', '52403', '52404', '52405'],
                              'Davenport': ['52801', '52802', '52803', '52804', '52806'],
                              'Sioux City': ['51101', '51103', '51104', '51105', '51106'],
                              'Iowa City': ['52240', '52242', '52245', '52246']},
                  'Kansas': {'Wichita': ['67202', '67203', '67204', '67205', '67206'],
                              'Overland Park': ['66204', '66207', '66210', '66212', '66213'],
                              'Kansas City': ['66101', '66102', '66103', '66104', '66105'],
                              'Topeka': ['66603', '66604', '66605', '66606', '66607'],
                              'Olathe': ['66061', '66062']},
                  'Kentucky': {'Louisville': ['40202', '40203', '40204', '40205', '40206'],
                              'Lexington': ['40502', '40503', '40504', '40505', '40507'],
                              'Bowling Green': ['42101', '42103', '42104'],
                              'Owensboro': ['42301', '42303'],
                              'Covington': ['41011', '41014', '41016']},
                  'Louisiana': {'New Orleans': ['70112', '70113', '70114', '70115', '70116'],
                              'Baton Rouge': ['70801', '70802', '70805', '70806', '70807'],
                              'Shreveport': ['71101', '71103', '71104', '71105', '71106'],
                              'Lafayette': ['70500', '70501', '70503', '70506', '70507'],
                              'Lake Charles': ['70601', '70605', '70607', '70611', '70615']},
                  'Maine': {'Portland': ['04101', '04102', '04103', '04109'],
                              'Lewiston': ['04240'],
                              'Bangor': ['04401'],
                              'South Portland': ['04106'],
                              'Auburn': ['04210']},
                  'Maryland': {'Baltimore': ['21201', '21202', '21205', '21206', '21209'],
                              'Frederick': ['21701', '21702', '21703', '21704'],
                              'Rockville': ['20850', '20851', '20852', '20853'],
                              'Gaithersburg': ['20877', '20878', '20879', '20882'],
                              'Bowie': ['20715', '20716', '20720', '20721']},
                  'Massachusetts': {'Boston': ['02108', '02109', '02110', '02111', '02113'],
                              'Worcester': ['01602', '01603', '01604', '01605', '01606'],
                              'Springfield': ['01103', '01104', '01105', '01107', '01108'],
                              'Lowell': ['01850', '01851', '01852', '01854'],
                              'Cambridge': ['02138', '02139', '02140', '02141', '02142']},
                  'Michigan': {'Detroit': ['48201', '48202', '48204', '48205', '48206'],
                              'Grand Rapids': ['49503', '49504', '49505', '49506', '49507'],
                              'Warren': ['48088', '48089', '48091', '48092', '48093'],
                              'Sterling Heights': ['48310', '48312', '48313', '48314'],
                              'Ann Arbor': ['48103', '48104', '48105', '48108', '48109']},
                  'Minnesota': {'Minneapolis': ['55401', '55402', '55403', '55404', '55405'],
                                'St. Paul': ['55071'],
                                'Rochester': ['55901', '55902', '55904', '55906'],
                                'Duluth': ['55802', '55803', '55804', '55805', '55806'],
                                'Bloomington': ['55796']},
                  'Mississippi': {'Jackson': ['39201', '39202', '39203', '39204', '39206'],
                                'Gulfport': ['39501', '39503', '39507'],
                                'Southaven': ['38671', '38672'],
                                'Hattiesburg': ['39401', '39402'],
                                'Biloxi': ['39530', '39531', '39532']},
                  'Missouri': {'Kansas City': ['64101', '64102', '64105', '64106', '64108'],
                                'St. Louis': ['63367'],
                                'Springfield': ['65802', '65803', '65804', '65806', '65807'],
                                'Independence': ['64050', '64052', '64053', '64054', '64055'],
                                'Columbia': ['65201', '65202', '65203', '65299']},
                  'Montana': {'Billings': ['59101', '59102', '59105', '59106'],
                              'Missoula': ['59801', '59802', '59803', '59804', '59808'],
                              'Great Falls': ['59401', '59404', '59405'],
                              'Bozeman': ['59715', '59718', '59773'],
                              'Butte': ['59701', '59750']},
                  'Nebraska': {'Omaha': ['68102', '68104', '68105', '68106', '68107'],
                              'Lincoln': ['68502', '68503', '68504', '68505', '68506'],
                              'Bellevue': ['68005', '68123', '68147'],
                              'Grand Island': ['68801', '68803'],
                              'Kearney': ['68845', '68847']},
                  'Nevada': {'Las Vegas': ['89101', '89102', '89103', '89104', '89106'],
                              'Henderson': ['89002', '89011', '89012', '89014', '89015'],
                              'Reno': ['89501', '89502', '89503', '89506', '89508'],
                              'North Las Vegas': ['89030', '89031', '89032', '89033', '89081'],
                              'Sparks': ['89431', '89434', '89436', '89437', '89441']},
                  'New Hampshire': {'Manchester': ['03101', '03102', '03103', '03104', '03109'],
                              'Nashua': ['03060', '03062', '03063', '03064'],
                              'Concord': ['03301', '03303'],
                              'Dover': ['03820'],
                              'Rochester': ['03839', '03867', '03868']},
                  'New Jersey': {'Newark': ['07102', '07103', '07104', '07105', '07106'],
                              'Jersey City': ['07302', '07304', '07305', '07306', '07307'],
                              'Paterson': ['07501', '07502', '07503', '07504', '07505'],
                              'Elizabeth': ['07201', '07202', '07208'],
                              'Edison': ['08817', '08820', '08837', '08899']},
                  'New Mexico': {'Albuquerque': ['87101', '87102', '87104', '87105', '87106'],
                              'Las Cruces': ['88001', '88005', '88007', '88011', '88012'],
                              'Rio Rancho': ['87124', '87144'],
                              'Santa Fe': ['87501', '87505', '87506', '87507', '87508'],
                              'Roswell': ['88201', '88203']},
                  'New York': {'New York City': ['10001', '10002', '10003', '10004', '10005'],
                              'Buffalo': ['14201', '14202', '14203', '14204', '14206'],
                              'Rochester': ['14604', '14605', '14606', '14607', '14608'],
                              'Yonkers': ['10701', '10703', '10704', '10705', '10710'],
                              'Syracuse': ['13202', '13203', '13204', '13205', '13206']},
                  'North Carolina': {'Charlotte': ['28202', '28203', '28204', '28205', '28206'],
                              'Raleigh': ['27601', '27603', '27604', '27605', '27606'],
                              'Greensboro': ['27395', '27401', '27403', '27405', '27406'],
                              'Durham': ['27701', '27703', '27704', '27705', '27706'],
                              'Winston-Salem': ['27101', '27103', '27104', '27105', '27106']},
                  'North Dakota': {'Fargo': ['58102', '58103', '58104'],
                              'Bismarck': ['58501', '58503', '58504', '58505'],
                              'Grand Forks': ['58201', '58202', '58203'],
                              'Minot': ['58701', '58703'],
                              'West Fargo': ['58078']},
                  'Ohio': {'Columbus': ['43085', '43201', '43202', '43203', '43204'],
                            'Cleveland': ['44102', '44103', '44104', '44105', '44106'],
                            'Cincinnati': ['45202', '45203', '45204', '45205', '45206'],
                            'Toledo': ['43601', '43604', '43605', '43606', '43607'],
                            'Akron': ['44301', '44302', '44303', '44304', '44305']},
                  'Oklahoma': {'Oklahoma City': ['73102', '73103', '73104', '73105', '73106'],
                            'Tulsa': ['74103', '74104', '74105', '74106', '74107'],
                            'Norman': ['73026', '73069', '73071', '73072'],
                            'Broken Arrow': ['74011', '74012', '74014'],
                            'Lawton': ['73501', '73505', '73507']},
                  'Oregon': {'Portland': ['97201', '97202', '97203', '97204', '97205'],
                              'Salem': ['97301', '97302', '97303', '97304', '97305'],
                              'Eugene': ['97401', '97402', '97403', '97404', '97405'],
                              'Gresham': ['97030', '97080'],
                              'Hillsboro': ['97123', '97124']},
                  'Pennsylvania': {'Philadelphia': ['19102','19103','19104','19106','19107'],
                              'Pittsburgh': ['15201', '15202', '15203', '15204', '15205'],
                              'Allentown': ['18101', '18102', '18103', '18104', '18106'],
                              'Erie': ['16501', '16502', '16503', '16504', '16505'],
                              'Reading': ['19601', '19602', '19604', '19605', '19606']},
                  'Rhode Island': {'Providence': ['02903', '02904', '02905', '02906', '02907'],
                              'Warwick': ['02886', '02888', '02889'],
                              'Cranston': ['02910', '02920', '02921'],
                              'Pawtucket': ['02860', '02861'],
                              'East Providence': ['02914']},
                  'South Carolina': {'Columbia': ['29201', '29203', '29204', '29205', '29206'],
                              'Charleston': ['29401', '29403', '29406', '29407', '29412'],
                              'North Charleston': ['29405', '29418', '29420'],
                              'Mount Pleasant': ['29464', '29466'],
                              'Rock Hill': ['29730', '29732', '29734']},
                  'South Dakota': {'Sioux Falls': ['57103', '57104', '57105', '57106', '57107'],
                              'Rapid City': ['57701', '57702', '57703'],
                              'Aberdeen': ['57401'],
                              'Brookings': ['57006'],
                              'Watertown': ['57201']},
                  'Tennessee': {'Nashville': ['37201', '37203', '37204', '37205', '37206'],
                              'Memphis': ['38103', '38104', '38105', '38106', '38107'],
                              'Knoxville': ['37902', '37909', '37912', '37914', '37915'],
                              'Chattanooga': ['37402', '37403', '37404', '37405', '37406'],
                              'Clarksville': ['37040', '37042', '37043']},
                  'Texas': {'Houston': ['77002', '77003', '77004', '77005', '77006'],
                              'San Antonio': ['78201', '78202', '78203', '78204', '78205'],
                              'Dallas': ['75201', '75202', '75203', '75204', '75205'],
                              'Austin': ['78701', '78702', '78703', '78704', '78705'],
                              'Fort Worth': ['76102', '76103', '76104', '76105', '76106']},
                  'Utah': {'Salt Lake City': ['84101', '84102', '84103', '84104', '84105'],
                              'West Valley City': ['84119', '84120', '84128'],
                              'Provo': ['84601', '84602', '84604', '84606'],
                              'West Jordan': ['84081', '84084', '84088'],
                              'Orem': ['84057', '84058', '84097']},
                  'Vermont': {'Burlington': ['05401', '05408'],
                              'South Burlington': ['05403'],
                              'Rutland': ['05701'],
                              'Barre': ['05641'],
                              'Montpelier': ['05602']},
                  'Virginia': {'Virginia Beach': ['23451', '23452', '23453', '23454', '23455'],
                              'Norfolk': ['23502', '23503', '23504', '23505', '23507'],
                              'Chesapeake': ['23320', '23321', '23322', '23323', '23324'],
                              'Richmond': ['23219', '23220', '23221', '23222', '23223'],
                              'Newport News': ['23601', '23602', '23603', '23605', '23606']},
                  'Washington': {'Seattle': ['98101', '98102', '98103', '98104', '98105'],
                              'Spokane': ['99201', '99202', '99203', '99204', '99205'],
                              'Tacoma': ['98402', '98403', '98404', '98405', '98406'],
                              'Vancouver': ['98660', '98661', '98662', '98663', '98664'],
                              'Bellevue': ['98004', '98005', '98006', '98007', '98008']},
                  'West Virginia': {'Charleston': ['25301', '25302', '25304', '25305', '25306'],
                              'Huntington': ['25701', '25702', '25703', '25704', '25705'],
                              'Morgantown': ['26501', '26505', '26506', '26508'],
                              'Parkersburg': ['26101', '26104'],
                              'Wheeling': ['26003']},
                  'Wisconsin': {'Milwaukee': ['53202', '53203', '53204', '53205', '53206'],
                              'Madison': ['53703', '53704', '53705', '53706', '53711'],
                              'Green Bay': ['54301', '54302', '54303', '54304', '54311'],
                              'Kenosha': ['53140', '53142', '53143', '53144'],
                              'Racine': ['53402', '53403', '53404', '53405', '53406']},
                  'Wyoming': {'Cheyenne': ['82001', '82007', '82009'],
                              'Casper': ['82601', '82604', '82609'],
                              'Laramie': ['82070', '82072'],
                              'Gillette': ['82716', '82718'],
                              'Rock Springs': ['82901']}
                  }
