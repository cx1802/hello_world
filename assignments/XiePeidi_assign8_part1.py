"""
Peidi Xie
April 28th, 2019
Introduction to Programming, Section 03
Part 1: Array-ders of the Lost Ark!
"""
'''
Challenge #1
'''
# the list
challenge1 = [54,40,37,64,81,15,65,72,61,57,83,3,67,12,30,54,11,51,3,78,48,31,68,77,64,68,95,68,35,82,57,26,67,41,47,80,36,88,5,9,55,87,77,8,65,31,7,79,49,22,32,94,34,12,20,30,91,12,57,77,37,96,22,29,17,76,36,56,80,33,20,65,57,40,50,97,20,92,25,14,19,84,12,62,20,42,99,52,88,29,75,48,27,73,46,72,48,84,19,55]

# find how many numbers are in the list
password1_1 = len(challenge1)
# find the sum of all numbers in the list
password1_2 = sum(challenge1)
# find the average of all numbers in the list
password1_3 = sum(challenge1) / len(challenge1)
# find the largest value in the list
password1_4 = max(challenge1)
# find the smallest value in the list
password1_5 = min(challenge1)

print("The password for challenge #1 is:", password1_1, password1_2, password1_3, password1_4, password1_5)

# the key for challenge #1 is "quartz"

print()

'''
Challenge #2
'''

# the list etched on the front of the amulet
challenge2a = [-0.6179074665219488, 0.012080423982449795, -0.21346000509541063, 0.08299652983289585, 2.44401680106775, 4.902778859313734, 1.7132831483350532, -4.2004763396051725, -4.043856195861675, -2.6728507023602326, 5.181911533071974, -2.1235877432845354, 7.603895698367564, -5.6730748575837975, -3.5868701412258464, 8.50824673494424, 1.9530312960520657, 1.4057711751329447, -6.6010520166956885, -0.8889270825881894, -3.066437913144831, -1.047977711607209, -0.6183425325427638, -1.9567474971238643, -1.6108985491087715, -3.4762343504063105, -0.7819967483948718, 1.2787199500848474, -1.724036624119682, 4.134045084705252, -4.302090407212001, 4.522452909896921, -9.510982189042458, 4.483571903648103, 4.734972592935479, 1.3007048393668028, -1.5733757395516363, -1.9343054344201707, 6.787212280236046, -0.35603892339489995, -1.3414921239899753, -0.9393551256779856, -1.9298884254368263, 6.043295105337908, 2.9330671137121733, 2.8561036619044047, -0.8293767467550212, 6.123622142714353, -2.2350961485598777, 7.20722805161423, 5.515389689089437, -2.7666432567169745, -4.344590134196103, 3.3453531590362613, 10.413288779778698, 0.3986583788822756, 1.8156402784897105, -6.495232639280744, -2.5586148068696852, 2.456750085945401, -2.0241915465317994, 2.6640207424833706, -3.221638093253812, -0.13291701098446618, 4.525894152095317, 3.833943185257407, -2.892260297173234, -3.247865929061468, 6.129696012756685, 4.451839001858698, -3.142375819178058, -1.0758596832313212, -7.85705595464708, -3.376343621066232, -3.993944532318441, 13.146850947670861, -1.3900676627648902, 3.8600378751921256, 3.9652071948870447, -2.4382860496298324, 3.0864605092488304, -10.769089293963074, 1.9773754511588617, 4.826841112732377, 7.9219782116860324, -3.266132871461332, 1.8118819669439024, 0.698579723806034, 7.119629551067371, -0.9141128559070014, 1.5143207368301361, -8.587596597534729, -0.9387144566983379, 2.5641381148921805, 10.628593146418485, 3.794317923770138, 6.2802756227726615, -0.05171930511667566, 0.8736426098894451, 0.6226851580000003]

