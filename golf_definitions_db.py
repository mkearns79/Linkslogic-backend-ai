
"""Official golf definitions database for the LinksLogic Golf Rules Assistant."""

GOLF_DEFINITIONS_DATABASE = [
    {
        "id": "ABNORMAL_COURSE_CONDITION",
        "term": "Abnormal Course Condition", 
        "definition": "Any of these four defined conditions: Animal Hole, Ground Under Repair, Immovable Obstruction, or Temporary Water.",
        "keywords": ["abnormal course condition", "animal hole", "ground under repair", "immovable obstruction", "temporary water"],
        "examples": [
            "sprinkler head interference",
            "cart path obstruction", 
            "ground under repair area",
            "puddles from rain",
            "gopher holes",
            "maintenance area"
        ],
        "related_rules": ["16.1", "16.2", "25"],
        "category": "relief"
    },
    
    {
        "id": "ADVICE",
        "term": "Advice",
        "definition": "Any verbal comment or action (such as showing what club was just used to make a stroke) that is intended to influence a player in choosing a club, making a stroke, or deciding how to play during a hole or round. But advice does not include public information, such as the location of things on the course, distances, or the Rules.",
        "keywords": ["advice", "club selection", "influence player", "verbal comment", "public information"],
        "examples": [
            "what club should I use",
            "showing club after shot",
            "how to play this shot",
            "aim over there", 
            "distances are public info",
            "location of hazards is public"
        ],
        "related_rules": ["10.2"],
        "category": "conduct"
    },
    
    {
        "id": "AREAS_OF_COURSE", 
        "term": "Areas of the Course",
        "definition": "The five defined areas that make up the course: the general area, the teeing area the player must play from in starting the hole, all penalty areas, all bunkers, and the putting green of the hole the player is playing.",
        "keywords": ["areas of course", "five areas", "general area", "teeing area", "penalty area", "bunker", "putting green"],
        "examples": [
            "ball in general area", 
            "ball on teeing area",
            "ball in penalty area", 
            "ball in bunker",
            "ball on putting green"
        ],
        "related_rules": ["1.1", "2.2"],
        "category": "course_areas"
    },
    
    {
        "id": "BALL_MARKER",
        "term": "Ball-Marker", 
        "definition": "An artificial object when used to mark the spot of a ball to be lifted, such as a tee, a coin, an object made to be a ball-marker or another small piece of equipment.",
        "keywords": ["ball marker", "mark ball", "coin", "tee", "artificial object", "small equipment"],
        "examples": [
            "coin behind ball",
            "tee marking ball position", 
            "ball marker behind ball",
            "small object marking spot"
        ],
        "related_rules": ["14.1", "13.1"],
        "category": "equipment"
    },
    
    {
        "id": "BOUNDARY_OBJECT",
        "term": "Boundary Object",
        "definition": "Artificial objects defining or showing out of bounds, such as walls, fences, stakes and railings, from which free relief is not allowed. Boundary objects are treated as immovable even if they are movable.",
        "keywords": ["boundary object", "out of bounds", "fence", "wall", "stakes", "railings", "no relief"],
        "examples": [
            "boundary fence", 
            "out of bounds stakes",
            "property wall",
            "boundary railings"
        ],
        "related_rules": ["8.1", "18.2"],
        "category": "boundaries"
    },
    
    {
        "id": "BUNKER",
        "term": "Bunker",
        "definition": "A specially prepared area of sand, which is often a hollow from which turf or soil was removed. These are not part of a bunker: a lip, wall or face at the edge consisting of soil, grass, stacked turf or artificial materials; soil or growing objects inside the edge; sand spilled outside the edge.",
        "keywords": ["bunker", "sand", "prepared area", "hollow", "sand trap", "lip not included", "edge"],
        "examples": [
            "sand bunker around green",
            "fairway bunker", 
            "greenside sand trap",
            "waste area is not bunker",
            "lip is not bunker"
        ],
        "related_rules": ["12", "16.1c"],
        "category": "course_areas"
    },
    
    {
        "id": "CADDIE",
        "term": "Caddie",
        "definition": "Someone who helps a player during a round, including carrying clubs, giving advice, or other assistance allowed by the Rules. A caddie is the only person (other than a partner) a player may ask for advice.",
        "keywords": ["caddie", "carry clubs", "give advice", "help player", "assistance"],
        "examples": [
            "person carrying bag",
            "giving yardages",
            "reading putts", 
            "cleaning clubs",
            "giving advice on club selection"
        ],
        "related_rules": ["10.3", "23.5"],
        "category": "player_assistance"
    },
    
    {
        "id": "CLUB_LENGTH",
        "term": "Club-Length", 
        "definition": "The length of the longest club of the 14 (or fewer) clubs the player has during the round (as allowed by Rule 4.1b(1)), other than a putter. Used in defining relief areas.",
        "keywords": ["club length", "longest club", "14 clubs", "relief area", "measuring", "not putter"],
        "examples": [
            "43-inch driver = club-length",
            "drop within two club-lengths", 
            "relief area measurement",
            "one club-length from point"
        ],
        "related_rules": ["14.3", "16.1", "17.1"],
        "category": "measurements"
    },
    
    {
        "id": "COMMITTEE",
        "term": "Committee",
        "definition": "The person or group in charge of the competition or the course.",
        "keywords": ["committee", "in charge", "competition", "course management", "tournament director"],
        "examples": [
            "tournament committee",
            "course superintendent", 
            "competition director",
            "rules official",
            "local rules authority"
        ],
        "related_rules": ["1.2", "2.1"],
        "category": "administration"
    },
    
    {
        "id": "CONDITIONS_AFFECTING_STROKE",
        "term": "Conditions Affecting the Stroke",
        "definition": "The lie of the player's ball at rest, the area of intended stance, the area of intended swing, the line of play and the relief area where the player will drop or place a ball.",
        "keywords": ["conditions affecting stroke", "lie", "stance", "swing", "line of play", "relief area"],
        "examples": [
            "ball lie in rough",
            "stance on cart path",
            "swing blocked by tree", 
            "intended line to hole",
            "drop zone area"
        ],
        "related_rules": ["8.1", "16.1"],
        "category": "playing_conditions"
    },
    
    {
        "id": "COURSE",
        "term": "Course", 
        "definition": "The entire area of play within the edge of any boundaries set by the Committee. All areas inside the boundary edge are in bounds and part of the course. The boundary edge extends both up above the ground and down below the ground.",
        "keywords": ["course", "area of play", "boundaries", "in bounds", "committee defined", "above and below ground"],
        "examples": [
            "everything inside white stakes",
            "from tee to green", 
            "all playable areas",
            "within boundary markers"
        ],
        "related_rules": ["2.1", "18.2"],
        "category": "course_definition"
    },
    
    {
        "id": "DROP",
        "term": "Drop",
        "definition": "To hold the ball and let go of it so that it falls through the air, with the intent for the ball to be in play. The player must let go of the ball from knee height so that the ball falls straight down, without throwing, spinning or rolling it or using any other motion that might affect where the ball will come to rest. The ball must not touch any part of the player's body or equipment before it hits the ground. If the player lets go of a ball without intending it to be in play, the ball has not been dropped.",
        "keywords": ["drop", "knee height", "straight down", "no throwing", "no spinning", "ball in play", "not touch body equipment", "intent for play"],
        "examples": [
            "drop from knee height",
            "let ball fall naturally",
            "relief procedure", 
            "don't throw the ball",
            "drop in relief area",
            "ball can't touch your leg when dropping",
            "must intend ball to be in play"
        ],
        "related_rules": ["14.3", "16.1", "17.1"],
        "category": "procedures"
    },
    
    {
        "id": "EMBEDDED",
        "term": "Embedded",
        "definition": "When a player's ball is in its own pitch-mark made as a result of the player's previous stroke and where part of the ball is below the level of the ground. A ball does not necessarily have to touch soil to be embedded.",
        "keywords": ["embedded", "pitch mark", "below ground level", "own stroke", "plugged ball"],
        "examples": [
            "ball plugged in fairway",
            "pitch mark from approach shot",
            "ball below ground surface",
            "embedded in soft conditions"
        ],
        "related_rules": ["16.3", "25.2"],
        "category": "ball_conditions"
    },
    
    {
        "id": "EQUIPMENT",
        "term": "Equipment",
        "definition": "Anything used, worn, held or carried by the player or the player's caddie. Objects used for course care (like rakes) are equipment only while being held or carried.",
        "keywords": ["equipment", "used worn held carried", "player caddie", "clubs", "bag", "rangefinder"],
        "examples": [
            "golf clubs and bag", 
            "rangefinder",
            "golf cart",
            "rain gear",
            "rake when carrying it"
        ],
        "related_rules": ["4", "11.1", "23.5"],
        "category": "equipment"
    },
    
    {
        "id": "FLAGSTICK",
        "term": "Flagstick", 
        "definition": "A movable pole provided by the Committee that is placed in the hole to show players where the hole is. The flagstick includes the flag and any other material or objects attached to the pole.",
        "keywords": ["flagstick", "flagpin", "pin", "movable pole", "hole location", "flag attached"],
        "examples": [
            "pin in the hole",
            "flagstick with flag", 
            "hole marker",
            "pin placement"
        ],
        "related_rules": ["13.2", "17.3"],
        "category": "course_features"
    },
    
    {
        "id": "GENERAL_AREA",
        "term": "General Area", 
        "definition": "The area of the course that covers all of the course except for the other four defined areas: (1) the teeing area the player must play from, (2) all penalty areas, (3) all bunkers, and (4) the putting green of the hole being played. Includes all other teeing areas and wrong greens.",
        "keywords": ["general area", "through the green", "fairway", "rough", "everywhere else", "not tee penalty bunker green"],
        "examples": [
            "fairway lies",
            "rough around fairway",
            "between tee and green", 
            "other tees on course",
            "practice greens",
            "wrong greens"
        ],
        "related_rules": ["13", "16.1", "25"],
        "category": "course_areas"
    },
    
    {
        "id": "GROUND_UNDER_REPAIR",
        "term": "Ground Under Repair",
        "definition": "Any part of the course the Committee defines to be ground under repair (whether by marking it or otherwise). Includes Committee/maintenance holes, grass cuttings piled for removal, and animal habitats near player's ball. When defined by stakes, the edge is the line between the outside points of the stakes at ground level, and the stakes are inside the ground under repair. When defined by painted lines, the edge is the outside edge of the line, and the line itself is in the ground under repair. Players get free relief from ground under repair.",
        "keywords": ["ground under repair", "GUR", "committee defined", "marked area", "maintenance", "cuttings", "no play", "outside edge of line", "line in GUR", "free relief"],
        "examples": [
            "marked GUR areas",
            "grass clippings piled up",
            "maintenance holes", 
            "newly seeded areas",
            "construction zones",
            "ball touching blue line is in GUR",
            "line itself is in ground under repair"
        ],
        "related_rules": ["16.1", "25.1"],
        "category": "course_conditions"
    },
    
    {
        "id": "HOLE",
        "term": "Hole",
        "definition": "The finishing point on the putting green for the hole being played. Must be 4¼ inches (108 mm) in diameter and at least 4 inches (101.6 mm) deep. The word 'hole' also refers to the entire playing area from tee to green.",
        "keywords": ["hole", "cup", "4.25 inches diameter", "4 inches deep", "putting green", "target"],
        "examples": [
            "cup on green",
            "hole in ground", 
            "target for putting",
            "4.25 inch diameter",
            "each of 18 holes"
        ],
        "related_rules": ["2.2", "13.2"],
        "category": "course_features"
    },
    
    {
        "id": "HOLED",
        "term": "Holed",
        "definition": "When a ball is at rest in the hole after a stroke and the entire ball is below the surface of the putting green. For a ball resting against the flagstick, it's holed if any part is below the surface.",
        "keywords": ["holed", "ball in hole", "below surface", "at rest", "stroke", "entire ball", "flagstick exception"],
        "examples": [
            "ball completely in cup",
            "successful putt",
            "ball below green surface",
            "hole completed"
        ],
        "related_rules": ["13.2c", "3.3"],
        "category": "scoring"
    },
    
    {
        "id": "IMMOVABLE_OBSTRUCTION",
        "term": "Immovable Obstruction",
        "definition": "Any obstruction that cannot be moved without unreasonable effort or without damaging the obstruction or the course, and otherwise does not meet the definition of a movable obstruction. Committee may define any obstruction as immovable.",
        "keywords": ["immovable obstruction", "cannot move", "unreasonable effort", "damage", "cart path", "sprinkler", "building"],
        "examples": [
            "cart paths",
            "sprinkler heads", 
            "buildings",
            "permanent bridges",
            "fixed benches"
        ],
        "related_rules": ["16.1", "24.2"],
        "category": "obstructions"
    },
    
    {
        "id": "IN_PLAY",
        "term": "In Play",
        "definition": "The status of a player's ball when it lies on the course and is being used in the play of a hole. Ball becomes in play when first struck from teeing area and remains so until holed, lifted, lost, out of bounds, or substituted.",
        "keywords": ["in play", "ball status", "on course", "playing hole", "first stroke", "until holed", "lifted lost OB"],
        "examples": [
            "ball after tee shot",
            "ball being played",
            "active ball in round",
            "ball until holed out"
        ],
        "related_rules": ["6.3", "18.1"],
        "category": "ball_status"
    },
    
    {
        "id": "KNOWN_VIRTUALLY_CERTAIN",
        "term": "Known or Virtually Certain", 
        "definition": "The standard for deciding what happened to a player's ball. Means more than just possible or probable - either conclusive evidence or at least 95% likely based on all reasonably available information.",
        "keywords": ["known virtually certain", "95 percent likely", "conclusive evidence", "standard", "more than probable"],
        "examples": [
            "saw ball go in water",
            "ball must be in hazard",
            "95% sure what happened",
            "witness saw ball hit tree"
        ],
        "related_rules": ["17.1", "18.2"],
        "category": "standards"
    },
    
    {
        "id": "LIE",
        "term": "Lie",
        "definition": "The spot on which a ball is at rest and any growing or attached natural object, immovable obstruction, integral object, or boundary object touching the ball or right next to it. Loose impediments and movable obstructions are not part of the lie.",
        "keywords": ["lie", "ball spot", "growing objects", "attached natural", "immovable obstruction", "touching ball", "not loose impediments"],
        "examples": [
            "ball position in rough",
            "ball against tree root", 
            "ball next to sprinkler head",
            "ball touching boundary fence"
        ],
        "related_rules": ["8.1", "14.2"],
        "category": "ball_position"
    },
    
    {
        "id": "LINE_OF_PLAY",
        "term": "Line of Play",
        "definition": "The line where the player intends his or her ball to go after a stroke, including the area on that line that is a reasonable distance up above the ground and on either side of that line. Not necessarily a straight line.",
        "keywords": ["line of play", "intended direction", "above ground", "either side", "not straight", "target line"],
        "examples": [
            "intended ball path",
            "curved line to target",
            "direction to hole", 
            "planned ball flight",
            "line through trees"
        ],
        "related_rules": ["8.1", "16.1"],
        "category": "playing_line"
    },
    
    {
        "id": "LOOSE_IMPEDIMENT",
        "term": "Loose Impediment",
        "definition": "Any unattached natural object such as stones, loose grass, leaves, branches, sticks, dead animals, worms, insects and similar animals that can be removed easily, and clumps of compacted soil. Not loose if attached, growing, or solidly embedded. Special cases: Sand and loose soil are NOT loose impediments. Dew, frost and water are NOT loose impediments. Snow and natural ice (other than frost) are either loose impediments OR temporary water, at the player's option. Spider webs ARE loose impediments even though attached to another object.",
        "keywords": ["loose impediment", "unattached natural", "stones", "leaves", "branches", "dead animals", "worms", "insects", "not attached growing embedded", "sand not loose", "dew not loose", "snow player option"],
        "examples": [
            "loose leaves on ground",
            "small stones", 
            "dead insects",
            "grass clippings",
            "loose twigs",
            "worm casts",
            "sand is NOT a loose impediment",
            "dew on ball is NOT loose impediment",
            "snow can be treated as loose impediment or casual water"
        ],
        "related_rules": ["15.1", "23.1"],
        "category": "natural_objects"
    },
    
    {
        "id": "LOST",
        "term": "Lost",
        "definition": "The status of a ball that is not found in three minutes after the player or caddie (or partner/partner's caddie) begins to search for it. Time interruptions don't count toward the three-minute limit.",
        "keywords": ["lost ball", "not found", "three minutes", "search time", "player caddie partner", "interruptions don't count"],
        "examples": [
            "can't find ball in 3 minutes",
            "searched for 3 minutes unsuccessfully",
            "ball not located",
            "search time expired"
        ],
        "related_rules": ["18.2", "27.1"],
        "category": "ball_status"
    },
    
    {
        "id": "MARK",
        "term": "Mark", 
        "definition": "To show the spot where a ball is at rest by either placing a ball-marker right behind or right next to the ball, or holding a club on the ground right behind or right next to the ball.",
        "keywords": ["mark", "show spot", "ball marker", "behind next to", "club on ground", "ball position"],
        "examples": [
            "coin behind ball",
            "ball marker next to ball",
            "club held behind ball",
            "marking ball on green"
        ],
        "related_rules": ["14.1", "13.1b"],
        "category": "procedures"
    },
    
    {
        "id": "MOVED",
        "term": "Moved",
        "definition": "When a ball at rest has left its original spot and come to rest on any other spot, and this can be seen by the naked eye (whether or not anyone actually sees it do so). The movement can be up, down, or horizontally in any direction. If the ball only wobbles (oscillates) and stays on or returns to its original spot, the ball has NOT moved. The key test is whether the ball has come to rest in a different location than where it originally was.",
        "keywords": ["moved", "left original spot", "other spot", "naked eye", "wobbles doesn't count", "new position", "up down horizontal", "oscillates", "different location"],
        "examples": [
            "ball rolled to new spot",
            "wind moved ball", 
            "ball shifted position",
            "visible movement to different location",
            "ball wobbling but returning to same spot has NOT moved",
            "ball oscillating in place has NOT moved"
        ],
        "related_rules": ["9.1", "13.1d"],
        "category": "ball_movement"
    },
    
    {
        "id": "MOVABLE_OBSTRUCTION",
        "term": "Movable Obstruction", 
        "definition": "An obstruction that can be moved with reasonable effort and without damaging the obstruction or the course. Committee may define any obstruction to be immovable even if it meets movable criteria.",
        "keywords": ["movable obstruction", "reasonable effort", "no damage", "can move", "committee may define immovable"],
        "examples": [
            "rake in bunker",
            "loose cart", 
            "movable bench",
            "temporary signs",
            "maintenance equipment"
        ],
        "related_rules": ["15.2", "24.1"],
        "category": "obstructions"
    },
    
    {
        "id": "OBSTRUCTION",
        "term": "Obstruction",
        "definition": "Any artificial object except for integral objects and boundary objects. Examples include roads, buildings, sprinkler heads, stakes, golf carts, equipment, flagsticks and rakes. Either movable or immovable.",
        "keywords": ["obstruction", "artificial object", "not integral boundary", "roads buildings", "sprinkler heads", "carts equipment"],
        "examples": [
            "cart path interference",
            "sprinkler head in line", 
            "maintenance shed",
            "golf cart blocking",
            "rake near ball"
        ],
        "related_rules": ["15", "16.1", "24"],
        "category": "obstructions"
    },
    
    {
        "id": "OUT_OF_BOUNDS",
        "term": "Out of Bounds",
        "definition": "All areas outside the boundary edge of the course as defined by the Committee. The boundary edge extends both up above the ground and down below the ground. When defined by stakes or fence, the boundary edge is the line between the course-side points at ground level. When defined by painted lines on the ground, the boundary edge is the course-side edge of the line, and the line itself is out of bounds.",
        "keywords": ["out of bounds", "OB", "outside boundary", "committee defined", "above below ground", "white stakes", "white lines", "course side edge", "line is OB"],
        "examples": [
            "beyond white stakes",
            "over boundary fence", 
            "outside course limits",
            "past white line - line itself is OB",
            "ball touching white line is OB",
            "course-side edge of painted line",
            "off property"
        ],
        "related_rules": ["18.2", "27.1"],
        "category": "boundaries"
    },
    
    {
        "id": "PENALTY_AREA",
        "term": "Penalty Area",
        "definition": "An area from which relief with a one-stroke penalty is allowed if the player's ball comes to rest there. Includes any body of water on the course and any other area the Committee defines. The edge extends both up above the ground and down below the ground. When defined by stakes, the edge is the line between the outside points of the stakes at ground level, and the stakes are inside the penalty area. When defined by painted lines on the ground, the edge is the outside edge of the line, and the line itself is in the penalty area. Yellow penalty areas have two relief options; red penalty areas have an additional lateral relief option.",
        "keywords": ["penalty area", "water hazard", "one stroke penalty", "yellow red", "body of water", "committee defined", "lateral relief", "outside edge of line", "line in penalty area", "stakes inside"],
        "examples": [
            "water hazard with stakes",
            "pond marked yellow",
            "stream marked red", 
            "designated wetland area",
            "lateral water hazard",
            "ball touching red line is in penalty area",
            "line itself is in the penalty area",
            "outside edge of painted line is boundary"
        ],
        "related_rules": ["17", "26"],
        "category": "course_areas"
    },
    
    {
        "id": "PROVISIONAL_BALL",
        "term": "Provisional Ball",
        "definition": "Another ball played in case the ball just played by the player may be out of bounds or lost outside a penalty area. Not the player's ball in play unless it becomes the ball in play under Rule 18.3c.",
        "keywords": ["provisional ball", "may be OB", "may be lost", "outside penalty area", "not in play unless", "backup ball"],
        "examples": [
            "might be out of bounds",
            "second ball from tee",
            "backup ball played", 
            "provisional off tee",
            "safety ball"
        ],
        "related_rules": ["18.3", "27.2"],
        "category": "ball_procedures"
    },
    
    {
        "id": "PUTTING_GREEN",
        "term": "Putting Green",
        "definition": "The area on the hole the player is playing that is specially prepared for putting, or the Committee has defined as the putting green. Contains the hole into which the player tries to play a ball. Other greens are wrong greens.",
        "keywords": ["putting green", "specially prepared", "putting", "committee defined", "contains hole", "other greens wrong"],
        "examples": [
            "green being played",
            "putting surface",
            "area around hole", 
            "specially maintained area",
            "target green"
        ],
        "related_rules": ["13", "25.3"],
        "category": "course_areas"
    },
    
    {
        "id": "RELIEF_AREA",
        "term": "Relief Area",
        "definition": "The area where a player must drop a ball when taking relief under a Rule. Size and location based on reference point, size measured from reference point (one or two club-lengths), and limits on location.",
        "keywords": ["relief area", "drop ball", "reference point", "one two club lengths", "limits location", "taking relief"],
        "examples": [
            "drop zone from obstruction",
            "one club-length from point",
            "two club-lengths relief", 
            "not nearer hole",
            "within relief bounds"
        ],
        "related_rules": ["14.3", "16.1", "17.1"],
        "category": "procedures"
    },
    
    {
        "id": "REPLACE",
        "term": "Replace",
        "definition": "To place a ball by setting it down and letting it go, with the intent for it to be in play. Rules identify the specific spot where ball must be replaced when required.",
        "keywords": ["replace", "place ball", "set down let go", "in play", "specific spot", "required"],
        "examples": [
            "replace on original spot",
            "put ball back",
            "return to position", 
            "place where marked",
            "restore ball position"
        ],
        "related_rules": ["14.2", "9.4"],
        "category": "procedures"
    },
    
    {
        "id": "STANCE",
        "term": "Stance",
        "definition": "The position of a player's feet and body in preparing for and making a stroke.",
        "keywords": ["stance", "feet position", "body position", "preparing stroke", "making stroke"],
        "examples": [
            "address position",
            "setup for shot",
            "feet placement", 
            "body alignment",
            "ready position"
        ],
        "related_rules": ["8.1", "16.1"],
        "category": "swing_mechanics"
    },
    
    {
        "id": "STROKE",
        "term": "Stroke", 
        "definition": "The forward movement of the club made to strike the ball. Not a stroke if player decides during downswing not to strike and avoids doing so, or accidentally strikes during practice swing or preparation.",
        "keywords": ["stroke", "forward movement", "strike ball", "not if avoid", "not practice swing", "not accident"],
        "examples": [
            "swing that hits ball",
            "intentional ball contact", 
            "completed golf swing",
            "counting stroke"
        ],
        "related_rules": ["1.1", "9.1"],
        "category": "swing_mechanics"
    },
    
    {
        "id": "SUBSTITUTE",
        "term": "Substitute",
        "definition": "To change the ball the player is using to play a hole by having another ball become the ball in play. Occurs when putting another ball in play instead of original ball, whether original was in play or not.",
        "keywords": ["substitute", "change ball", "another ball in play", "instead of original", "whether in play or not"],
        "examples": [
            "new ball for damaged ball",
            "different ball after relief",
            "replacement ball in play", 
            "switching balls"
        ],
        "related_rules": ["14.6", "15.3"],
        "category": "ball_procedures"
    },
    
    {
        "id": "TEEING_AREA",
        "term": "Teeing Area",
        "definition": "The area the player must play from in starting the hole. A rectangle two club-lengths deep where the front edge is defined by the line between the forward-most points of two tee-markers set by the Committee.",
        "keywords": ["teeing area", "starting hole", "rectangle", "two club lengths deep", "tee markers", "committee set"],
        "examples": [
            "tee box",
            "between tee markers", 
            "starting area for hole",
            "two club-lengths back",
            "first shot area"
        ],
        "related_rules": ["6.2", "11.1"],
        "category": "course_areas"
    },
    
    {
        "id": "TEMPORARY_WATER",
        "term": "Temporary Water",
        "definition": "Any temporary accumulation of water on the surface of the ground (such as puddles from rain or irrigation or an overflow from a body of water) that is not in a penalty area and can be seen before or after the player takes a stance. It is not enough for the ground to be merely wet, muddy or soft - an accumulation of water must remain present either before or after the stance is taken. Special cases: Dew and frost are NOT temporary water. Snow and natural ice (other than frost) are either loose impediments or temporary water, at the player's option. Manufactured ice is an obstruction.",
        "keywords": ["temporary water", "accumulation water", "surface ground", "not penalty area", "before after stance", "not wet muddy soft", "dew frost not temporary", "snow player option", "manufactured ice obstruction"],
        "examples": [
            "puddles from rain",
            "irrigation overflow",
            "standing water on fairway", 
            "casual water",
            "water visible when standing",
            "dew on grass is NOT temporary water",
            "frost is NOT temporary water",
            "ice from sprinklers is obstruction"
        ],
        "related_rules": ["16.1", "25.1"],
        "category": "course_conditions"
    },
    
    {
        "id": "WRONG_BALL",
        "term": "Wrong Ball",
        "definition": "Any ball other than the player's ball in play, provisional ball (before abandoned), or second ball in stroke play. Includes another player's ball, stray balls, or player's own ball that is out of bounds, lost, or lifted and not yet put back in play.",
        "keywords": ["wrong ball", "not players ball", "other than in play provisional second", "another players", "stray", "OB lost lifted"],
        "examples": [
            "another player's ball",
            "stray ball found",
            "player's old ball", 
            "ball not in play",
            "incorrect ball played"
        ],
        "related_rules": ["6.3c", "15.3"],
        "category": "ball_identification"
    },
    
    {
        "id": "WRONG_GREEN",
        "term": "Wrong Green",
        "definition": "Any green on the course other than the putting green for the hole the player is playing. Includes putting greens for other holes, normal green when temporary green is used, and practice greens unless Committee excludes them.",
        "keywords": ["wrong green", "other than putting green", "hole being played", "other holes", "practice greens", "committee exclude"],
        "examples": [
            "green from another hole",
            "practice putting green",
            "chipping green", 
            "green not being played",
            "adjacent hole's green"
        ],
        "related_rules": ["13.1f", "25.3"],
        "category": "course_areas"
    },
    
    {
        "id": "WRONG_PLACE",
        "term": "Wrong Place", 
        "definition": "Any place on the course other than where the player is required or allowed to play his or her ball under the Rules. Includes playing after replacing on wrong spot, from outside relief area, under wrong rule, or from no play zone.",
        "keywords": ["wrong place", "other than required allowed", "wrong spot", "outside relief area", "wrong rule", "no play zone"],
        "examples": [
            "dropped outside relief area",
            "replaced on incorrect spot",
            "played from no play zone", 
            "wrong relief procedure",
            "not allowed location"
        ],
        "related_rules": ["14.7", "20.7"],
        "category": "playing_violations"
    }
]

# Search optimization data for definitions
DEFINITIONS_SEARCH_DATA = {
    'common_queries': {
        'what is abnormal course condition': ['ABNORMAL_COURSE_CONDITION'],
        'what counts as advice': ['ADVICE'],
        'areas of golf course': ['AREAS_OF_COURSE', 'GENERAL_AREA', 'TEEING_AREA', 'PUTTING_GREEN', 'PENALTY_AREA', 'BUNKER'],
        'ball marker rules': ['BALL_MARKER', 'MARK'],
        'boundary fence relief': ['BOUNDARY_OBJECT'],
        'what is a bunker': ['BUNKER'],
        'caddie rules': ['CADDIE', 'ADVICE'],
        'club length measurement': ['CLUB_LENGTH', 'RELIEF_AREA'],
        'course boundaries': ['COURSE', 'OUT_OF_BOUNDS', 'BOUNDARY_OBJECT'],
        'how to drop ball': ['DROP', 'RELIEF_AREA'],
        'embedded ball definition': ['EMBEDDED'],
        'golf equipment rules': ['EQUIPMENT'],
        'flagstick rules': ['FLAGSTICK'],
        'general area definition': ['GENERAL_AREA'],
        'ground under repair': ['GROUND_UNDER_REPAIR', 'ABNORMAL_COURSE_CONDITION'],
        'what is a hole': ['HOLE', 'HOLED'],
        'when is ball holed': ['HOLED'],
        'immovable obstruction': ['IMMOVABLE_OBSTRUCTION', 'OBSTRUCTION'],
        'ball in play status': ['IN_PLAY'],
        'known or virtually certain': ['KNOWN_VIRTUALLY_CERTAIN'],
        'ball lie definition': ['LIE'],
        'line of play': ['LINE_OF_PLAY'],
        'loose impediments': ['LOOSE_IMPEDIMENT'],
        'lost ball definition': ['LOST'],
        'how to mark ball': ['MARK', 'BALL_MARKER'],
        'when ball moved': ['MOVED'],
        'movable obstruction': ['MOVABLE_OBSTRUCTION', 'OBSTRUCTION'],
        'obstruction definition': ['OBSTRUCTION', 'MOVABLE_OBSTRUCTION', 'IMMOVABLE_OBSTRUCTION'],
        'out of bounds definition': ['OUT_OF_BOUNDS'],
        'penalty area vs water hazard': ['PENALTY_AREA'],
        'provisional ball rules': ['PROVISIONAL_BALL'],
        'putting green definition': ['PUTTING_GREEN'],
        'relief area rules': ['RELIEF_AREA', 'CLUB_LENGTH'],
        'how to replace ball': ['REPLACE'],
        'golf stance definition': ['STANCE'],
        'what counts as stroke': ['STROKE'],
        'substitute ball': ['SUBSTITUTE'],
        'teeing area definition': ['TEEING_AREA'],
        'temporary water': ['TEMPORARY_WATER', 'ABNORMAL_COURSE_CONDITION'],
        'wrong ball played': ['WRONG_BALL'],
        'wrong green definition': ['WRONG_GREEN'],
        'wrong place penalty': ['WRONG_PLACE']
    },
    
    'category_groupings': {
        'course_areas': ['AREAS_OF_COURSE', 'GENERAL_AREA', 'TEEING_AREA', 'PUTTING_GREEN', 'PENALTY_AREA', 'BUNKER'],
        'ball_status': ['IN_PLAY', 'LOST', 'HOLED'],
        'ball_procedures': ['DROP', 'REPLACE', 'SUBSTITUTE', 'PROVISIONAL_BALL'],
        'obstructions': ['OBSTRUCTION', 'MOVABLE_OBSTRUCTION', 'IMMOVABLE_OBSTRUCTION'],
        'course_conditions': ['GROUND_UNDER_REPAIR', 'TEMPORARY_WATER', 'ABNORMAL_COURSE_CONDITION'],
        'boundaries': ['OUT_OF_BOUNDS', 'BOUNDARY_OBJECT', 'COURSE'],
        'equipment': ['EQUIPMENT', 'BALL_MARKER', 'FLAGSTICK'],
        'procedures': ['MARK', 'DROP', 'REPLACE', 'RELIEF_AREA'],
        'violations': ['WRONG_PLACE', 'WRONG_BALL', 'WRONG_GREEN'],
        'measurements': ['CLUB_LENGTH', 'RELIEF_AREA'],
        'playing_conditions': ['CONDITIONS_AFFECTING_STROKE', 'LIE', 'STANCE'],
        'standards': ['KNOWN_VIRTUALLY_CERTAIN'],
        'natural_objects': ['LOOSE_IMPEDIMENT'],
        'player_assistance': ['CADDIE', 'ADVICE']
    }
}