# compute the sum of the values of numbers in all even positions in the list to get the latitude value of the location
latitude_a = sum(challenge2a[::2])
# compute the sum of the values of numbers in all odd positions in the list to get the longitude value of the location
longitude_a = sum(challenge2a[1::2])

print("The front of the amulet points", str(latitude_a)+"N", str(longitude_a)+"E")

# the list etched on the back of the amulet
# repeat the exact procedures done to the list on the front of the amulet
challenge2b = [9.631212195521316, -2.1235831279282698, 3.7468670477204773, -4.559878135521824, 3.2444286767576545, 6.2877828741148605, 6.520597627024687, 2.642307472836288, 1.2002893113069557, 0.32620641006622675, -3.368962812990781, -2.588868228199504, 4.356518441561512, -0.5955112302723241, 0.3875648501871751, -2.9311051175998064, 2.0095554763173666, -1.228769483871199, 5.900445902470515, 0.41527619439744434, 2.9752128071432145, 4.805920315662717, -4.797853823364673, 5.752192282393844, 2.9073605365834556, 2.4870719041084497, -1.7994046436584152, 7.79554996548367, 4.4174973514255536, 2.084039895979635, 0.6281302992116424, -3.1466915662704524, 3.646400672147826, 0.9609952887592054, -6.070082172976056, -0.9392599054917704, 0.904301836858967, 5.926867039519574, 3.238559698585232, -4.439332575192746, 1.352444182896236, -0.24594080100384297, -1.6395807550351367, 3.591208179788307, 4.15757174804611, -3.5334824535956173, 0.5302366137985215, 9.564674975899017, 4.175389023096817, -0.9827335882191762, 4.305890552392608, 3.059083687714633, 2.3224548745551488, 0.1934380213592375, 1.0235814, 1.1716370685853148, -2.931711339626567, -4.214035402157694, -1.0093422753964358, -4.843082160061708, -7.148710177896536, -1.910725804980465, -0.22905523068711164, 3.8200222938181367, -1.744095856344644, 1.354958988184811, 0.9933832752568843, 0.8820951391051288, -2.062035935350486, -7.633897329029599, 0.49911238393151325, -1.1684033502541722, 4.090099097765502, 4.566828839384462, 0.6901115935421007, -4.30695891725898, -5.637531096381548, 2.6920329212478507, -1.522395621132775, 6.351734133984433, 0.4895678835360122, -4.755548841958967, -2.826990702897114, 1.974618789378563, -6.999938959339396, 0.6289774718852977, 3.2732671487606266, -1.2781272997669557, 6.725303989648547, -7.163688015215646, 5.547683884070125, -3.0189942298996213, -0.2487963910538069, -0.46314538549764894, 5.3913279138183645, -4.018219623545416, 6.491084381355617, -1.5629014732514819, -6.557894883162792, -3.856421007612216]

latitude_b = sum(challenge2b[::2])
longitude_b = sum(challenge2b[1::2])

print("The back of the amulet points", str(latitude_b)+"N", str(longitude_b)+"W")

# the front of the amulet points THE GREAT PYRAMID OF GISA, and the back of the amulet points STONEHENGE

# the key for challenge #2 is "moonstone"

print()

'''
Challenge #3
'''

# the list
challenge3 = [56, 69, -2, 31, -54, -40, -82, 23, 43, -82, 51, -97, -113, -138, -16, -113, -42, -41, 18, 34, 57, -42, -47, 68, -47, -59, -88, 0, -12, 69, -22, -12, -94, -48, -18, -100, -131, 10, -84, 15, -109, -19, 61, -19, -30, 31, 8, -108, -77, -95, 79, -18, -128, -103, -66, -3, 51, -59, 78, 80, -66, 73, -144, -14, 59, -9, -2, -51, -74, -132, -94, -119, -56, -90, 30, 19, -73, 47, -14, -94, -120, -38, 56, -44, -39, 19, -66, 44, 9, 75, -4, -70, 53, 12, -35, -47, 31, -128, -41, 73, -113, -144, -95, 74, 16, 55, 43, 65, -148, 2, 52, 32, -61, 19, -72, -44, -24, 32, -27, -43, -53, 76, -124, -131, 63, -82, 23, -30, -76, 12, -85, 27, -33, -140, -39, -101, -12, -69, -150, 28, -70, -81, -8, -84, -79, -139, 27, -126, 61, 14, -101, 70, -19, 20, 26, -82, -80, 7, -129, 31, 38, -47, -28, 23, -59, -148, -58, -99, -152, -56, -90, -109, -14, -124, -94, 27, 61, 28, -58, -1, -108, -80, 24, -120, -62, -130, -60, -94, -22, 40, 58, -150, -145, 71, 47, -12, -30, 9, 75, -129, 20, -78, -61, -39, 24, -23, 18, -13, -111, -43, 40, -46, -135, 78, -51, -76, 63, 11, 15, -111, 42, -119, -76, -116, -144, -139, -95, 37, 71, -35, -75, -54, -112, 23, 63, 35, -101, -109, 68, -40, -26, -110, 34, 21, 28, -113, 1, -4, -80, -21, 68, -95, -115, -100, -67, -148, -78, -3, -41, -142, -107, -33, -23, -96, -131, 80, -47, 5, -34, -130, -76, 32, -9, 62, -85, -38, -8, 58, -43, -15, -84, 41, -3, 40, 42, 29, -125, -115, -127, 23, 30, -3, -68, 14, 30, -89, 56, -73, -142, 62, -68, -54, 26, -139, -113, -64, 27, -8, 63, 25, -105, 71, -147, 46, 42, 73, -119, 41, -79, -145, -149, 77, 30, -46, 25, -21, -22, -67, 79, 24, -141, 24, -131, -111, 25, 23, -72, 61, 34, -52, -115, 77, -42, 46, -131, -45, -56, -114, -84, -114, -137, -62, 42, -145, 2, 61, -10, 5, -66, -102, -41, 38, -144, -106, -128, -69, 35, -73, -122, 34, 32, -83, -85, 46, -67, -139, 35, -33, 10, -74, -13, -143, 58, 67, 6, -13, -16, -76, -145, 59, -32, -71, -149, 50, -140, -4, 19, -102, -145, -33, -131, 6, -132, -15, -54, -72, 61, -7, 22, 7, -71, -133, 64, -124, -142, -87, -79, -47, -62, -54, -72, -18, -110, -81, -146, -48, -124, 22, -77, 53, -126, 26, -74, -78, -95, 50, 8, -151, 32, 12, -27, -26, -53, -108, -54, 11, 59, 79, 20, 43, -37, -109, -29, 78, 27, -121, -128, 66, 73, -8, -32, -111, -55, -119, 20, -21, -10, -80, -64, -131, -89, 5, 51, 30, 36, -69, -62, -119, 54, -132, -134, -142, -129, 60, -150, -104, -39, -128, -3, -33, -149, -137, 43, 2, -67, -85, -52, -11, -133, -59, -81, 74, -49, -50, 44, 42, 30, -104, -31, -22, -66, -2, -2, -89, -12, -33, 0, -141, -116, 0, 27, -87, -9, -77, -29, -150, -121, 9, -38, -51, -104, 48, -50, 18, 0, -147, -55, -10, 56, -26, -70, 32, -148, 16, -86, 17, -92, -138, -149, -67, -72, -8, -32, 17, -25, 53, -17, -27, -36, -89, 69, -15, -45, 42, 32, -127, -93, -50, -90, -20, -131, 37, 63, -10, -88, -33, -150, -148, -120, -3, 45, -27, 0, 10, -103, -67, 25, -11, -138, -141, -151, -134, -151, -126, 29, -75, -21, -18, -35, 23, 34, 80, -137, 57, 20, -123, -119, 15, 39, 12, -88, -70, 49, -94, -80, -112, -119, 1, -69, -126, 14, 62, -65, -60, -39, 38, -56, 57, -41, 29, 35, -48, -53, -15, 52, -135, 73, -25, -106, -94, 38, -103, -126, 2, 19, -35, -148, 48, -39, -106, 38, -55, 19, -58, -127, 76, -16, 21, 62, -21, -45, -119, -109, 78, -127, -109, 39, -87, 45, -136, 51, -131, -30, 52, -111, 73, -70, 51, -143, -72, -48, -128, -30, 24, 46, -101, -50, -16, 40, 57, -33, -151, -40, 26, 71, 5, -117, 49, -27, -10, -51, -118, 72, -41, -31, -67, 79, -69, -81, -147, -37, -54, 4, 16, -44, 24, 0, -64, -53, 25, -82, -96, -17, -147, 14, -20, 15, 22, -100, -104, -67, -140, -38, 49, -59, -89, -89, -97, -90, 15, 6, -43, 78, 43, 65, -32, -97, 31, -117, -96, -63, 53, -123, 55, -34, -111, 57, 2, -29, 12, 1, 47, 74, -34, 14, 9, -85, 1, -98, 37, -76, -143, -145, -16, -56, -93, -150, -94, -82, -20, -16, 51, -33, -61, -112, 0, 15, 22, 72, -148, -64, 58, 77, -83, -101, 80, -112, -52, -118, -152, -108, -86, 27, 69, -1, 54, -143, -51, 49, -59, -49, -136, -35, -14, 31, -65, -140, 11, 79, 63, 66, -80, 61, -59, 12, 63, -89, -104, 76, -66, -45, -143, 50, -134, -52, -26, -140, -32, 50, 21, -137, 43, -29, -8, -134, 34, -121, -81, -78, -13, 78, -100, -144, -133, -65, -144, -70, -81, 67, -105, -94, 33, -54, -94, 30, -49, -33, -52, 28, -148, -110, 46, -56, 18, -36, -90, 5, -135, 31, -129, 70, -35, -136, -111, -132, -117, 34, 33, 20, 23, -73, -50, -82, 1, 75, -28, -78, -79, -144, -139, -74, -67, -60, 8, 55, 16, -14, -52, 2, -41, 71, -68, -130, 2, -71, -85, -125, -107, -35, -64, -24, -129, 15, 80, -136, -31, -135, -129, -130, -50, -28, -90, -36, -107, -119, 7, 33, -71, 45, 20, -37, -124, 16, 67, -152, -118, 76, -111, -90, 8, 26, -143, -139, 23, -15, -129, 42, 26, -104, -5, -19, 9, 66, -132, 34, -73, -13, -104, -111, 12, 42, -109, 78, -146, -112, 12, -88, 37, 20, -138, 58, -148, 34, 9, -99, 75, -135, 43, -119, -139, -114, 5, 50, 18, 32, 38, -86, -17, -138, -83, -44, -65, 0, -43, 70, -112, 34, -23, -70, -23, 31, -61, 80, 51, 72, -92, 71, -48, -23, -111, 77, -147, -139, -80, 58, 37, 1, -78, -33, 4, 35, -6, -57, -18, -116, -4, 71, 39, -115, 13, -105, 28, 24, 41, 25, 53, -104, -102, -5, -141, -37, -103, -86, -105, -13, -143, 11, 61, 34, -15, 37, -13, -119, 16, -100, -12, -44, 66, -54, -128, 21, -95, -79, -123, -147, -56, -29, -35, 31, -38, 58, 58, -16, 0, -28, -88, -11, 68, -147, -128, -128, -23, 36, -135, 24, -54, -149, -38, 4, 75, 62, 43, -117, 47, 64, -40, -86, 75, 53, -116, -101, -32, 19, 5, -132, -21, 29, -42, 32, -130, -106, -124, -90, -118, -120, -77, -80, -15, -53, 62, 51, -139, 25, -8, -45, 57, -38, -114, -74, 49, -147, -7, -36, -16, 6, -124, -42, -61, 34, -79, 28, -105, -99, -95, -103, -12, -40, -131, -97, -132, -25, -56, -66, 36, 34, -128, 53, 0, -62, -49, -117, 46, -52, 4, -27, -50, -55, 50, -92, -111, -24, -30, -72, -34, -122, -56, 28, -148, 37, 57, 48, -152, -131, 14, -111, -137, -35, 0, 5, 52, 63, -94, -116, -78, 11, 70, 57, -128, -26, -45, -120, -134, 41, -91, 78, 69, -24, -24, -7, -109, 60, -23, 14, -133, 35, -36, 24, 78, -89, -134, -92, -24, -25, -112, 35, 12, 14, -120, 19, 79, -12, 3, -72, -129, -87, -22, 3, -16, -15, -103, -52, -10, -132, 64, -123, -41, -128, -91, -149, -52, -152, 32, -6, 63, -84, 5, -69, -108, 79, -84, -152, -97, -64, -149, -91, -128, -32, -152, 40, -110, 63, -59, -78, 47, -98, 70, -143, 9, -149, -33, -29, -19, 58, -135, 78, 37, -22, -13, 69, -11, -73, -28, 61, -89, -53, -16, -86, -142, -10, 15, 1, -105, -118, 10, -32, -132, -146, 57, -123, 38, -77, -115, -142, 26, -17, 6, 4, -133, -146, 45, 56, -1, 11, 57, 2, 8, 48, -141, 67, -41, 24, -23, 1, 55, -70, -8, -83, 55, -38, 50, -135, 75, 75, -102, -101, 10, -77, 1, -92, -42, 64, -50, -101, -82, -72, -33, -70, -74, -61, 76, -92, -85, -93, -31, -69, 14, -150, -103, -118, -77, 9, -17, -101, -142, 27, 11, -14, 17, 10, -55, 78, -16, -38, 3, -39, -31, -114, 64, -96, -7, -10, -62, -66, 15, -2, -34, -71, -152, -143, 60, -103, -102, 34, -69, -72, -3, -99, 35, 45, -30, -68, -139, -60, -108, 2, -1, 38, -114, -63, 37, -114, -118, -31, -36, -65, -16, -108, -100, -16, 45, -111, 1, 66, 23, -84, -55, 28, -84, 31, -79, -83, 63, -127, 69, -104, 23, -126, 76, -98, -107, -61, 37, -90, -31, -74, 40, -44, 32, -19, -57, 47, -90, -21, -95, -144, -88, -37, -67, 13, 71, -108, -87, -11, -132, -102, -22, -37, -105, -54, 32, -110, -131, 52, 7, 70, -46, -33, -48, -86, -136, 35, -90, -9, -11, -14, 63, -4, -76, -77, 72, 36, 13, -113, 67, 31, 40, 80, -33, -137, 69, -18, 65, -76, -25, -98, 9, -131, -125, -148, -26, -26, 78, -49, -110, 66, -111, -148, -89, 15, 77, -85, -119, -147, 10, -75, 54, -43, -92, -7, 64, -128, -108, 5, -41, -3, -60, -116, -94, -40, 13, 57, -103, 52, -111, -145, 0, 44, -109, -82, -88, 35, -60, 22, -90, 2, -63, -73, -42, -76, 2, -113, -151, -133, -53, 66, -53, 0, 37, -25, 34, -24, -80, -143, -38, 73, 44, 31, -30, 28, 49, -107, 15, 46, -12, -52, -2, 25, 77, -79, -36, 54, -9, 75, 39, 51, -101, 52, 17, -138, 17, -6, 70, -80, 74, -104, 3, 60, -32, -26, -62, -57, 53, -10, 24, -44, -12, -118, -87, -4, -101, -36, -125, -44, -72, -112, -53, -107, -91, 39, -39, -39, -30, -76, 53, -15, -141, -70, 38, 38, -144, 65, -77, -2, -152, 12, 36, -83, 0, 47, 62, 15, -96, -113, -148, -51, -68, -31, -115, -105, -8, -12, -51, -28, 74, 62, 69, -44, 36, -127, -14, 8, 37, 48, 41, 53, 77, -95, -6, 22, 39, 48, -89, 1, 52, 31, 43, 10, -72, -42, -97, -53, -89, -26, 8, -125, -58, 55, -12, 74, -94, -5, -89, -29, -80, -115, -141, -21, 17, -112, 3, 50, 38, -69, -23, -5, -133, -52, 39, -47, -98, -38, -20, 56, 57, 8, 14, 76, -116, -136, -35, -134, -103, -18, -141, 9, 33, -21, -113, 58, 9, -36, 14, -21, -143, -115, -99, 67, 0, -51, 23, -120, -5, -10, 38, -27, 56, -87, -20, -28, -92, -150, 64, 55, 11, -51, -15, -26, -69, 49, -112, 69, -27, -68, 13, 78, 51, 16, -144, 45, -102, -80, -125, 15, -58, -92, 25, 41, 2, -46, -69, 47, -68, -4, -59, -133, -35, -144, 36, -93, -127, -59, 25, 43, -147, -60, 53, -94, -89, -60, -92, -3, -58, 60, -29, -118, -20, -73, 42, 8, -124, -96, -152, -139, 61, -132, -18, -2, 76, -69, 64, 77, 19, 10, -19, -82, -109, -75, -134, -78, -23, 59, -105, 76, -68, 44, -63, -128, -62, -31, 74, -9, -34, 28, -107, 29, -7, 53, -65, 37, -101, -26, 26, -104, -103, -43, -14, -46, 12, 43, -61, -101, -43, -117, -151, -38, -52, -127, 33, -151, 32, 38, 4, -132, -64, 31, -3, -147, -129, -86, -64, -83, -75, -109, -90, -76, 32, 21, 61, 36, -10, -5, -150, -48, -38, -112, -9, -19, -119, -143, 24, -101, 69, -55, -75, -101, 62, -82, -26, -107, 43, 65, -41, 13, -140, 57, -79, -24, -85, -66, -1, -23, -127, 31, -77, -2, -57, -55, -140, -36, -56, -45, -21, -19, -113, 16, 38, 0, -47, -5, -80, -58, -68, 15, 16, -79, -12, -138, 29, -152, -27, 0, -126, -141, 38, -59, -87, -29, -128, -92, 72, 19, -149, -137, -45, -135, -151, 12, -84, 4, -104, -16, -18, -146, 5, 62, -34, 68, 19, 50, 31, -132, -114, -69, -75, -4, -125, -64, 78, -134, -4, 17, -76, -23, -83, -123, -12, 64, 0, -50, -86, 0, -64, 69, -59, -36, 71, -16, 63, -95, -122, -6, -84, -128, -19, 40, 6, -8, 38, -18, -16, 67, -31, -27, -34, 40, -119, -67, -110, 21, -25, 64, -147, 5, -65, -99, 24, -70, -40, -119, -54, -129, 67, -89, 44, -128, -108, -37, 52, -22, -137, -126, -77, -121, -77, -77, -36, -121, -106, -121, 52, -142, -98, -108, -150, -56, -66, -16, -85, -22, 32, -78, 3, -67, 2, -110, 0, -149, 76, -28, -115, 33, -37, -150, 69, 68, -47, -115, -48, -132, -76, 42, -34, -151, -32, -23, 42, -85, -139, -134, -95, -144, -112, -100, 15, 35, -103, -111, 52, -151, -112, 38, 21, -106, -5, -152, -81, -121, -102, -80, -58, 62, -75, -23, 66, -50, 33, -100, -90, 54, 11, -116, 22, -42, -84, 27, -62, -78, -91, 45, -116, -132, -91, -128, -28, -103, -27, 1, -115, -74, -119, -101, -72, -80, 59, 78, -84, -148, 19, -123, -20, -18, -57, -71, -90, -62, -114, -89, 50, -60, 45, -140, -54, 78, -91, -39, -144, -130, 19, 15, -70, 26, -29, 35, -51, -42, 53, -8, -76, 36, -134, 66, -138, -59, -3, -93, -73, -57, -77, -73, 4, 36, -107, 17, 64, -90, -105, -135, -9, -39, -72, 12, -123, -126, -95, 60, -29, -39, 1, -130, -124, 72, 37, -50, 79, -94, -149, 28, -20, 42, -91, -148, 11, -14, 37, 61, -20, 6, 51, 67, 55, -125, -41, 24, 19, 20, 40, -126, 69, 53, 68, 62, 78, 18, -28, -139, -23, -95, -78, -18, 41, -46, -127, -117, 10, -99, 45, -140, -66, 30, 37, -76, -41, 55, 60, 21, -78, -127, 19, 6, -35, -42, 14, -71, 0, 10, -142, 8, -95, -67, 33, 34, 30, -19, -19, -151, 41, -123, 1, -36, -70, 37, -17, -138, 58, -127, 79, -12, 77, -47, 73, 49, 11, -51, -55, -24, 3, -88, -91, 28, -49, -66, 4, -135, -15, -78, -126, -109, -9, -79, 0, -75, -30, 31, -103, -89, 43, -150, 26, 63, -112, 7, 39, -63, -73, -2, -46, -149, -135, -53, -80, -8, -103, 63, 64, 11, 52, -105, -59, 14, -144, -56, -57, -63, -109, 51, -148, -78, -30, -23, -57, 45, -87, -9, 78, -111, -105, -93, 55, -98, -75, 6, 60, 65, -60, -148, -75, -118, -152, 63, 73, -45, 68, 39, 73, -31, -37, -151, -26, 77, -41, -59, 46, -128, -39, -72, 44, -51, -127, -26, -53, -14, -39, -72, 80, 7, 64, -17, 15, 24, -33, -55, -112, 17, 9, -104, -41, -109, -97, 21, 37, 65, -46, -99, 14, -58, 54, 69, -149, 38, -115, 74, -14, -28, -20, -149, -16, -118, -52, -60, -30, 22, 51, -121, -66, -111, -149, -112, 77, -110, 51, -58, 50, -65, -4, -100, -49, -149, 40, -54, -109, 78, -92, -26, -96, 74, -83, -82, 55, -103, -150, -93, -25, -56, -40, -4, -73, 58, -113, -94, -19, 10, 45, -61, -43, -145, -135, 49, 10, -8, -29, 39, -114, -71, 52, -68, -94, 70, 75, 38, 17, 76, -70, -77, 78, -13, 44, -71, 77, 50, -75, -130, 0, -6, -125, 44, -128, -77, -54, 65, -143, -57, 66, 16, -110, -138, -141, -36, -39, -16, 3, -48, -130, -24, -143, 38, 19, -54, -127, 2, -91, -35, -100, 67, -11, -140, 69, -40, -90, 35, 43, 33, 38, -50, 40, 55, -44, -85, 0, -145, -146, -118, -10, 29, -136, -128, -122, 54, 53, -89, 27, -107, -68, -17, -149, -79, -19, -134, 74, 18, 58, 48, -97, 61, -81, -101, -117, -108, -147, 13, 64, -56, -6, -21, 52, 57, 64, -101, 75, 21, -35, -152, 1, -68, -119, -67, -51, 76, -15, 46, -46, -134, -106, 1, 7, -7, -120, -18, 5, 30, 20, -88, -103, -143, -53, -148, -74, -68, -33, -50, -79, -129, 8, -54, -114, -113, 40, 78, -108, -112, 57, 42, 49, 8, -23, -78, -117, -120, 65, 17, 33, -24, 0, -107, 73, -132, 62, 56, 23, -58, 43, -132, -19, 25, 38, -150, 18, -87, 62, -137, -17, -145, -22, -67, 2, -89, 45, -63, -53, 46, -101, 0, 4, 21, -26, -103, -138, -15, -111, 63, -87, -39, -150, -75, -46, -20, -128, 57, -18, -82, -58, -13, -60, -79, -91, -56, -74, -108, 60, -41, -75, 41, -17, 10, -17, 73, 9, -129, -95, 26, -80, -13, -136, 74, -83, -34, 25, -35, -72, -133, 4, -72, -112, -137, -140, -66, -46, 0, 8, 42, -81, -86, -111, -15, -143, -63, -33, -85, -146, -54, 68, -3, -113, 37, -100, -112, -29, 6, -40, -125, 74, 59, 80, 37, 13, 47, 77, -78, 0, 12, -57, -99, -85, 14, -49, -126, 23, -25, -145, 14, -74, -28, -91, 38, -73, 41, 69, -24, 14, -41, -132, -114, -77, 31, 78, -41, -145, 47, -87, -24, -139, 18, 41, 57, -134, -67, 22, -120, 52, 4, -61, 46, 55, 39, -98, -9, -74, -64, 79, -103, 59, -122, -120, -38, -112, -111, -83, 23, 49, -70, -23, -64, -68, -116, -148, 76, -69, -107, -141, 3, 20, -36, 52, 40, -96, -94, -71, -67, -137, -129, -86, 3, -72, 36, -131, -110, -36, 33, 21, -87, -132, -118, -126, -139, 50, 22, -147, -13, 79, -41, -137, 16, -97, 45, -53, -43, -91, -138, -78, -148, -21, -103, 53, 35, 32, -108, -65, 72, -29, -127, -14, 8, -58, 68, -78, 66, 42, 55, -51, -48, -136, 78, -147, -59, -37, 20, -43, 19, -42, 41, -135, 72, 67, -61, -123, -125, -107, -89, 15, 46, -151, -144, 75, 7, -85, 78, -96, 72, -144, -127, -107, 12, -129, -45, -22, -130, 23, 23, -141, -59, -13, 6, -143, -126, -9, 74, -139, -101, -29, -53, 20, -144, 15, 65, 5, -76, -114, 63, -27, -69, -5	]