def get_definition_by_id(definition_id):
    """Get a specific definition by ID."""
    for definition in GOLF_DEFINITIONS_DATABASE:
        if definition['id'] == definition_id:
            return definition
    return None

def search_definitions_by_keyword(keywords):
    """Search definitions by keywords."""
    results = []
    keywords_lower = [k.lower() for k in keywords]
    
    for definition in GOLF_DEFINITIONS_DATABASE:
        # Check if any keyword matches
        matches = 0
        for keyword in keywords_lower:
            # Check term name
            if keyword in definition['term'].lower():
                matches += 2  # Higher weight for term match
            
            # Check definition text  
            if keyword in definition['definition'].lower():
                matches += 1
                
            # Check keywords list
            for def_keyword in definition['keywords']:
                if keyword in def_keyword.lower():
                    matches += 1
                    
            # Check examples
            for example in definition['examples']:
                if keyword in example.lower():
                    matches += 1
        
        if matches > 0:
            results.append({
                'definition': definition,
                'relevance_score': matches
            })
    
    # Sort by relevance score
    results.sort(key=lambda x: x['relevance_score'], reverse=True)
    return results

def get_definitions_by_category(category):
    """Get all definitions in a specific category."""
    if category in DEFINITIONS_SEARCH_DATA['category_groupings']:
        definition_ids = DEFINITIONS_SEARCH_DATA['category_groupings'][category]
        return [get_definition_by_id(def_id) for def_id in definition_ids if get_definition_by_id(def_id)]
    return []