# find the largest value in the list
largest = max(challenge3)
# find the number of times the largest value appears in the list, if it repeats
largest_repeats = challenge3.count(max(challenge3))
# find the second largest value in the list
second_largest = challenge3[0]
for i in challenge3:
    if i != max(challenge3):
        if i > second_largest:
            second_largest = i
# find the number of times the second largest value appears in the list, if it repeats
second_repeats = challenge3.count(second_largest)
# find the location of the first occurence of the largest value in the list
largest_location = challenge3.index(max(challenge3))
# find the location of the last occurence of the second largest value in the list
challenge3.reverse()
second_location = len(challenge3) - challenge3.index(second_largest) - 1

print("The password for challenge #3 is:", largest, largest_repeats, second_largest, second_repeats, largest_location, second_location)

# the key for challenge #3 is "ruby"

print()

'''
Challenge #4
'''

# the list and the string
challenge4 = [323, 331, 323, 336, 319, 330, 322]
string = "treasurelieswithinthischest"

# find the sum of the values of all letters in the string
# the value of each letter is determined as a=0, b=1, c=2, etc.
sum_letters = 0
for i in string:
    sum_letters += ord(i) - 97

# subtract the sum from each value in the list
# the final password is comprised of concatenating characters of corresponding values in the list
# the value of each character follows the rule of a=0, b=1, c=2, etc.
final_password = ""
for j in challenge4:
    j -= sum_letters
    final_password += chr(j+97)

print("The final password is:", final_password)