def get_related_definitions(definition_id):
    """Get definitions related to a specific definition."""
    definition = get_definition_by_id(definition_id)
    if not definition:
        return []
    
    related = []
    category = definition['category']
    
    # Get other definitions in same category
    for other_def in GOLF_DEFINITIONS_DATABASE:
        if other_def['id'] != definition_id and other_def['category'] == category:
            related.append(other_def)
    
    return related[:5]  # Return top 5 related

# Quick access lookup for common definition queries
COMMON_DEFINITION_LOOKUPS = {
    'general area': 'GENERAL_AREA',
    'penalty area': 'PENALTY_AREA', 
    'water hazard': 'PENALTY_AREA',
    'bunker': 'BUNKER',
    'sand trap': 'BUNKER',
    'putting green': 'PUTTING_GREEN',
    'teeing area': 'TEEING_AREA',
    'tee box': 'TEEING_AREA',
    'out of bounds': 'OUT_OF_BOUNDS',
    'ob': 'OUT_OF_BOUNDS',
    'lost ball': 'LOST',
    'provisional ball': 'PROVISIONAL_BALL',
    'wrong ball': 'WRONG_BALL',
    'ground under repair': 'GROUND_UNDER_REPAIR',
    'gur': 'GROUND_UNDER_REPAIR',
    'temporary water': 'TEMPORARY_WATER',
    'casual water': 'TEMPORARY_WATER',
    'obstruction': 'OBSTRUCTION',
    'immovable obstruction': 'IMMOVABLE_OBSTRUCTION',
    'movable obstruction': 'MOVABLE_OBSTRUCTION',
    'loose impediment': 'LOOSE_IMPEDIMENT',
    'advice': 'ADVICE',
    'caddie': 'CADDIE',
    'ball marker': 'BALL_MARKER',
    'flagstick': 'FLAGSTICK',
    'pin': 'FLAGSTICK',
    'embedded': 'EMBEDDED',
    'plugged': 'EMBEDDED',
    'relief area': 'RELIEF_AREA',
    'club length': 'CLUB_LENGTH',
    'abnormal course condition': 'ABNORMAL_COURSE_CONDITION'
}
]
