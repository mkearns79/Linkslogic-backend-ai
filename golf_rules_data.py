"""Golf rules database for the hybrid approach."""

# Core golf rules with structured data
RULES_DATABASE = [
    # --- Section 1: The Game, Player Conduct and the Rules ---
    {
        "id": "1",
        "title": "The Game, Player Conduct and the Rules",
        "text": "Rule 1 introduces these central principles of the game for the player: Play the course as you find it and play the ball as it lies. Play by the Rules and in the spirit of the game. You are responsible for applying your own penalties if you breach a Rule, so that you cannot gain any potential advantage over your opponent in match play or other players in stroke play.",
        "keywords": ["central principles", "play course as found", "play ball as lies", "rules", "spirit of game", "apply own penalties", "no advantage"],
        "examples": [
            "fundamental golf principles",
            "play as found principle",
            "self-penalty application",
            "fair play standards"
        ]
    },
    {
        "id": "1.1",
        "title": "The Game of Golf",
        "text": "Golf is played in a round of 18 (or fewer) holes on a course by striking a ball with a club. Each hole starts with a stroke from the teeing area and ends when the ball is holed on the putting green (or when the Rules otherwise say the hole is completed). For each stroke, the player plays the course as they find it and plays the ball as it lies, but there are exceptions where the Rules allow altering conditions or playing from a different place.",
        "keywords": ["golf", "18 holes", "fewer holes", "course", "striking ball", "club", "teeing area", "putting green", "holed", "play as found", "ball as lies", "exceptions"],
        "examples": [
            "basic golf game definition",
            "hole completion rules",
            "fundamental playing principles",
            "course and ball conditions"
        ],
        "conditions": [
        {
            "situation": "Basic definition of golf",
            "explanation": "Under Rule 1.1, golf is played in a round of 18 (or fewer) holes on a course by striking a ball with a club.",
            "examples": ["18 holes or fewer", "striking ball with club", "played on course", "round format"]
        },
        {
            "situation": "Hole start and completion",
            "explanation": "Under Rule 1.1, each hole starts with a stroke from the teeing area and ends when the ball is holed on the putting green (or when the Rules otherwise say the hole is completed).",
            "examples": ["starts from teeing area", "ends when holed", "putting green completion", "rules may specify completion"]
        },
        {
            "situation": "Fundamental playing principles",
            "explanation": "Under Rule 1.1, for each stroke, the player plays the course as they find it and plays the ball as it lies.",
            "examples": ["course as found", "ball as lies", "each stroke principle", "fundamental approach"]
        },
        {
            "situation": "Exceptions to basic principles",
            "explanation": "Under Rule 1.1, there are exceptions where the Rules allow the player to alter conditions on the course and require or allow the player to play the ball from a different place than where it lies.",
            "examples": ["alter course conditions", "play from different place", "rules allow exceptions", "specific circumstances"]
        }
    ]
    },
    {
        "id": "1.2",
        "title": "Standards of Player Conduct",
        "text": "All players are expected to play in the spirit of the game by acting with integrity, showing consideration to others, and taking good care of the course. There is no penalty under the Rules for failing to act this way, except that the Committee may disqualify a player for serious misconduct. The Committee may set its own standards in a Code of Conduct with specific penalties.",
        "keywords": ["standards", "player conduct", "spirit of game", "integrity", "consideration", "care of course", "no penalty", "serious misconduct", "disqualification", "code of conduct"],
        "examples": [
            "expected player behavior",
            "spirit of the game",
            "serious misconduct penalties",
            "committee conduct codes"
        ],
        "conditions": [
        {
            "situation": "Expected conduct - integrity",
            "explanation": "Under Rule 1.2a, all players are expected to act with integrity - for example, by following the Rules, applying all penalties, and being honest in all aspects of play.",
            "examples": ["following rules", "applying penalties", "being honest", "integrity in play"]
        },
        {
            "situation": "Expected conduct - consideration to others",
            "explanation": "Under Rule 1.2a, players should show consideration to others - for example, by playing at a prompt pace, looking out for safety, not distracting others, and shouting warnings like 'fore' when there's danger of hitting someone.",
            "examples": ["prompt pace", "safety awareness", "no distracting", "fore warning"]
        },
        {
            "situation": "Expected conduct - care of course",
            "explanation": "Under Rule 1.2a, players should take good care of the course - for example, by replacing divots, smoothing bunkers, repairing ball-marks, and not causing unnecessary damage.",
            "examples": ["replace divots", "smooth bunkers", "repair ball-marks", "avoid damage"]
        },
        {
            "situation": "No penalty for conduct failures",
            "explanation": "Under Rule 1.2a, there is no penalty under the Rules for failing to act in the expected way, except that the Committee may disqualify a player for acting contrary to the spirit of the game if serious misconduct is found.",
            "examples": ["no rules penalty", "committee may disqualify", "serious misconduct", "spirit of game violation"]
        },
        {
            "situation": "Definition of serious misconduct",
            "explanation": "Under Rule 1.2a, 'serious misconduct' is player behavior that is so far removed from what is expected in golf that the most severe sanction of removing a player from the competition is justified.",
            "examples": ["far removed from expected", "most severe sanction", "removing from competition", "justified disqualification"]
        },
        {
            "situation": "Other misconduct penalties",
            "explanation": "Under Rule 1.2a, penalties other than disqualification may be imposed for player misconduct only if those penalties are adopted as part of a Code of Conduct under Rule 1.2b.",
            "examples": ["other penalties only with code", "code of conduct required", "not automatic penalties", "committee adoption needed"]
        },
        {
            "situation": "Committee Code of Conduct",
            "explanation": "Under Rule 1.2b, the Committee may set its own standards of player conduct in a Code of Conduct adopted as a Local Rule, including penalties like one-stroke penalty or general penalty, and may disqualify for serious misconduct.",
            "examples": ["committee sets standards", "local rule adoption", "specific penalties", "disqualification option"]
        }
    ]
    },
    {
        "id": "1.3",
        "title": "Playing by the Rules",
        "text": "The 'Rules' means Rules 1-25, definitions, and any Local Rules the Committee adopts. Players are responsible for applying the Rules to themselves, including recognizing breaches and applying penalties honestly. Players use reasonable judgement in determining locations, and penalties are applied at specific levels with no discretion to vary them.",
        "keywords": ["playing by rules", "rules 1-25", "definitions", "local rules", "player responsibility", "applying rules", "reasonable judgment", "penalties", "no discretion"],
        "examples": [
            "definition of rules",
            "player self-policing",
            "reasonable judgment standard",
            "penalty level structure"
        ],
        "conditions": [
        {
            "situation": "Definition of Rules",
            "explanation": "Under Rule 1.3a, the term 'Rules' means Rules 1-25 and the definitions in these Rules of Golf, and any 'Local Rules' the Committee adopts for the competition or the course.",
            "examples": ["Rules 1-25", "definitions included", "local rules", "committee adoption"]
        },
        {
            "situation": "Terms of the Competition",
            "explanation": "Under Rule 1.3a, players are also responsible for complying with all 'Terms of the Competition' adopted by the Committee (such as entry requirements, form and dates of play, number of rounds, and number and order of holes).",
            "examples": ["entry requirements", "form and dates", "number of rounds", "hole order"]
        },
        {
            "situation": "Player responsibility for applying Rules",
            "explanation": "Under Rule 1.3b(1), players are responsible for applying the Rules to themselves: expected to recognize breaches, be honest in applying penalties, and if knowingly failing to apply a penalty, are disqualified.",
            "examples": ["recognize breaches", "honest penalty application", "deliberate failure = disqualification", "self-policing"]
        },
        {
            "situation": "Agreement to ignore Rules",
            "explanation": "Under Rule 1.3b(1), if two or more players agree to ignore any Rule or penalty they know applies and any have started the round, they are disqualified (even if not yet acted on the agreement).",
            "examples": ["agreement to ignore", "two or more players", "started round", "disqualification even without action"]
        },
        {
            "situation": "Deciding questions of fact",
            "explanation": "Under Rule 1.3b(1), when deciding questions of fact, a player is responsible for considering not only their own knowledge but also all other reasonably available information.",
            "examples": ["own knowledge", "reasonably available information", "fact determination", "comprehensive consideration"]
        },
        {
            "situation": "Asking for Rules help",
            "explanation": "Under Rule 1.3b(1), a player may ask for help with Rules from referee or Committee, but if help not available in reasonable time, must play on and raise issue when help becomes available.",
            "examples": ["referee or committee help", "reasonable time", "play on if no help", "raise issue later"]
        },
        {
            "situation": "Reasonable judgment in determining location",
            "explanation": "Under Rule 1.3b(2), many Rules require determining spots, points, lines, areas under the Rules (like estimating penalty area crossings, measuring relief, replacing balls, determining course areas, or abnormal conditions). Determinations must be prompt and careful but often cannot be precise.",
            "examples": ["penalty area crossings", "measuring relief", "replacing balls", "course area determination"]
        },
        {
            "situation": "Accepting reasonable judgment",
            "explanation": "Under Rule 1.3b(2), so long as player does what can reasonably be expected under circumstances to make accurate determination, reasonable judgment will be accepted even if later shown wrong by video or other information.",
            "examples": ["reasonably expected effort", "accurate determination attempt", "accepted even if wrong", "video evidence doesn't change"]
        },
        {
            "situation": "Correcting wrong determination",
            "explanation": "Under Rule 1.3b(2), if a player becomes aware of a wrong determination before the stroke is made, it must be corrected (see Rule 14.5).",
            "examples": ["aware before stroke", "must be corrected", "Rule 14.5 reference", "pre-stroke correction"]
        },
        {
            "situation": "Actions giving rise to penalties",
            "explanation": "Under Rule 1.3c(1), a penalty applies when a breach results from player's own actions or caddie's actions, or when another person acts that would breach Rules if done by player/caddie at player's request or with authority, or when player sees someone else about to breach Rules concerning the player's ball/equipment and doesn't object or stop it.",
            "examples": ["player or caddie actions", "other person at request", "with player authority", "failure to object or stop"]
        },
        {
            "situation": "Penalty levels",
            "explanation": "Under Rule 1.3c(2), penalties cancel potential advantage with three levels: One-Stroke Penalty (minor advantage or penalty relief), General Penalty (loss of hole/two strokes for most breaches), Disqualification (serious misconduct or significant advantage making score invalid).",
            "examples": ["one-stroke for minor", "general for most breaches", "disqualification for serious", "penalty matches advantage"]
        },
        {
            "situation": "No discretion to vary penalties",
            "explanation": "Under Rule 1.3c(3), penalties must be applied only as provided in Rules - neither player nor Committee has authority to apply differently, and wrong application may stand only if too late to correct. In match play, players may agree how to decide Rules issues but not ignore known Rules or penalties.",
            "examples": ["no authority to vary", "wrong application may stand", "too late to correct", "match play agreement limitations"]
        },
        {
            "situation": "Multiple penalty application - intervening events",
            "explanation": "Under Rule 1.3c(4), whether multiple penalties apply depends on two intervening events: completion of a stroke, and being/becoming aware of a breach (including knowing, being told, or being uncertain about a breach).",
            "examples": ["completion of stroke", "being aware of breach", "being told of breach", "uncertain about breach"]
        },
        {
            "situation": "Single penalty for multiple breaches between events",
            "explanation": "Under Rule 1.3c(4), if player breaches multiple Rules or same Rule multiple times between intervening events, only one penalty applies. If different penalty levels, only the higher-level penalty applies.",
            "examples": ["multiple breaches between events", "unaware of multiple breaches between strokes", "only one penalty", "different levels", "Multiple mistakes before realizing any breach = single penalty", "higher-level applies"]
        },
        {
            "situation": "Multiple penalties for breaches before and after events",
            "explanation": "Under Rule 1.3c(4), if player breaches a Rule then breaches same or another Rule after an intervening event, multiple penalties apply.",
            "examples": ["breach before and after", "Once you know about a breach, new breaches get separate penalties", "each stroke creates a fresh start for penalty counting", "intervening event", "multiple penalties", "separate violations"]
        },
        {
            "situation": "Exception for failure to replace moved ball",
            "explanation": "Under Rule 1.3c(4), if player required to replace moved ball under Rule 9.4 but fails to do so and plays from wrong place, they get only general penalty under Rule 14.7a.",
            "examples": ["failure to replace", "Rule 9.4 requirement", "wrong place play", "only general penalty under 14.7a"]
        },
        {
            "situation": "Penalty relief strokes always apply",
            "explanation": "Under Rule 1.3c(4), penalty strokes for taking penalty relief (like one-stroke under Rules 17.1, 18.1, 19.2) are always applied in addition to any other penalties.",
            "examples": ["penalty relief strokes", "Rules 17.1 18.1 19.2", "always additional", "not absorbed"]
        }
    ]
    },

    # --- Section 2: The Course ---
    {
        "id": "2.1",
        "title": "Course Boundaries and Out of Bounds",
        "text": "Out of bounds is defined by the boundary edge of the course as defined by the Committee. All areas inside that edge are in bounds. The boundary edge of the course extends both up above the ground and down below the ground.",
        "keywords": ["out of bounds", "OB", "boundary", "edge", "course", "limits", "white stakes", "fence"],
        "examples": [
            "determining out of bounds",
            "white stakes on course",
            "boundary fence ruling"
        ]
    },
    {
        "id": "2.2",
        "title": "Defined Areas of the Course",
        "text": "There are five areas of the course: the general area (which covers the entire course except for four specific areas) and four specific areas (teeing area, penalty areas, bunkers, and putting green). A ball is always treated as lying in only one area, with specific rules for determining which area when the ball is in multiple areas.",
        "keywords": ["five areas", "general area", "specific areas", "teeing area", "penalty areas", "bunkers", "putting green", "ball lies", "one area"],
        "examples": [
            "course area definitions",
            "ball location determination",
            "area-specific rules",
            "overlapping area priority"
        ],
        "conditions": [
        {
            "situation": "General area definition",
            "explanation": "Under Rule 2.2a, the general area covers the entire course except for the four specific areas (teeing area, penalty areas, bunkers, putting green). It includes fairway, rough, trees, and every type of ground and growing or attached objects in that area.",
            "examples": ["entire course except four areas", "fairway and rough", "trees included", "growing objects included"]
        },
        {
            "situation": "Why called general area",
            "explanation": "Under Rule 2.2a, it's called the 'general area' because it covers most of the course and is where a player's ball will most often be played until the ball reaches the putting green.",
            "examples": ["covers most of course", "most often played", "until putting green", "majority of play"]
        },
        {
            "situation": "Four specific areas",
            "explanation": "Under Rule 2.2b, certain Rules apply specifically to four areas not in the general area: the teeing area for starting the hole (Rule 6.2), all penalty areas (Rule 17), all bunkers (Rule 12), and the putting green of the hole being played (Rule 13).",
            "examples": ["teeing area Rule 6.2", "penalty areas Rule 17", "bunkers Rule 12", "putting green Rule 13"]
        },
        {
            "situation": "Ball in multiple areas - general and specific",
            "explanation": "Under Rule 2.2c, if part of the ball is in both the general area and one of the four specific areas, it is treated as lying in that specific area of the course.",
            "examples": ["part in general and specific", "treated as specific area", "specific area takes priority", "not general area"]
        },
        {
            "situation": "Ball in multiple specific areas",
            "explanation": "Under Rule 2.2c, if part of the ball is in two specific areas, it is treated as lying in the specific area that comes first in this order: penalty area, bunker, putting green.",
            "examples": ["penalty area first priority", "bunker second priority", "putting green third priority", "hierarchical determination"]
        },
        {
            "situation": "Ball always in one area only",
            "explanation": "Under Rule 2.2c, a ball is always treated as lying in only one area of the course, and the area where the ball lies affects the Rules that apply in playing the ball or taking relief.",
            "examples": ["only one area", "affects applicable rules", "playing the ball", "taking relief"]
        }
    ]
    },
   {
        "id": "2.3",
        "title": "Objects or Conditions That Can Interfere with Play",
        "text": "Certain Rules may give free relief (relief with no penalty) from interference by certain defined objects or conditions, such as loose impediments, movable obstructions, and abnormal course conditions. But there is no free relief from boundary objects or integral objects that interfere with play.",
        "keywords": ["free relief", "no penalty", "interference", "loose impediments", "movable obstructions", "abnormal course conditions", "no relief", "boundary objects", "integral objects"],
        "examples": [
            "free relief situations",
            "interference by objects",
            "no relief exceptions",
            "penalty-free relief options"
        ],
        "conditions": [
        {
            "situation": "Free relief from loose impediments",
            "explanation": "Under Rule 2.3, certain Rules may give free relief (relief with no penalty) from interference by loose impediments (Rule 15.1).",
            "examples": ["loose impediments", "Rule 15.1", "free relief", "no penalty"]
        },
        {
            "situation": "Free relief from movable obstructions",
            "explanation": "Under Rule 2.3, certain Rules may give free relief from interference by movable obstructions (Rule 15.2).",
            "examples": ["movable obstructions", "Rule 15.2", "free relief", "interference"]
        },
        {
            "situation": "Free relief from abnormal course conditions",
            "explanation": "Under Rule 2.3, certain Rules may give free relief from interference by abnormal course conditions, which are animal holes, ground under repair, immovable obstructions and temporary water (Rule 16.1).",
            "examples": ["animal holes", "ground under repair", "immovable obstructions", "temporary water", "Rule 16.1"]
        },
        {
            "situation": "No free relief from boundary objects",
            "explanation": "Under Rule 2.3, there is no free relief from boundary objects that interfere with play.",
            "examples": ["boundary objects", "no free relief", "no relief from bounary stakes", "no relief from boundary fences", "interfere with play", "must play as lies"]
        },
        {
            "situation": "No free relief from integral objects",
            "explanation": "Under Rule 2.3, there is no free relief from integral objects that interfere with play.",
            "examples": ["integral objects", "no free relief", "interfere with play", "part of course design"]
        }
    ]
    },
    {
        "id": "2.4",
        "title": "No Play Zones",
        "text": "A no play zone is a defined part of an abnormal course condition or a penalty area where play is not allowed. A player must take relief when their ball is in a no play zone, or when a no play zone interferes with their area of intended stance or area of intended swing in playing a ball outside the no play zone.",
        "keywords": ["no play zone", "abnormal course condition", "penalty area", "play not allowed", "must take relief", "ball in zone", "interferes", "intended stance", "intended swing"],
        "examples": [
            "no play zone relief requirements",
            "mandatory relief situations",
            "interference with stance or swing",
            "environmental protection areas"
        ],
        "conditions": [
        {
            "situation": "Definition of no play zone",
            "explanation": "Under Rule 2.4, a no play zone is a defined part of an abnormal course condition (see Rule 16.1f) or a penalty area (see Rule 17.1e) where play is not allowed.",
            "examples": ["defined part of abnormal condition", "part of penalty area", "play not allowed", "Rule 16.1f and 17.1e"]
        },
        {
            "situation": "Mandatory relief when ball in no play zone",
            "explanation": "Under Rule 2.4, a player must take relief when their ball is in a no play zone.",
            "examples": ["ball in no play zone", "must take relief", "mandatory relief", "cannot play from zone"]
        },
        {
            "situation": "Mandatory relief when zone interferes with stance or swing",
            "explanation": "Under Rule 2.4, a player must take relief when a no play zone interferes with their area of intended stance or area of intended swing in playing a ball outside the no play zone (see Rules 16.1f and 17.1e).",
            "examples": ["ball outside zone", "zone interferes with stance", "zone interferes with swing", "intended stance or swing area"]
        },
        {
            "situation": "Code of Conduct restrictions",
            "explanation": "Under Rule 2.4, a Code of Conduct may tell players to stay out of a no play zone entirely (see Committee Procedures, Section 5I(2)).",
            "examples": ["code of conduct", "stay out entirely", "additional restrictions", "committee procedures"]
        }
    ]
    },

    # --- Section 3: The Competition ---    
    {
    "id": "3",
    "title": "The Competition",
    "text": "Rule 3 covers the three central elements of all golf competitions: Playing either match play or stroke play, playing either as an individual or with a partner as part of a side, and scoring either by gross scores (no handicap strokes applied) or net scores (handicap strokes applied).",
    "keywords": ["competition", "match play", "stroke play", "individual", "partner", "side", "gross scores", "net scores", "handicap strokes"],
    "examples": [
        "competition formats",
        "scoring methods",
        "partner play",
        "handicap applications"
    ]
    },
    {
        "id": "3.1",
        "title": "Central Elements of Every Competition",
        "text": "Every competition has three central elements: form of play (match play or stroke play), how players compete (individual or partners), and how players score (gross or net scores). Most Rules apply in both forms of play, but certain Rules apply in only one or the other.",
        "keywords": ["central elements", "form of play", "how players compete", "how players score", "most rules apply", "certain rules", "only one"],
        "examples": [
            "competition structure",
            "play format differences",
            "scoring variations",
            "rule applications"
        ],
        "conditions": [
        {
            "situation": "Match play vs stroke play",
            "explanation": "Under Rule 3.1a(1), in match play, a player and opponent compete against each other based on holes won, lost or tied. In regular stroke play, all players compete based on total score - adding up each player's total strokes (including penalty strokes) on each hole in all rounds.",
            "examples": ["holes won lost tied", "total score competition", "all players compete", "strokes and penalties"]
        },
        {
            "situation": "Other forms of stroke play",
            "explanation": "Under Rule 3.1a(2), Rule 21 covers other forms of stroke play (Stableford, Maximum Score and Par/Bogey) that use different scoring methods. Rules 1-20 apply in these forms, as modified by Rule 21.",
            "examples": ["Stableford scoring", "Maximum Score", "Par/Bogey", "Rule 21 modifications"]
        },
        {
            "situation": "Individual vs partner play",
            "explanation": "Under Rule 3.1b, golf is played either by individual players competing on their own or by partners competing together as a side. Rules 1-20 and 25 focus on individual play but also apply in partner competitions (Foursomes and Four-Ball, modified by Rules 22 and 23) and team competitions (modified by Rule 24).",
            "examples": ["individual players", "partners as side", "Foursomes Four-Ball", "team competitions"]
        },
        {
            "situation": "Gross vs net scoring",
            "explanation": "Under Rule 3.1c, in scratch competitions the player's 'gross score' is total strokes (including penalties) with no handicap applied. In handicap competitions, the 'net score' is gross score adjusted for handicap strokes so players of differing abilities can compete fairly.",
            "examples": ["gross score total strokes", "no handicap applied", "net score adjusted", "fair competition"]
        }
    ]
    },
    {
        "id": "3.2",
        "title": "Match Play",
        "text": "Match play has specific Rules (particularly about concessions and giving information about strokes taken) because the player and opponent compete solely against each other on every hole, can see each other's play, and can protect their own interests.",
        "keywords": ["match play", "specific rules", "concessions", "information", "strokes taken", "compete against each other", "see play", "protect interests"],
        "examples": [
            "match play rules",
            "concession procedures",
            "stroke information",
            "head-to-head competition"
        ],
        "conditions": [
        {
            "situation": "Winning a hole",
            "explanation": "Under Rule 3.2a(1), a player wins a hole when: completing the hole in fewer strokes than opponent, opponent concedes the hole, or opponent gets general penalty (loss of hole). Special rule: if opponent's ball needs to be holed to tie and is deliberately deflected with no reasonable chance to be holed, player wins.",
            "examples": ["fewer strokes wins", "opponent concedes", "general penalty loss", "deliberate deflection rule"]
        },
        {
            "situation": "Tying a hole",
            "explanation": "Under Rule 3.2a(2), a hole is tied (halved) when: player and opponent complete hole in same number of strokes, or they agree to treat hole as tied (but only after at least one player has made a stroke to begin the hole).",
            "examples": ["same number strokes", "agree to tie", "after stroke begun", "halved hole"]
        },
        {
            "situation": "Winning a match",
            "explanation": "Under Rule 3.2a(3), a player wins a match when: leading opponent by more holes than remain to be played, opponent concedes the match, or opponent is disqualified.",
            "examples": ["more holes than remain", "opponent concedes match", "opponent disqualified", "match victory"]
        },
        {
            "situation": "Extending tied match",
            "explanation": "Under Rule 3.2a(4), if match is tied after final hole: match extends one hole at a time until winner, holes played in same order unless Committee sets different order, but Terms of Competition may say match ends in tie rather than extend.",
            "examples": ["one hole at a time", "same order", "committee different order", "terms may allow tie"]
        },
        {
            "situation": "When result is final",
            "explanation": "Under Rule 3.2a(5), match result becomes final in way stated by Committee (in Terms of Competition), such as when recorded on official scoreboard or other identified place, or when reported to person identified by Committee.",
            "examples": ["committee determines", "official scoreboard", "identified place", "reported to identified person"]
        },
        {
            "situation": "Conceding next stroke",
            "explanation": "Under Rule 3.2b(1), a player may concede opponent's next stroke any time before it's made. Opponent completes hole with score including conceded stroke, ball may be removed by anyone. Concession while ball in motion applies to next stroke unless ball is holed.",
            "examples": ["before stroke made", "score includes conceded", "ball removed by anyone", "motion applies to next"]
        },
        {
            "situation": "Conceding by deflecting ball",
            "explanation": "Under Rule 3.2b(1), player may concede opponent's next stroke by deflecting or stopping opponent's ball in motion only if done specifically to concede next stroke and only when no reasonable chance ball can be holed.",
            "examples": ["deflecting to concede", "specifically to concede", "no reasonable chance", "stopping ball in motion"]
        },
        {
            "situation": "Conceding a hole",
            "explanation": "Under Rule 3.2b(1), conceding a hole is allowed any time before hole is completed, including before players start hole. Players not allowed to agree to concede holes to each other for shortening match - doing so knowingly results in disqualification.",
            "examples": ["before hole completed", "before starting hole", "cannot agree mutual concession", "shortening match disqualifies"]
        },
        {
            "situation": "Conceding the match",
            "explanation": "Under Rule 3.2b(1), conceding the match is allowed any time before result is decided, including before players start the match.",
            "examples": ["before result decided", "before match starts", "any time allowed", "match concession"]
        },
        {
            "situation": "How concessions are made",
            "explanation": "Under Rule 3.2b(2), concession made only when clearly communicated verbally or by action showing intent (like gesture). If opponent lifts ball due to reasonable misunderstanding of concession, no penalty and ball replaced. Concession is final and cannot be declined or withdrawn.",
            "examples": ["clearly communicated", "verbal or gesture", "reasonable misunderstanding no penalty", "final cannot withdraw"]
        },
        {
            "situation": "Declaring handicaps in match",
            "explanation": "Under Rule 3.2c(1), player and opponent should tell each other handicaps before match. Wrong handicap declared: if too high and affects strokes given/received = disqualification, if doesn't affect = no penalty; if too low = no penalty but must use declared lower handicap.",
            "examples": ["tell before match", "too high affects strokes = DQ", "too high no affect = no penalty", "too low use declared"]
        },
        {
            "situation": "Handicap stroke application in match",
            "explanation": "Under Rule 3.2c(2), handicap strokes given by hole, lower net score wins hole. In extended match, strokes given same way as round unless Committee sets different way. Players responsible for knowing holes where they give/get strokes based on stroke index. Mistakes in applying strokes: agreed result stands unless corrected in time.",
            "examples": ["given by hole", "lower net wins", "extended match same", "stroke index responsibility", "mistakes stand unless corrected"]
        },
        {
            "situation": "Telling opponent about strokes taken",
            "explanation": "Under Rule 3.2d(1), opponent may ask for number of strokes taken any time during or after hole. Player must give right number when asked or giving without being asked. Wrong number given = general penalty (loss of hole) unless corrected in time: during hole before opponent's next stroke, after hole before either player starts next hole or match result final.",
            "examples": ["opponent may ask anytime", "must give right number", "wrong number = loss hole", "correct before next stroke or hole"]
        },
        {
            "situation": "Exception for wrong stroke count after hole",
            "explanation": "Under Rule 3.2d(1), no penalty if player gives wrong stroke count after hole completed but this doesn't affect opponent's understanding of whether hole was won, lost, or tied.",
            "examples": ["wrong count after hole", "no affect on understanding", "won lost tied", "no penalty exception"]
        },
        {
            "situation": "Telling opponent about penalty",
            "explanation": "Under Rule 3.2d(2), when player gets penalty, must tell opponent as soon as reasonably possible considering proximity and practical factors. Applies even if player doesn't know about penalty. Failure to tell and not correcting before opponent's next stroke = general penalty (loss of hole). Exception: no penalty if opponent knew of player's penalty.",
            "examples": ["as soon reasonably possible", "even if don't know", "before opponent next stroke", "must tell opponent about penalty before opponent's next stroke", "opponent knew = no penalty"]
        },
        {
            "situation": "Knowing match score",
            "explanation": "Under Rule 3.2d(3), players expected to know match score (holes up or all square). Mistaken agreement on wrong score may be corrected before either player starts next hole or match result final. If not corrected, wrong score becomes actual score. Exception: timely ruling request can correct wrong score from opponent's wrong stroke count or failure to report penalty.",
            "examples": ["holes up or all square", "correct before next hole", "wrong becomes actual", "timely ruling corrects"]
        },
        {
            "situation": "Protecting own rights and interests",
            "explanation": "Under Rule 3.2d(4), players should protect own rights under Rules. If player knows/believes opponent breached Rule, may choose whether to act. But agreeing not to apply Rules or a penalty they know applies, after the round has started = both disqualified. Disagreement about breach = either may ask for ruling. Assigned referee is responsible for acting on any breach seen or told about.",
            "examples": ["protect own rights", "choose whether act", "agree not apply = DQ both", "disagreement ask ruling"]
        }
    ]
    },
    {
        "id": "3.3",
        "title": "Stroke Play",
        "text": "Stroke play has specific Rules (particularly for scorecards and holing out) because each player competes against all other players in the competition, and all players need to be treated equally under the Rules. After the round, the player and marker must certify that the player's score for each hole is right and the player must return the scorecard to the Committee.",
        "keywords": ["stroke play", "specific rules", "scorecards", "holing out", "competes against all", "treated equally", "marker", "certify", "return scorecard"],
        "examples": [
            "stroke play procedures",
            "scorecard requirements",
            "marker responsibilities",
            "score certification"
        ],
        "conditions": [
        {
            "situation": "Winner in stroke play",
            "explanation": "Under Rule 3.3a, the player who completes all rounds in fewest total strokes (including strokes made and penalty strokes) is the winner. In handicap competition, this means fewest total net strokes.",
            "examples": ["fewest total strokes", "includes penalties", "handicap = net strokes", "all rounds completed"]
        },
        {
            "situation": "Marker identification and consistency",
            "explanation": "Under Rule 3.3b, player's score kept on scorecard by marker, either identified by Committee or chosen by player in Committee-approved way. Player must have same marker for entire round unless Committee approves change before or after it happens.",
            "examples": ["committee identified", "player chosen approved", "same marker entire round", "committee approve change"]
        },
        {
            "situation": "Marker's responsibility for entering scores",
            "explanation": "Under Rule 3.3b(1), after each hole, marker should confirm strokes with player and enter gross score on scorecard. When round ended, marker must certify hole scores. With multiple markers, each certifies their holes, but if one saw all holes, may certify all. Marker may refuse to certify wrong score - Committee decides.",
            "examples": ["confirm and enter each hole", "certify when ended", "multiple markers each certify", "refuse wrong score"]
        },
        {
            "situation": "Marker knowingly certifying wrong score",
            "explanation": "Under Rule 3.3b(1), if a marker who is a player knowingly certifies a wrong score for a hole, the marker should be disqualified under Rule 1.2a.",
            "examples": ["marker is player", "knowingly wrong score", "should be disqualified", "Rule 1.2a"]
        },
        {
            "situation": "Player's scorecard responsibilities",
            "explanation": "Under Rule 3.3b(2), during round player should track scores. When ended: carefully check hole scores and raise issues with Committee, ensure marker certifies, must not change score except with marker agreement or Committee approval, must certify and promptly return scorecard then cannot change. Breach = disqualification.",
            "examples": ["track during round", "check and raise issues", "ensure marker certifies", "certify and return promptly"]
        },
        {
            "situation": "Exception for marker failure",
            "explanation": "Under Rule 3.3b(2), no penalty if Committee finds player's breach was caused by marker's failure to carry out responsibilities (like leaving with scorecard or without certifying) beyond player's control.",
            "examples": ["marker failure caused breach", "beyond player control", "leaving with scorecard", "without certifying"]
        },
        {
            "situation": "Wrong score higher than actual",
            "explanation": "Under Rule 3.3b(3), if player returns scorecard with score higher than actual score, the higher returned score for the hole stands.",
            "examples": ["higher than actual", "returned score stands", "no change allowed", "stands as returned"]
        },
        {
            "situation": "Wrong score lower than actual",
            "explanation": "Under Rule 3.3b(3), if player returns scorecard with score lower than actual score or no score returned, player is disqualified.",
            "examples": ["lower than actual", "no score returned", "player disqualified", "serious penalty"]
        },
        {
            "situation": "Exception for unknown penalty",
            "explanation": "Under Rule 3.3b(3), if hole scores lower because excluded unknown penalty strokes before returning scorecard: not disqualified, Committee revises score by adding penalty strokes if found before competition close. Exception doesn't apply if excluded penalty is disqualification or player was told/uncertain about penalty and didn't raise with Committee.",
            "examples": ["unknown penalty excluded", "not disqualified", "committee adds penalty", "doesn't apply if told or uncertain"]
        },
        {
            "situation": "Handicap and adding scores not player responsibility",
            "explanation": "Under Rule 3.3b(4), no requirement for player's handicap on scorecard or for players to add up scores. No penalty for mistakes in showing/applying handicap or adding up scores. Committee responsible for adding up scores and calculating handicap strokes for net score after receiving scorecard.",
            "examples": ["no handicap requirement", "no adding requirement", "no penalty for mistakes", "committee calculates"]
        },
        {
            "situation": "Marker refusal to certify wrong score",
            "explanation": "Under Rule 3.3b(1), a marker may refuse to certify a player's hole score that the marker believes is wrong. In such case, Committee will consider available evidence and make decision on player's score. If marker still refuses, Committee may certify the hole score or accept certification from someone else who saw the player's actions on the hole.",
            "examples": ["marker believes wrong", "committee considers evidence", "committee decision", "someone else certify"]
        },
        {
            "situation": "Player responsibilities when round ended",
            "explanation": "Under Rule 3.3b(2), when round ended, player: should carefully check hole scores entered by marker and raise issues with Committee, must ensure marker certifies hole scores, must not change hole score except with marker agreement or Committee approval, must certify hole scores and promptly return scorecard, after which cannot change scorecard.",
            "examples": ["check scores raise issues", "ensure marker certifies", "change only with agreement", "certify and return promptly"]
        },
        {
            "situation": "Changing hole scores on scorecard",
            "explanation": "Under Rule 3.3b(2), player must not change a hole score entered by marker except with marker's agreement or Committee's approval (but neither player nor marker required to make extra certification of changed score).",
            "examples": ["marker agreement required", "committee approval required", "no extra certification", "cannot change unilaterally"]
        },
        {
            "situation": "Breach of scorecard requirements",
            "explanation": "Under Rule 3.3b(2), if player breaches any requirements in Rule 3.3b, the player is disqualified.",
            "examples": ["any breach Rule 3.3b", "player disqualified", "scorecard requirements", "serious penalty"]
        },
        {
            "situation": "Exception when marker fails responsibilities",
            "explanation": "Under Rule 3.3b(2) Exception, there is no penalty if Committee finds player's breach of Rule 3.3b(2) was caused by marker's failure to carry out responsibilities (such as marker leaving with player's scorecard or without certifying scorecard), so long as this was beyond player's control.",
            "examples": ["marker failure caused breach", "leaving with scorecard", "without certifying", "beyond player control"]
        },
        {
            "situation": "Unknown penalty exception details",
            "explanation": "Under Rule 3.3b(3) Exception, the unknown penalty exception does not apply when: the excluded penalty is disqualification, or when player was told penalty might apply or was uncertain whether penalty applied and did not raise this with Committee before returning scorecard.",
            "examples": ["excluded penalty is DQ", "told penalty might apply", "uncertain about penalty", "did not raise with committee"]
        },
        {
            "situation": "Committee revision of score for unknown penalty",
            "explanation": "Under Rule 3.3b(3) Exception, if mistake found before close of competition, Committee will revise player's score for that hole or holes by adding penalty stroke(s) that should have been included under the Rules.",
            "examples": ["found before competition close", "committee revises score", "adding penalty strokes", "should have been included"]
        },
        {
            "situation": "Committee responsibilities after receiving scorecard",
            "explanation": "Under Rule 3.3b(4), once Committee receives scorecard from player at end of round, Committee is responsible for: adding up player's scores, and calculating player's handicap strokes for competition and using it to calculate net score.",
            "examples": ["committee receives scorecard", "adding up scores", "calculating handicap strokes", "net score calculation"]
        },
        {
            "situation": "No penalty for handicap or addition mistakes",
            "explanation": "Under Rule 3.3b(4), if player returns scorecard with mistake in showing or applying handicap, or mistake in adding up scores, there is no penalty.",
            "examples": ["mistake showing handicap", "mistake applying handicap", "mistake adding scores", "no penalty"]
        },
        {
            "situation": "Failure to hole out timing for correction",
            "explanation": "Under Rule 3.3c, if player fails to hole out at any hole: must correct that mistake before making stroke to begin another hole or, for final hole of round, before returning scorecard. If mistake not corrected in that time, player is disqualified.",
            "examples": ["before stroke next hole", "final hole before return", "not corrected in time", "player disqualified"]
        },
        {
            "situation": "Other stroke play forms and holing out",
            "explanation": "Under Rule 3.3c, see Rules 21.1, 21.2 and 21.3 for other forms of stroke play (Stableford, Maximum Score and Par/Bogey) where scoring is different and player is not disqualified if they do not hole out.",
            "examples": ["Stableford scoring", "Maximum Score", "Par/Bogey", "not disqualified"]
        }
    ]
    },

    # --- Section 4: Player's Equipment ---
    {
    "id": "4",
    "title": "The Player's Equipment",
    "text": "Rule 4 covers the equipment that players may use during a round. Based on the principle that golf is a challenging game in which success should depend on the player's judgment, skills and abilities, the player: Must use conforming clubs and balls, is limited to no more than 14 clubs and is restricted in the use of other equipment that gives artificial help to their play.",
    "keywords": ["player equipment", "challenging game", "judgment skills abilities", "conforming clubs balls", "14 clubs", "artificial help", "equipment restrictions"],
    "examples": [
        "equipment regulations",
        "club conformity",
        "artificial assistance limits",
        "skill-based competition"
    ]
    },
    {
        "id": "4.1",
        "title": "Clubs",
        "text": "Players must use conforming clubs when making strokes. Clubs damaged during a round may be repaired or replaced. Players must not deliberately change a club's playing characteristics during the round. Players are limited to 14 clubs, cannot share clubs with others, and must follow specific procedures when taking clubs out of play.",
        "keywords": ["conforming clubs", "making strokes", "damaged during round", "repair replace", "deliberately change", "playing characteristics", "14 clubs", "share clubs", "out of play"],
        "examples": [
            "club conformity requirements",
            "damage and repair rules",
            "14-club limit",
            "club sharing restrictions"
        ],
        "conditions": [
        {
            "situation": "Conforming clubs requirement",
            "explanation": "Under Rule 4.1a(1), in making a stroke, a player must use a club that conforms to Equipment Rules requirements when: it is new, or its playing characteristics have been changed in any way (but see Rule 4.1a(2) for clubs damaged during round). If playing characteristics change because of wear through normal use, it is still conforming.",
            "examples": ["new club conform", "characteristics changed", "damaged during round exception", "normal wear still conforming"]
        },
        {
            "situation": "Playing characteristics definition",
            "explanation": "Under Rule 4.1a(1), the 'playing characteristics' of a club are any part, feature, or property that affects how the club performs or aids in alignment, including but not limited to, weighting, lie, loft, alignment features and permissible external attachments.",
            "examples": ["affects performance", "aids alignment", "weighting lie loft", "alignment features attachments"]
        },
        {
            "situation": "Club damaged during round use and repair",
            "explanation": "Under Rule 4.1a(2), if a conforming club is damaged during a round or while play is stopped under Rule 5.7a, except in cases of abuse, the player may repair it or replace it with another club. The damaged club is treated as conforming for the rest of the round (but not during stroke play playoff).",
            "examples": ["damaged during round", "except cases of abuse", "repair or replace", "treated as conforming"]
        },
        {
            "situation": "Options with damaged club",
            "explanation": "Under Rule 4.1a(2), for the rest of the round, the player may: continue to make strokes with the damaged club, or except in cases of abuse, repair the club or replace it with another club. If replacing, must take damaged club out of play before making another stroke using Rule 4.1c(1) procedure.",
            "examples": ["continue with damaged", "repair or replace", "except abuse", "no replacing or repairing damaged club due to player abuse of the club", "take out of play", "cannot replace or repair club if damaged due to player throwing or slamming it"]
        },
        {
            "situation": "Definition of damaged during round",
            "explanation": "Under Rule 4.1a(2), 'damaged during a round' means when any part, feature, or property of a club is changed because of any act during the round (including while play stopped), whether by the player (making stroke, practice swing, putting in bag, dropping, leaning, throwing, abusing) or by any other person, outside influence or natural forces.",
            "examples": ["any part changed", "act during round", "by player actions", "other person outside influence"]
        },
        {
            "situation": "Not damaged if deliberately changed",
            "explanation": "Under Rule 4.1a(2), a club is not 'damaged during a round' if its playing characteristics are deliberately changed by the player during the round, as covered by Rule 4.1a(3).",
            "examples": ["not damaged if deliberate", "deliberately changed", "Rule 4.1a(3) covers", "different category"]
        },
        {
            "situation": "Deliberately changing club characteristics prohibited",
            "explanation": "Under Rule 4.1a(3), a player must not make a stroke with a club when they have deliberately changed that club's characteristics during the round by: using an adjustable feature or physically changing the club (except when allowed to repair damage), or by applying any substance to the clubhead (other than cleaning) to affect performance.",
            "examples": ["adjustable feature", "physically changing", "applying substance", "affect performance"]
        },
        {
            "situation": "Exception for restoring adjustable club",
            "explanation": "Under Rule 4.1a(3) Exception, there is no penalty and club may be used in two situations: if club's characteristics were changed by adjustable feature and before used to make stroke, club is restored as nearly as possible to original position by adjusting back, or a non-permissible external attachment is removed before club is used.",
            "examples": ["restored to original", "adjusting back", "non-permissible attachment removed", "before used"]
        },
        {
            "situation": "Penalty for non-conforming stroke",
            "explanation": "Under Rule 4.1a, penalty for making stroke in breach of Rule 4.1a: Disqualification. No penalty for merely having (but not making stroke with) non-conforming club or deliberately changed club, but such club still counts towards 14-club limit.",
            "examples": ["making non-conforming stroke = DQ", "merely having no penalty", "still counts towards 14", "disqualification penalty"]
        },
        {
            "situation": "14-club limit basic rule",
            "explanation": "Under Rule 4.1b(1), a player must not: start a round with more than 14 clubs, or have more than 14 clubs during the round. Limit includes all clubs carried by or for the player, but doesn't include parts of broken club and separated parts being carried at start of round.",
            "examples": ["start with more than 14", "have more during round", "carried by or for", "broken parts don't count"]
        },
        {
            "situation": "Adding clubs during round",
            "explanation": "Under Rule 4.1b(1), if player starts with fewer than 14 clubs, may add clubs during round up to 14-club limit (see Rule 4.1b(4) for restrictions). Club is considered added when player makes next stroke with any club while added club is in possession.",
            "examples": ["start with fewer", "add up to 14", "restrictions in 4.1b(4)", "added when next stroke"]
        },
        {
            "situation": "Procedure when exceeding 14 clubs",
            "explanation": "Under Rule 4.1b(1), when player becomes aware of having more than 14 clubs, must take excess clubs out of play before making another stroke using Rule 4.1c(1) procedure. If started with more than 14, may choose which clubs to remove. If added excess during round, those added clubs must be removed.",
            "examples": ["take excess out of play", "before another stroke", "started more = choose", "added excess = those removed"]
        },
        {
            "situation": "Other player's club not counted",
            "explanation": "Under Rule 4.1b(1), after player's round started, if player picks up another player's club left behind, or club mistakenly put in player's bag without knowledge, the club is not treated as one of player's clubs for 14-club limit (but must not be used).",
            "examples": ["picks up left behind", "mistakenly put in bag", "not treated as players", "must not be used"]
        },
        {
            "situation": "No sharing clubs rule",
            "explanation": "Under Rule 4.1b(2), player limited to clubs they started with or added as allowed. Must not make stroke with club being used by anyone else playing on course (even in different group or competition). When aware of breach, must take that club out of play before making another stroke using Rule 4.1c(1).",
            "examples": ["limited to own clubs", "not used by anyone else", "different group or competition", "take out of play"]
        },
        {
            "situation": "Partner exception for sharing",
            "explanation": "Under Rule 4.1b(2), see Rules 22.5 and 23.7 for limited exception in partner forms of play allowing partners to share clubs if they have no more than 14 clubs between them.",
            "examples": ["partner forms exception", "Rules 22.5 and 23.7", "14 clubs between them", "limited exception"]
        },
        {
            "situation": "No replacing lost clubs",
            "explanation": "Under Rule 4.1b(3), if player started with 14 clubs or added clubs up to limit of 14 and then lost a club during round or while play stopped under Rule 5.7a, the player must not replace it with another club.",
            "examples": ["started with 14", "added up to 14", "lost during round", "must not replace"]
        },
        {
            "situation": "Restrictions when adding or replacing",
            "explanation": "Under Rule 4.1b(4), when adding or replacing club under Rule 4.1a(2) or 4.1b(1), player must not: unreasonably delay play, add or borrow any club being carried by or for any other player on course, or build club from parts being carried by or for player or other player on course.",
            "examples": ["unreasonably delay play", "borrow from other player", "build from parts", "restrictions apply"]
        },
        {
            "situation": "Breach of adding/replacing restrictions",
            "explanation": "Under Rule 4.1b(4), when player becomes aware of breach by adding or replacing club when not allowed, must take that club out of play before making another stroke using Rule 4.1c(1). If makes stroke with club still carried after being taken out of play, disqualified under Rule 4.1c(1).",
            "examples": ["aware of breach", "take out of play", "stroke with club taken out of play = DQ", "Rule 4.1c(1)"]
        },
        {
            "situation": "Penalty timing for Rule 4.1b breach",
            "explanation": "Under Rule 4.1b, penalty applies based on when player becomes aware: if while playing hole, penalty applied at end of hole being played (in match play, complete hole, apply result, then apply penalty); if between holes, penalty applied as of end of hole just completed.",
            "examples": ["while playing hole", "end of hole played", "between holes", "end just completed"]
        },
        {
            "situation": "Match play penalty for excess clubs",
            "explanation": "Under Rule 4.1b, match play penalty is match score revised by deducting hole, maximum two holes. This is match adjustment penalty, not loss of hole. At end of hole being played or just completed, match score revised by deducting one hole for each hole where breach happened, maximum deduction two holes in round.",
            "examples": ["deducting hole maximum two", "match adjustment not loss", "one hole per breach", "maximum two holes round"]
        },
        {
            "situation": "Stroke play penalty for excess clubs",
            "explanation": "Under Rule 4.1b, stroke play penalty is general penalty (two penalty strokes) for each hole where breach happened, with maximum of four penalty strokes in round (adding two penalty strokes at each of first two holes where breach happened).",
            "examples": ["two strokes per hole", "maximum four strokes", "first two holes", "general penalty"]
        },
        {
            "situation": "Taking clubs out of play during round",
            "explanation": "Under Rule 4.1c(1), when player becomes aware during round of Rule 4.1b breach, must take action clearly indicating each club being taken out of play before making next stroke. May be done by: declaring to opponent/marker/player in group, or taking other clear action (turning upside down, placing on cart floor, giving to another person).",
            "examples": ["clearly indicating", "before next stroke", "declaring to others", "clear action"]
        },
        {
            "situation": "No strokes with taken out clubs",
            "explanation": "Under Rule 4.1c(1), player must not make stroke for rest of round with any club taken out of play. If club taken out is another player's club, that other player may continue to use the club. Penalty for breach of Rule 4.1c(1): Disqualification.",
            "examples": ["no stroke rest of round", "other player may continue", "breach = disqualification", "serious penalty"]
        },
        {
            "situation": "Taking clubs out before round",
            "explanation": "Under Rule 4.1c(2), if player becomes aware shortly before starting round that they accidentally have more than 14 clubs, should try to leave excess behind. As option without penalty: may take excess clubs out of play before start using procedure in (1), and excess clubs may be kept during round (but not used) and don't count towards 14-club limit.",
            "examples": ["accidentally more than 14", "try to leave behind", "option without penalty", "kept but not used"]
        },
        {
            "situation": "Deliberate excess clubs before round",
            "explanation": "Under Rule 4.1c(2), if player deliberately brings more than 14 clubs to first teeing area and starts round without leaving excess behind, the option to take out of play without penalty is not allowed and Rule 4.1b(1) applies.",
            "examples": ["deliberately brings more", "starts without leaving", "option not allowed", "Rule 4.1b(1) applies"]
        }
    ]
    },
    {
        "id": "4.2",
        "title": "Balls",
        "text": "Players must use conforming balls and must not play deliberately altered balls. If a ball breaks into pieces, there is no penalty and the stroke doesn't count - play another ball from where the stroke was made. Players may lift balls to check if cut or cracked during the hole and may substitute another ball only if clearly cut or cracked.",
        "keywords": ["conforming balls", "deliberately altered", "breaks into pieces", "no penalty", "stroke doesn't count", "lift to check", "cut or cracked", "substitute ball"],
        "examples": [
            "ball conformity requirements",
            "ball damage procedures",
            "substitution rules",
            "lifting to inspect"
        ],
        "conditions": [
        {
            "situation": "Conforming ball requirement",
            "explanation": "Under Rule 4.2a(1), in making each stroke, a player must use a ball that conforms to the requirements in the Equipment Rules. A player may get a conforming ball to play from anyone else, including another player on the course.",
            "examples": ["each stroke conforming", "Equipment Rules requirements", "get from anyone", "another player on course"]
        },
        {
            "situation": "Deliberately altered ball prohibited",
            "explanation": "Under Rule 4.2a(2), a player must not make a stroke at a ball whose performance characteristics have been deliberately altered, such as by scuffing or heating the ball or by applying any substance (other than in cleaning it).",
            "examples": ["performance characteristics altered", "scuffing or heating", "applying substance", "other than cleaning"]
        },
        {
            "situation": "Penalty for non-conforming or altered ball",
            "explanation": "Under Rule 4.2a, penalty for making stroke in breach of Rule 4.2a: Disqualification.",
            "examples": ["making stroke breach", "disqualification penalty", "serious consequence", "non-conforming or altered"]
        },
        {
            "situation": "Ball breaks into pieces",
            "explanation": "Under Rule 4.2b, if a player's ball breaks into pieces after a stroke, there is no penalty and the stroke does not count. The player must play another ball from where that stroke was made (see Rule 14.6).",
            "examples": ["breaks into pieces", "no penalty", "stroke doesn't count", "play another from same place"]
        },
        {
            "situation": "Wrong place penalty for broken ball",
            "explanation": "Under Rule 4.2b, penalty for playing ball from a wrong place in breach of Rule 4.2b: General Penalty under Rule 14.7a.",
            "examples": ["wrong place", "general penalty", "Rule 14.7a", "two strokes or loss of hole"]
        },
        {
            "situation": "Lifting ball to check if cut or cracked",
            "explanation": "Under Rule 4.2c(1), if player reasonably believes their ball has become cut or cracked during hole being played: may lift ball to look at it, but spot must first be marked, and ball must not be cleaned (except on putting green). If lifts without reasonable belief (except putting green), fails to mark spot, or cleans when not allowed, gets one penalty stroke.",
            "examples": ["reasonably believes", "mark spot first", "not cleaned except green", "without belief = penalty"]
        },
        {
            "situation": "When another ball may be substituted for cut/cracked",
            "explanation": "Under Rule 4.2c(2), player may substitute another ball only if it can be clearly seen that original ball is cut or cracked and this damage happened during hole being played – but not if only scratched or scraped or paint only damaged or discoloured.",
            "examples": ["clearly seen cut or cracked", "damage during hole", "not scratched or scraped", "not paint damage"]
        },
        {
            "situation": "Replacement procedure for cut/cracked ball",
            "explanation": "Under Rule 4.2c(2), if original ball is cut or cracked, player must replace either another ball or original ball on original spot. If original ball is not cut or cracked, player must replace it on original spot. If makes stroke at incorrectly substituted ball, gets one penalty stroke under Rule 6.3b.",
            "examples": ["replace on original spot", "another or original ball", "not cut = replace original", "incorrect substitution penalty"]
        },
        {
            "situation": "Other substitution rules not affected",
            "explanation": "Under Rule 4.2c(2), nothing in this Rule prohibits player from substituting another ball under any other Rule or changing balls between two holes.",
            "examples": ["other Rules allow substitution", "changing between holes", "nothing prohibits", "other circumstances"]
        },
        {
            "situation": "Wrong place penalty for cut/cracked ball",
            "explanation": "Under Rule 4.2c, penalty for playing ball from a wrong place in breach of Rule 4.2c: General Penalty Under Rule 14.7a.",
            "examples": ["wrong place", "general penalty", "Rule 14.7a", "two strokes or loss of hole"]
        }
    ]
    },
        {
        "id": "4.3",
        "title": "Use of Equipment",
        "text": "Rule 4.3 applies to all types of equipment except conforming clubs and balls (covered by Rules 4.1 and 4.2). Players may use equipment to help them play, except they must not create potential advantage by using equipment that artificially eliminates or reduces need for essential skill or judgment, or using equipment in an abnormal way in making a stroke.",
        "keywords": ["all types equipment", "except clubs balls", "help them play", "potential advantage", "artificially eliminates", "essential skill judgment", "abnormal way", "making stroke"],
        "examples": [
            "equipment usage rules",
            "artificial assistance limits",
            "skill preservation",
            "normal vs abnormal use"
        ],
        "conditions": [
        {
            "situation": "General equipment use principle",
            "explanation": "Under Rule 4.3a, a player may use equipment to help them play during a round, except that a player must not create a potential advantage by: using equipment (other than club or ball) that artificially eliminates or reduces need for skill or judgment essential to challenge of game, or using equipment (including club or ball) in abnormal way in making stroke.",
            "examples": ["may use to help", "not create advantage", "artificially eliminates skill", "abnormal way making stroke"]
        },
        {
            "situation": "Definition of abnormal way",
            "explanation": "Under Rule 4.3a, 'abnormal way' means a way that is fundamentally different than its intended use and is not normally recognized as part of playing the game.",
            "examples": ["fundamentally different", "intended use", "not normally recognized", "part of playing game"]
        },
        {
            "situation": "Distance and directional information allowed",
            "explanation": "Under Rule 4.3a(1), allowed: getting information on distance or direction (such as from distance-measuring device or compass).",
            "examples": ["distance measuring device", "compass", "distance or direction", "information allowed"]
        },
        {
            "situation": "Distance and directional information not allowed",
            "explanation": "Under Rule 4.3a(1), not allowed: measuring elevation changes, or interpreting distance or directional information (such as using device to get recommended line of play or club selection based on location of player's ball), or using alignment device to help align the ball.",
            "examples": ["measuring elevation", "interpreting information", "recommended line or club", "alignment device"]
        },
        {
            "situation": "Weather information allowed",
            "explanation": "Under Rule 4.3a(2), allowed: getting any type of weather information (including wind speed) available from weather forecasts or measuring temperature and humidity at course.",
            "examples": ["weather forecasts", "wind speed forecasts", "measuring temperature humidity", "at the course"]
        },
        {
            "situation": "Gauging wind by tossing grass, leaves, or other natural objects",
            "explanation": "While Rule 4.3a(2) doesn't specifically address a player's ability to toss grass or leaves to gauge the wind, it is permitted by implication because it is a natural method that aligns with the game's reliance on player judgement and is not prohibited under Rule 4.3a, or any other Rule, which restricts use of artificial aids. Previous versions of the Official Golf Rules did specifically allow tossing grass to gauge wind.",
            "examples": ["toss grass", "toss leaves", "gauging wind with grass is allowed"]
        },
        {
            "situation": "Weather information not allowed",
            "explanation": "Under Rule 4.3a(2), not allowed: measuring wind speed at the course, or using artificial object to get other wind-related information (such as using powder, handkerchief or ribbon to assess wind direction).",
            "examples": ["measuring wind at course", "artificial object", "powder handkerchief ribbon", "assess wind direction"]
        },
        {
            "situation": "Pre-round and recording information allowed",
            "explanation": "Under Rule 4.3a(3), allowed: using information gathered before round (such as playing information from previous rounds, swing tips or club recommendations), or recording (for use after round) playing or physiological information from round (such as club distance, playing statistics or heart rate).",
            "examples": ["before round information", "previous rounds tips", "recording for after", "club distance statistics heart rate"]
        },
        {
            "situation": "Processing current round information not allowed",
            "explanation": "Under Rule 4.3a(3), not allowed: processing or interpreting playing information from the round (such as club recommendations based on current round distances), or using any physiological information recorded during the round.",
            "examples": ["processing interpreting", "current round distances", "club recommendations", "physiological during round"]
        },
        {
            "situation": "Audio and video allowed",
            "explanation": "Under Rule 4.3a(4), allowed: listening to audio or watching video on matters unrelated to competition being played (such as news report or background music). But in doing so, consideration should be shown to others (see Rule 1.2).",
            "examples": ["unrelated to competition", "news report background music", "consideration to others", "Rule 1.2"]
        },
        {
            "situation": "Audio and video not allowed",
            "explanation": "Under Rule 4.3a(4), not allowed: listening to music or other audio to eliminate distractions or help with swing tempo, or watching video of competition that helps player in choosing club, making stroke, or deciding how to play during round, except may watch video being broadcast to spectators at course.",
            "examples": ["eliminate distractions", "help swing tempo", "competition video", "broadcast to spectators exception"]
        },
        {
            "situation": "Gloves and gripping agents allowed",
            "explanation": "Under Rule 4.3a(5), allowed: using plain glove that meets Equipment Rules requirements, using resin, powders and other moisturizing or drying agents, or wrapping towel or handkerchief around grip.",
            "examples": ["plain glove meets requirements", "resin powders agents", "moisturizing drying", "towel handkerchief around grip"]
        },
        {
            "situation": "Gloves and gripping agents not allowed",
            "explanation": "Under Rule 4.3a(5), not allowed: using glove that does not meet Equipment Rules requirements, or using other equipment that gives unfair advantage with hand position or grip pressure.",
            "examples": ["glove doesn't meet requirements", "unfair advantage", "hand position", "grip pressure"]
        },
        {
            "situation": "Stretching devices allowed",
            "explanation": "Under Rule 4.3a(6), allowed: using any equipment for general stretching (other than in making practice swing), whether equipment is designed for stretching, for use in golf (such as alignment rod placed across shoulders) or for any purpose unrelated to golf (such as rubber tubing or section of pipe).",
            "examples": ["general stretching", "other than practice swing", "alignment rod across shoulders", "rubber tubing pipe"]
        },
        {
            "situation": "Training and swing aids not allowed",
            "explanation": "Under Rule 4.3a(6), not allowed: using any type of golf training or swing aid (such as alignment rod or weighted headcover or 'donut') or non-conforming club in any way that creates potential advantage by helping player in preparing for or making stroke (such as help with swing plane, grip, alignment, ball position or posture).",
            "examples": ["training or swing aid", "alignment rod weighted headcover", "non-conforming club", "swing plane grip alignment posture"]
        },
        {
            "situation": "Medical exception general rule",
            "explanation": "Under Rule 4.3b(1), a player is not in breach of Rule 4.3 if they use equipment to help with medical condition, so long as: player has medical reason to use equipment, and Committee decides its use does not give player any unfair advantage over other players.",
            "examples": ["medical condition", "medical reason", "committee decides", "no unfair advantage"]
        },
        {
            "situation": "Tape or similar coverings for medical reasons",
            "explanation": "Under Rule 4.3b(2), a player may use adhesive tape or similar covering for any medical reason (such as to prevent injury or help with existing injury), but tape or covering must not: be applied excessively, or help player more than necessary for medical reason (for example, must not immobilize joint to help player swing club).",
            "examples": ["prevent or help injury", "not applied excessively", "not more than necessary", "not immobilize joint"]
        },
        {
            "situation": "Penalty structure for Rule 4.3",
            "explanation": "Under Rule 4.3, penalty for first breach: General Penalty (if breach happens between two holes, penalty applies to next hole). Penalty for second breach: Disqualification (applies even if nature of breach was entirely different, only applies if there has been intervening event after first breach).",
            "examples": ["first breach general penalty", "between holes = next hole", "second breach = DQ", "intervening event required"]
        }
    ]
    },

    # --- Section 5: Playing the Round and a Hole ---
    {
        "id": "5",
        "title": "Playing the Round",
        "text": "Rule 5 covers how to play a round – such as where and when a player may practice on the course before or during a round, when a round starts and ends and what happens when play has to stop or resume. Players are expected to: Start each round on time, and play continuously and at a prompt pace during each hole until the round is completed.",
        "keywords": ["playing the round", "practise on course", "round starts ends", "play stops resume", "start on time", "continuously", "prompt pace", "round completed"],
        "examples": [
            "round procedures",
            "practice restrictions",
            "timing requirements",
            "pace of play"
        ]
    },
    {
        "id": "5.1",
        "title": "Meaning of Round",
        "text": "A 'round' is 18 or fewer holes played in the order set by the Committee. When a round ends in a tie: tied match extended one hole at a time is continuation of same round, while play-off in stroke play is a new round. A player is playing their round from when it starts until it ends, except while play is stopped under Rule 5.7a.",
        "keywords": ["18 or fewer holes", "order set by committee", "ends in tie", "tied match extended", "same round", "play-off stroke play", "new round", "starts until ends", "play stopped"],
        "examples": [
            "round definition",
            "tie procedures",
            "round continuation",
            "play stoppage timing"
        ],
        "conditions": [
        {
            "situation": "Definition of round",
            "explanation": "Under Rule 5.1, a 'round' is 18 or fewer holes played in the order set by the Committee.",
            "examples": ["18 or fewer holes", "order set by committee", "round definition", "committee determines"]
        },
        {
            "situation": "Tied match extension",
            "explanation": "Under Rule 5.1, when round ends in tie and play continues: tied match extended one hole at a time is continuation of same round, not a new round.",
            "examples": ["tied match extended", "one hole at a time", "same round continuation", "not new round"]
        },
        {
            "situation": "Stroke play playoff",
            "explanation": "Under Rule 5.1, when round ends in tie and play continues: play-off in stroke play is a new round.",
            "examples": ["stroke play play-off", "new round", "different from match", "separate round"]
        },
        {
            "situation": "When player is playing round",
            "explanation": "Under Rule 5.1, a player is playing their round from when it starts until it ends (see Rule 5.3), except while play is stopped under Rule 5.7a. When Rule refers to actions 'during a round,' that does not include while play is stopped unless Rule says otherwise.",
            "examples": ["starts until ends", "except play stopped", "during round actions", "unless rule says otherwise"]
        }
    ]
    },
    {
        "id": "5.2",
        "title": "Practising on Course Before or Between Rounds",
        "text": "For this Rule, 'practising on the course' means playing a ball, or testing the surface of the putting green by rolling a ball or rubbing the surface. In match play, players may practise on the course before or between rounds. In stroke play, players must not practise on the course before a round, except putting/chipping near first tee, practice areas, or near completed hole's green.",
        "keywords": ["practising on course", "playing ball", "testing putting green", "rolling ball rubbing surface", "match play may practise", "stroke play must not", "putting chipping near tee", "practice areas", "completed hole green"],
        "examples": [
            "practice restrictions",
            "match vs stroke play differences",
            "allowed practice areas",
            "green testing rules"
        ],
        "conditions": [
        {
            "situation": "Definition of practising on course",
            "explanation": "Under Rule 5.2, 'practising on the course' means playing a ball, or testing the surface of the putting green of any hole by rolling a ball or rubbing the surface. The limitations apply only to the player, not to the player's caddie.",
            "examples": ["playing a ball", "testing putting green surface", "rolling ball rubbing", "player only not caddie"]
        },
        {
            "situation": "Match play practice allowance",
            "explanation": "Under Rule 5.2a, a player may practise on the course before a round or between rounds of a match-play competition.",
            "examples": ["may practise", "before round", "between rounds", "match-play competition"]
        },
        {
            "situation": "Stroke play practice restrictions",
            "explanation": "Under Rule 5.2b, on day of stroke-play competition: player must not practise on course before round, except may practise putting or chipping on or near first teeing area, practise on any practice area, practise on or near putting green of hole just completed even if will play that hole again same day.",
            "examples": ["must not practise", "except putting chipping", "near first tee", "practice area", "completed hole green"]
        },
        {
            "situation": "After final round practice",
            "explanation": "Under Rule 5.2b, a player may practise on the course after completing play of their final round for that day.",
            "examples": ["after final round", "completing play", "that day", "may practise"]
        },
        {
            "situation": "Penalty for stroke play practice breach",
            "explanation": "Under Rule 5.2b, if player makes stroke in breach of this Rule, they get general penalty applied to first hole. If they make additional stroke in breach, they are disqualified.",
            "examples": ["stroke in breach", "general penalty first hole", "additional stroke", "disqualified"]
        }
    ]
    },
    {
        "id": "5.3",
        "title": "Starting and Ending Round",
        "text": "A player's round starts when they make a stroke to start their first hole. Players must start at (not before) their starting time set by the Committee, treated as exact time. Round ends: in match play when result decided, in stroke play when player holes out at final hole. Penalty for late start is usually disqualification with limited exceptions.",
        "keywords": ["round starts", "stroke first hole", "start at starting time", "not before", "exact time", "round ends", "match play result decided", "stroke play holes out", "late start disqualification", "limited exceptions"],
        "examples": [
            "round start procedures",
            "starting time requirements",
            "round completion",
            "punctuality penalties"
        ],
        "conditions": [
        {
            "situation": "When round starts",
            "explanation": "Under Rule 5.3a, a player's round starts when the player makes a stroke to start their first hole (see Rule 6.1a).",
            "examples": ["stroke to start", "first hole", "Rule 6.1a", "round begins"]
        },
        {
            "situation": "Starting time requirement",
            "explanation": "Under Rule 5.3a, player must start at (and not before) their starting time: means player must be ready to play at starting time and starting point set by Committee. Starting time set by Committee is treated as exact time (for example, 9 am means 9:00:00 am, not any time until 9:01 am).",
            "examples": ["at not before", "ready to play", "starting point", "exact time 9:00:00"]
        },
        {
            "situation": "Delayed starting time accommodation",
            "explanation": "Under Rule 5.3a, if starting time is delayed for any reason (such as weather, slow play of other groups or need for ruling by referee), there is no breach if player is present and ready to play when player's group is able to start.",
            "examples": ["delayed for any reason", "weather slow play ruling", "present and ready", "group able to start"]
        },
        {
            "situation": "General penalty for late start",
            "explanation": "Under Rule 5.3a, penalty for breach of Rule 5.3a: Disqualification, except in three cases with exceptions.",
            "examples": ["breach = disqualification", "three exceptions", "general rule", "serious penalty"]
        },
        {
            "situation": "Exception 1 - Five minutes late",
            "explanation": "Under Rule 5.3a Exception 1, player arrives at starting point, ready to play, no more than five minutes late: the player gets general penalty applied to their first hole.",
            "examples": ["five minutes late", "ready to play", "general penalty", "first hole"]
        },
        {
            "situation": "Exception 2 - Five minutes early",
            "explanation": "Under Rule 5.3a Exception 2, player starts no more than five minutes early: the player gets general penalty applied to their first hole.",
            "examples": ["five minutes early", "starts early", "general penalty", "first hole"]
        },
        {
            "situation": "Exception 3 - Exceptional circumstances",
            "explanation": "Under Rule 5.3a Exception 3, Committee decides that exceptional circumstances prevented player from starting on time: there is no breach of this Rule and no penalty.",
            "examples": ["exceptional circumstances", "committee decides", "prevented starting", "no breach no penalty"]
        },
        {
            "situation": "When round ends match play",
            "explanation": "Under Rule 5.3b, a player's round ends: in match play, when the result of the match is decided under Rule 3.2a(3) or (4).",
            "examples": ["match play", "result decided", "Rule 3.2a(3) or (4)", "match completion"]
        },
        {
            "situation": "When round ends stroke play",
            "explanation": "Under Rule 5.3b, a player's round ends: in stroke play, when the player holes out at the final hole (including correction of a mistake, such as under Rule 6.1 or 14.7b).",
            "examples": ["stroke play", "holes out final hole", "correction of mistake", "Rule 6.1 or 14.7b"]
        }
    ]
    },
    {
        "id": "5.4",
        "title": "Playing in Groups",
        "text": "In match play, the player and opponent must play each hole in the same group during a round. In stroke play, the player must remain in the group set by the Committee during a round, unless the Committee approves a change either before or after it happens. Penalty for breach: Disqualification.",
        "keywords": ["match play", "player opponent", "same group", "stroke play", "remain in group", "committee set", "committee approves change", "before or after", "disqualification"],
        "examples": [
            "group integrity",
            "match play pairing",
            "stroke play grouping",
            "committee approval"
        ],
        "conditions": [
        {
            "situation": "Match play group requirement",
            "explanation": "Under Rule 5.4a, during a round, the player and opponent must play each hole in the same group.",
            "examples": ["player and opponent", "each hole", "same group", "during round"]
        },
        {
            "situation": "Stroke play group requirement",
            "explanation": "Under Rule 5.4b, during a round, the player must remain in the group set by the Committee, unless the Committee approves a change either before or after it happens.",
            "examples": ["remain in group", "set by committee", "committee approves change", "before or after"]
        },
        {
            "situation": "Penalty for group breach",
            "explanation": "Under Rule 5.4, penalty for breach of Rule 5.4: Disqualification.",
            "examples": ["breach Rule 5.4", "disqualification", "serious penalty", "group integrity"]
        }
    ]
    },
    {
        "id": "5.5",
        "title": "Practising During Round or While Play Is Stopped",
        "text": "While playing a hole, players must not make practice strokes at any ball. After completing a hole, players must not make practice strokes except putting/chipping on or near the completed hole's green, practice greens, or next tee area. While play is suspended, practice is restricted to outside the course or Committee-allowed areas.",
        "keywords": ["playing hole", "no practice strokes", "after completing hole", "putting chipping", "completed hole green", "practice greens", "next tee area", "play suspended", "outside course", "committee allowed"],
        "examples": [
            "practice stroke restrictions",
            "between holes practice",
            "suspended play practice",
            "allowed practice areas"
        ],
        "conditions": [
        {
            "situation": "No practice strokes while playing hole",
            "explanation": "Under Rule 5.5a, while playing a hole, a player must not make a practice stroke at any ball on or off the course.",
            "examples": ["playing a hole", "no practice stroke", "any ball", "on or off course"]
        },
        {
            "situation": "What are not practice strokes",
            "explanation": "Under Rule 5.5a, these are not practice strokes: practice swing with no intent to strike ball, hitting ball back to practice area or another player when done solely as courtesy, strokes made by player in playing out hole whose result has been decided.",
            "examples": ["practice swing no intent", "hitting back as courtesy", "playing out decided hole", "not practice strokes"]
        },
        {
            "situation": "Restriction after completing hole",
            "explanation": "Under Rule 5.5b, after completing play of a hole, but before making stroke to begin another hole, player must not make a practice stroke.",
            "examples": ["after completing hole", "before begin another", "must not practice stroke", "between holes"]
        },
        {
            "situation": "Exception for putting and chipping practice",
            "explanation": "Under Rule 5.5b Exception, player may practise putting or chipping on or near: putting green of hole just completed and any practice green, and teeing area of next hole. But practice strokes must not be made from bunker and must not unreasonably delay play.",
            "examples": ["putting chipping", "completed hole green", "practice green next tee", "not from bunker", "not delay play"]
        },
        {
            "situation": "Practice while play suspended",
            "explanation": "Under Rule 5.5c, while play is suspended or otherwise stopped under Rule 5.7a, player must not make practice stroke except: as allowed in Rule 5.5b, anywhere outside the course, and anywhere on course the Committee allows.",
            "examples": ["play suspended", "Rule 5.5b allowed", "outside the course", "committee allows"]
        },
        {
            "situation": "Match stopped by agreement",
            "explanation": "Under Rule 5.5c, if match is stopped by agreement of players and will not be resumed on same day, the players may practise on course without restriction before match is resumed.",
            "examples": ["stopped by agreement", "not resumed same day", "practise without restriction", "before resumed"]
        },
        {
            "situation": "Penalty for practice breach",
            "explanation": "Under Rule 5.5, penalty for breach of Rule 5.5: General Penalty. If breach happens between two holes, penalty applies to next hole.",
            "examples": ["general penalty", "between two holes", "applies next hole", "practice violation"]
        }
    ]
    },
    {
        "id": "5.6",
        "title": "Unreasonable Delay; Prompt Pace of Play",
        "text": "Players must not unreasonably delay play, either when playing a hole or between holes. Short delays may be allowed for certain reasons (seeking help, injury/illness, other good reason). Players should play at prompt pace throughout round. When it's their turn, recommended to make stroke in no more than 40 seconds. Penalties escalate: first breach one stroke, second breach general penalty, third breach disqualification.",
        "keywords": ["unreasonably delay", "playing hole", "between holes", "short delays allowed", "seeking help", "injury illness", "prompt pace", "40 seconds", "penalties escalate", "one stroke", "general penalty", "disqualification"],
        "examples": [
            "pace of play requirements",
            "reasonable delay allowances",
            "timing recommendations",
            "escalating penalties"
        ],
        "conditions": [
        {
            "situation": "Unreasonable delay prohibition",
            "explanation": "Under Rule 5.6a, a player must not unreasonably delay play, either when playing a hole or between two holes.",
            "examples": ["unreasonably delay", "playing hole", "between two holes", "prohibited"]
        },
        {
            "situation": "Allowed short delays",
            "explanation": "Under Rule 5.6a, player may be allowed short delay for certain reasons, such as: when player seeks help from referee or Committee, when player becomes injured or ill, or when there is another good reason.",
            "examples": ["short delay allowed", "seeks help referee", "injured or ill", "another good reason"]
        },
        {
            "situation": "Escalating penalties for delay",
            "explanation": "Under Rule 5.6a, penalty for first breach: One penalty stroke. Penalty for second breach: General Penalty. Penalty for third breach: Disqualification. If player unreasonably delays between two holes, penalty applies to next hole.",
            "examples": ["first = one stroke", "second = general penalty", "third = disqualification", "between holes = next hole"]
        },
        {
            "situation": "Prompt pace principle",
            "explanation": "Under Rule 5.6b, a round of golf is meant to be played at a prompt pace. Each player should recognize that their pace affects how long it will take other players to play their rounds, including both those in player's own group and those in following groups.",
            "examples": ["prompt pace", "affects other players", "own group", "following groups"]
        },
        {
            "situation": "Pace recommendations",
            "explanation": "Under Rule 5.6b(1), player should play at prompt pace throughout round, including time taken to: prepare for and make each stroke, move from one place to another between strokes, and move to next teeing area after completing hole. Player should prepare in advance and be ready to play when it's their turn.",
            "examples": ["prepare and make stroke", "move between strokes", "move to next tee", "prepare in advance"]
        },
        {
            "situation": "40-second recommendation",
            "explanation": "Under Rule 5.6b(1), when it is player's turn to play: recommended that player make stroke in no more than 40 seconds after they are (or should be) able to play without interference or distraction, and player should usually be able to play more quickly and is encouraged to do so.",
            "examples": ["40 seconds recommended", "without interference", "usually more quickly", "encouraged faster"]
        },
        {
            "situation": "Playing out of turn for pace",
            "explanation": "Under Rule 5.6b(2), depending on form of play, there are times when players may play out of turn to help pace: in match play, players may agree that one will play out of turn to save time; in stroke play, players may play 'ready golf' in safe and responsible way.",
            "examples": ["play out of turn", "match play agree", "save time", "ready golf safe"]
        },
        {
            "situation": "Committee pace policy",
            "explanation": "Under Rule 5.6b(3), to encourage and enforce prompt play, Committee should adopt Local Rule setting Pace of Play Policy. This Policy may set maximum time to complete round, hole or series of holes and stroke, and may set penalties for not following Policy.",
            "examples": ["committee pace policy", "local rule", "maximum time", "penalties for not following"]
        }
    ]
    },
    {
        "id": "5.7",
        "title": "Stopping Play; Resuming Play",
        "text": "During a round, players must not stop play except: Committee suspension (all must stop), agreement in match play (except if delays competition), or individual player stopping for lightning danger (must report to Committee). Committee suspensions are either immediate (must stop stroke immediately) or normal (different rules for between holes vs. playing hole). When resuming, players must be present and ready at designated time and location.",
        "keywords": ["must not stop", "committee suspension", "agreement match play", "lightning danger", "report committee", "immediate suspension", "normal suspension", "between holes", "playing hole", "resuming", "present ready", "designated time location"],
        "examples": [
            "play stoppage rules",
            "suspension types",
            "resumption procedures",
            "lightning safety"
        ],
        "conditions": [
        {
            "situation": "When players may or must stop",
            "explanation": "Under Rule 5.7a, during round, player must not stop play except: Committee suspension (all players must stop), stopping by agreement in match play (players may agree for any reason, except if delays competition), individual player stopping for lightning (may stop if reasonably believes danger, but must report to Committee as soon as possible).",
            "examples": ["committee suspension", "match play agreement", "lightning danger", "must report committee"]
        },
        {
            "situation": "Leaving course vs stopping play",
            "explanation": "Under Rule 5.7a, leaving the course is not, by itself, stopping play. A player's delay of play is covered by Rule 5.6a, not by this Rule.",
            "examples": ["leaving not stopping", "delay Rule 5.6a", "different concepts", "not this rule"]
        },
        {
            "situation": "Penalty for improper stopping",
            "explanation": "Under Rule 5.7a, if player stops play for any reason not allowed under this Rule or fails to report to Committee when required to do so, the player is disqualified.",
            "examples": ["reason not allowed", "fails to report", "disqualified", "serious penalty"]
        },
        {
            "situation": "Immediate suspension requirements",
            "explanation": "Under Rule 5.7b(1), if Committee declares immediate suspension of play, player must not make another stroke until Committee resumes play. Committee should use distinct method of telling players about immediate suspension.",
            "examples": ["immediate suspension", "not make another stroke", "until committee resumes", "distinct method"]
        },
        {
            "situation": "Normal suspension between holes",
            "explanation": "Under Rule 5.7b(2), if Committee suspends play for normal reasons: between two holes, if all players in group are between holes, they must stop play and must not make stroke to begin another hole until Committee resumes play.",
            "examples": ["normal suspension", "between two holes", "all players between", "not begin another hole"]
        },
        {
            "situation": "Normal suspension while playing hole",
            "explanation": "Under Rule 5.7b(2), if Committee suspends for normal reasons: while playing hole, if any player in group has started hole, players may choose either to stop play or to play out hole. Players allowed brief time (normally no more than two minutes) to decide. May complete hole or stop before completing.",
            "examples": ["any player started", "choose stop or play out", "two minutes decide", "complete or stop before"]
        },
        {
            "situation": "Disagreement during normal suspension",
            "explanation": "Under Rule 5.7b(2), if players do not agree on what to do: Match Play - if opponent stops, player must also stop and both must not play until Committee resumes (if player doesn't stop, gets general penalty); Stroke Play - any player may choose to stop or continue, except may continue only if marker stays to keep score.",
            "examples": ["match play opponent stops", "both must stop", "stroke play any choose", "marker stays for score"]
        },
        {
            "situation": "Penalty for suspension breach",
            "explanation": "Under Rule 5.7b, penalty for breach of Rule 5.7b: Disqualification. Exception: no penalty if Committee decides that failure to stop was justified.",
            "examples": ["breach = disqualification", "committee decides justified", "failure to stop", "exception applies"]
        },
        {
            "situation": "Where to resume play",
            "explanation": "Under Rule 5.7c(1), player must resume play from where they stopped play on hole or, if between two holes, at next teeing area, even if play is resumed on later day. If resumes from different spot, see Rules 6.1b and 14.7.",
            "examples": ["where stopped play", "between holes = next tee", "even later day", "different spot see other rules"]
        },
        {
            "situation": "When to resume play",
            "explanation": "Under Rule 5.7c(2), player must be present at location and ready to play: at time set by Committee for play to resume, and must resume at (not before) that time. If ability to resume delayed (players ahead need to move), no breach if present and ready when group able to resume.",
            "examples": ["present and ready", "time set by committee", "at not before", "ahead players delayed"]
        },
        {
            "situation": "Penalty for late resumption",
            "explanation": "Under Rule 5.7c(2), penalty for breach: Disqualification. Exceptions 1, 2 and 3 in Rule 5.3a and Exception to Rule 5.7b apply here as well.",
            "examples": ["breach = disqualification", "exceptions from 5.3a", "exception from 5.7b", "similar to starting"]
        },
        {
            "situation": "Lifting ball when play stops",
            "explanation": "Under Rule 5.7d(1), when stopping play under this Rule, player may mark spot of ball and lift ball. When resuming: if ball was lifted, must replace original or another ball on original spot; if ball was not lifted, may play as lies or may mark, lift and replace original or another ball on original spot.",
            "examples": ["may mark and lift", "lifted = replace", "not lifted = play as lies", "original or another ball"]
        },
        {
            "situation": "Lie altered during stoppage",
            "explanation": "Under Rule 5.7d(1), if lie of ball altered as result of lifting, must replace under Rule 14.2d. If lie altered after lifted and before replaced, Rule 14.2d doesn't apply: must replace on original spot, but if lie or conditions worsened during this time, Rule 8.1d applies.",
            "examples": ["altered from lifting", "Rule 14.2d", "altered after lifted", "worsened = Rule 8.1d"]
        },
        {
            "situation": "Ball or marker moved while stopped",
            "explanation": "Under Rule 5.7d(2), if player's ball or ball-marker moved in any way before play resumes (including by natural forces), player must either: replace original or another ball on original spot, or place ball-marker to mark original spot and then replace ball on that spot.",
            "examples": ["moved any way", "including natural forces", "replace on original", "mark then replace"]
        },
        {
            "situation": "Penalty for wrong place from stoppage",
            "explanation": "Under Rule 5.7d, penalty for playing ball from wrong place in breach of Rule 5.7d: General Penalty Under Rule 14.7a.",
            "examples": ["wrong place", "general penalty", "Rule 14.7a", "two strokes or loss hole"]
        }
    ]
    },

    # --- Section 6: Playing a Hole ---
    {
        "id": "6.1a",
        "title": "When Hole Starts",
        "text": "A player has started a hole when they make a stroke to begin the hole. The hole has started even if the stroke was made from outside the teeing area or the stroke was cancelled under a Rule.",
        "keywords": ["hole starts", "beginning hole", "first stroke", "stroke to begin", "cancelled stroke", "hole timing"],
        "conditions": [
        {
            "situation": "Player makes stroke to begin hole",
            "explanation": "Under Rule 6.1a, hole officially starts with the first stroke attempt, regardless of outcome or location.",
            "examples": [
              "Player swings and misses the ball completely - hole has started",
              "Player hits ball from wrong tee markers - hole has started", 
              "Player's stroke is later cancelled by opponent - hole had started when stroke was made"
            ]
        },
        {
            "situation": "Stroke made from outside teeing area",
            "explanation": "Under Rule 6.1a, hole begins even when first stroke is made from incorrect location, though penalties may apply under Rule 6.1b.",
            "examples": [
              "Player accidentally tees off from forward tees - hole has started",
              "Player hits from behind tee markers - hole has started but stroke may be cancelled/penalized"
            ]
        },
        {
            "situation": "Stroke cancelled under a Rule",
            "explanation": "Under Rule 6.1a, even if stroke is later cancelled or ruled invalid, the hole had begun when stroke was attempted.",
            "examples": [
              "Match play opponent cancels stroke from wrong teeing area - hole had started",
              "Stroke cancelled due to advice penalty - hole timing unaffected"
            ]
        }
    ]
    },
    {
        "id": "6.1b",
        "title": "Ball Must Be Played from Inside Teeing Area",
        "text": "A player must start each hole by playing a ball from anywhere inside the teeing area. Different procedures apply in match play vs stroke play when this rule is breached.",
        "keywords": ["teeing area", "wrong tee", "outside teeing area", "match play cancellation", "stroke play penalty", "tee markers", "correct mistake"],
        "conditions": [
        {
            "situation": "Match play - opponent may cancel stroke from outside teeing area",
            "explanation": "Under Rule 6.1b(1), there is no penalty in match play, but opponent may cancel stroke promptly before either player makes another stroke. Cancellation cannot be withdrawn, and the player must replay from the correct teeing area.",
            "examples": [
              "Player tees off from championship tees instead of member tees - opponent can cancel in which case the player's stroke does not count and must rehit from the correct teeing area",
              "Player hits from 2 yards behind tee markers - opponent has option to cancel, in which case the player's stroke does not count and must rehit from the correct teeing area",
              "If opponent doesn't cancel immediately, stroke counts and ball is in play"
            ]
        },
        {
            "situation": "Stroke play - general penalty and mandatory correction",
            "explanation": "Under Rule 6.1b(2), player gets 2-stroke penalty and must correct by playing from inside teeing area. Original ball not in play.",
            "examples": [
              "Player tees off from wrong tees: 2-stroke penalty + replay from correct tee",
              "Player hits from in front of tee markers: penalty + must replay",
              "Failing to correct before next hole results in disqualification"
            ]
        },
        {
            "situation": "Consequences of not correcting mistake",
            "explanation": "Under Rule 6.1b(2), in stroke play, player must correct before starting next hole or returning scorecard, or face disqualification.",
            "examples": [
              "Player realizes mistake on next tee but hasn't corrected - must return and correct",
              "Player realizes mistake after hitting tee shot on the next hole - disqualified",
              "Player finishes round without correcting tee shot error - disqualified",
              "Committee discovers error after round completion - disqualification stands"
            ]
        }
    ]
    },
    {
        "id": "6.2a",
        "title": "When Teeing Area Rules Apply",
        "text": "The teeing area Rules in Rule 6.2b apply whenever a player is required or allowed to play a ball from the teeing area.",
        "keywords": ["teeing area rules", "when apply", "required to play", "allowed to play", "starting hole", "playing again", "relief"],
        "conditions": [
        {
            "situation": "Starting play of the hole",
            "explanation": "Under Rule 6.2a, teeing area rules apply when the player is starting play of the hole from the teeing area.",
            "examples": [
              "First stroke of any hole - teeing area rules apply",
              "Player teeing off on hole 1 - Rule 6.2b applies",
              "Starting a par 3 from the tee - teeing area rules in effect"
            ]
        },
        {
            "situation": "Playing again from teeing area under a Rule",
            "explanation": "Under Rule 6.2a and Rule 14.6, teeing area rules apply when a player will play again from the teeing area under a Rule.",
            "examples": [
              "Ball goes out of bounds, taking stroke-and-distance from tee - teeing area rules apply",
              "Ball unplayable, choosing to replay from tee - Rule 6.2b applies",
              "Lost ball, returning to tee under stroke-and-distance - teeing area rules in effect"
            ]
        },
        {
            "situation": "Ball in play in teeing area after stroke or relief",
            "explanation": "Under Rule 6.2a, teeing area rules apply when the player's ball is in play in the teeing area after a stroke or after taking relief.",
            "examples": [
              "Tee shot hits tree and bounces back into teeing area - teeing area rules apply",
              "After taking relief, ball is dropped in teeing area - Rule 6.2b applies",
              "Ball barely advances and remains in teeing area - teeing area rules still apply"
            ]
        },
        {
            "situation": "Applies only to correct teeing area",
            "explanation": "Under Rule 6.2a, this Rule applies only to the teeing area the player must play from for the hole being played, not other teeing locations.",
            "examples": [
              "Playing from member tees - only member tee rules apply, not championship tees",
              "Ball near different hole's tee markers - those markers treated as obstructions",
              "Wrong set of tees for same hole - not the applicable teeing area"
            ]
        }
    ]
    },
    {
        "id": "6.2b",
        "title": "Teeing Area Rules",
        "text": "Specific rules that apply whenever a player is required or allowed to play from the teeing area, including ball position, tee usage, and improvement of conditions.",
        "keywords": ["teeing area", "ball position", "tee placement", "ground", "improving conditions", "tee markers", "ball in play", "conforming tee"],
        "conditions": [
        {
            "situation": "Ball position in teeing area",
            "explanation": "Under Rule 6.2b(1), ball is in teeing area when any part touches or is above any part of the teeing area. Player may stand outside while striking ball inside.",
            "examples": [
              "Ball on tee with half the ball behind tee line - ball is in teeing area",
              "Player stands outside tee markers but ball is properly teed - this is legal",
              "Ball entirely in front of or behind tee markers - not in teeing area"
            ]
        },
        {
            "situation": "Tee and ground placement requirements",
            "explanation": "Under Rule 6.2b(2), ball must be played from conforming tee placed in/on ground, or from ground itself. Non-conforming tees penalized.",
            "examples": [
              "Ball teed on wooden or plastic conforming tee - legal",
              "Ball placed directly on ground or sand mound - legal", 
              "Ball balanced on bottle cap or non-conforming device - general penalty",
              "Using non-conforming tee twice in round - disqualification"
            ]
        },
        {
            "situation": "Improving conditions in teeing area",
            "explanation": "Under Rule 6.2b(3), player may alter surface, move/bend/break natural objects, remove/press sand and soil, remove dew/frost/water before stroke.",
            "examples": [
              "Pressing down grass behind ball or making divot with club - allowed",
              "Breaking tree branch hanging over teeing area - allowed",
              "Removing leaves, sand, or water from teeing area - allowed",
              "Moving immovable obstruction like sprinkler head - still not allowed"
            ]
        },
        {
            "situation": "Tee-markers and missing markers",
            "explanation": "Under Rule 6.2b(4), general penalty for moving tee-markers to improve conditions. If missing, seek Committee help or estimate location.",
            "examples": [
              "Moving tee-marker to get better angle for tee shot - general penalty",
              "Tee-marker missing due to maintenance - estimate area and proceed",
              "Moving tee-marker as obstruction when ball is elsewhere on course - allowed"
            ]
        },
        {
            "situation": "Ball not in play until stroke made",
            "explanation": "Under Rule 6.2b(5), ball may be lifted/moved without penalty before stroke. Once stroke attempted, ball is in play regardless of outcome.",
            "examples": [
              "Teed ball falls off in wind - re-tee anywhere without penalty",
              "Player accidentally knocks ball off tee - re-tee without penalty",
              "Player swings and misses - ball is now in play where it lies",
              "Player hits ball while falling off tee - stroke counts, ball in play"
            ]
        },
        {
            "situation": "Ball in play returns to teeing area",
            "explanation": "Under Rule 6.2b(6), if ball in play ends up in teeing area after stroke/relief, player may lift/move without penalty and play from anywhere in teeing area.",
            "examples": [
              "Tee shot hits tree and bounces back into teeing area - can re-tee or play as lies",
              "After unplayable ball relief, ball dropped in teeing area - can re-tee",
              "Ball barely moves forward after stroke, stays in teeing area - can pick up and re-tee"
            ]
        }
    ]
    },
    {
        "id": "6.3a",
        "title": "Holing Out with Same Ball Played from Teeing Area",
        "text": "A player must hole out with the same ball played from the teeing area, except when that ball is lost/out of bounds or the player substitutes another ball.",
        "keywords": ["same ball", "holing out", "ball identification", "lost ball", "out of bounds", "ball substitution", "completing hole"],
        "conditions": [
        {
            "situation": "Same ball requirement throughout hole",
            "explanation": "Under Rule 6.3a, ball integrity maintained from tee to completion unless specific circumstances require or allow substitution.",
            "examples": [
              "Ball played from tee to green and holed - proper completion",
              "Ball lost in water hazard, new ball played under penalty - allowed substitution",
              "Player finds ball has crack mid-hole - may substitute only if unfit for play"
            ]
        },
        {
            "situation": "Exceptions allowing different ball at hole completion",
            "explanation": "Under Rule 6.3a, original ball no longer required when lost, out of bounds, or legitimately substituted under Rules.",
            "examples": [
              "Ball lost in rough, stroke-and-distance taken - hole out with substituted ball",
              "Ball goes out of bounds - must use different ball",
              "Ball damaged during play and unfit - may substitute and hole out with new ball"
            ]
        },
        {
            "situation": "Ball identification importance",
            "explanation": "Under Rule 6.3a and Rule 7.2, player should mark ball for identification to avoid wrong ball situations and ensure same ball completion.",
            "examples": [
              "Player marks ball with initials before teeing off",
              "Two identical balls found near each other - identification marks help determine correct ball",
              "Unmarked ball creates uncertainty about which ball belongs to which player"
            ]
        }
    ]
    },
    {
        "id": "6.3b",
        "title": "Substitution of Another Ball While Playing Hole",
        "text": "Certain Rules allow ball substitution during a hole while others require using the original ball. Understanding when substitution is permitted is crucial.",
        "keywords": ["ball substitution", "original ball", "relief", "dropping", "placing", "replacing", "ball in play", "incorrectly substituted"],
        "conditions": [
        {
            "situation": "When substitution is allowed",
            "explanation": "Under Rule 6.3b(1), may substitute when taking relief (dropping/placing) or playing again from previous stroke location, but not when replacing ball on spot.",
            "examples": [
              "Taking relief from cart path - may use original ball or substitute",
              "Playing again after lost ball - may use original ball or substitute", 
              "Ball won't stay in relief area when dropped - may substitute when placing"
            ]
        },
        {
            "situation": "When substitution is not allowed",
            "explanation": "Under Rule 6.3b(1), when replacing ball on a spot, must use original ball except in specific circumstances outlined in Rule 14.2a.",
            "examples": [
              "Replacing ball moved by outside agency - must use original ball",
              "Replacing ball marked to avoid interference with another player's swing - must replace same ball",
              "Ball lifted to clean on green - must replace same ball",
              "Ball mark repaired and ball replaced - original ball required"
            ]
        },
        {
            "situation": "Substituted ball becomes ball in play",
            "explanation": "Under Rule 6.3b(2), once substituted, original ball no longer in play even if substitution was incorrect. Must continue with substituted ball.",
            "examples": [
              "Player takes stroke-and-distance, finds original ball - continue with substituted ball",
              "Player incorrectly substitutes ball - penalty applies but continue with substituted ball",
              "Original ball found after search time expired - too late, play substituted ball"
            ]
        },
        {
            "situation": "Incorrectly substituted ball penalty",
            "explanation": "Under Rule 6.3b(3), one penalty stroke when playing incorrectly substituted ball, but must continue with that ball for remainder of hole.",
            "examples": [
              "Player substitutes ball when replacing on green - 1 stroke penalty, continue with new ball",
              "Player uses different ball when not taking relief - penalty, complete hole with that ball"
            ]
        }
    ]
    },
    {
        "id": "6.3c",
        "title": "Wrong Ball",
        "text": "A player must not make a stroke at a wrong ball. Penalties and procedures differ between match play and stroke play.",
        "keywords": ["wrong ball", "hit wrong ball", "played wrong ball", "another player hit my ball", "I hit another player's ball", "hit someone else's ball", "someone else hit my ball", "match play", "stroke play", "loss of hole", "penalty strokes", "moving in water", "another player", "correct mistake"],
        "conditions": [
        {
            "situation": "Wrong ball penalties in match play",
            "explanation": "Under Rule 6.3c(1), general penalty (loss of hole) in match play. If both players play each other's balls, first to play wrong ball loses hole.",
            "examples": [
              "Player hits opponent's ball - loses hole immediately",
              "Both players hit each other's balls - first to do so loses hole",
              "Unknown which wrong ball played first - no penalty, and hole must be played out with the exchanged balls"
            ]
        },
        {
            "situation": "Wrong ball penalties in stroke play",
            "explanation": "Under Rule 6.3c(1), two penalty strokes and must correct by playing original ball. Must correct before next hole or face disqualification.",
            "examples": [
              "Player hits wrong ball - 2 strokes, must find and play original ball",
              "Wrong ball strokes don't count toward score",
              "Must correct before starting next hole or be disqualified"
            ]
        },
        {
            "situation": "Wrong ball moving in water exception",
            "explanation": "Exception under Rule 6.3c(1): No penalty if wrong ball struck is moving in penalty area water or temporary water. Stroke doesn't count, must correct.",
            "examples": [
              "Ball moving in stream in penalty area - no penalty if wrong ball hit",
              "Ball floating in temporary water puddle - exception applies",
              "Ball at rest in water - normal wrong ball penalties apply"
            ]
        },
        {
            "situation": "Player's ball played by another as wrong ball",
            "explanation": "Under Rule 6.3c(2), when another player plays your ball by mistake, you replace your ball on original spot without penalty.",
            "examples": [
              "Another player hits your ball from rough - replace on original spot",
              "Your ball hit by other player and lost - replace another ball on estimated spot",
              "Ball played from green by mistake - replace regardless of outcome"
            ]
        }
    ]
    },
    {
        "id": "6.4a",
        "title": "Order of Play - Match Play",
        "text": "Order of play rules in match play, including honour system and procedures when players play out of turn.",
        "keywords": ["order of play", "match play", "honour", "out of turn", "cancel stroke", "farther from hole", "agreement", "random method"],
        "conditions": [
        {
            "situation": "Determining honour and order",
            "explanation": "Under Rule 6.4a(1), first hole by draw/agreement/random method. Winner of hole has honour. Ball farther from hole plays first during hole.",
            "examples": [
              "Player wins hole 1, has honour on hole 2 tee",
              "Hole is tied, player who had honour keeps it for next hole",
              "Player A 150 yards out, Player B 100 yards - Player A plays first",
              "Balls equidistant - decide by agreement or random method"
            ]
        },
        {
            "situation": "Playing out of turn consequences",
            "explanation": "Under Rule 6.4a(2), no penalty but opponent may cancel stroke promptly. Cannot cancel if agreed to out-of-turn play or waited too long.",
            "examples": [
              "Player plays out of turn - opponent can cancel before either's next stroke",
              "Players agree to play out of turn for time - opponent cannot cancel",
              "Opponent says 'go ahead' then changes mind - cannot cancel, gave up right"
            ]
        },
        {
            "situation": "Cancellation procedures",
            "explanation": "Under Rule 6.4a(2), cancellation must be prompt and before next stroke by either player. Once cancelled, cannot be withdrawn.",
            "examples": [
              "Opponent immediately says 'I cancel that stroke' - valid cancellation",
              "Opponent waits until after seeing result - too late to cancel",
              "Opponent cancels then changes mind - cancellation stands"
            ]
        }
    ]
    },
    {
        "id": "6.4b",
        "title": "Order of Play - Stroke Play",
        "text": "Order of play in stroke play, including honour system and ready golf provisions.",
        "keywords": ["order of play", "stroke play", "honour", "ready golf", "out of turn", "lowest score", "farther from hole", "advantage"],
        "conditions": [
        {
            "situation": "Normal order determination",
            "explanation": "Under Rule 6.4b(1), honour based on lowest gross score. Ball farthest from hole should play first. No penalty for playing out of turn.",
            "examples": [
              "Player shoots 4, others shoot 5 - player with 4 has honour",
              "Two players tie with 4s - maintain same order as previous hole",
              "Player plays out of turn accidentally - no penalty, continue",
              "Agreement to play out of turn for advantage - 2-stroke penalty for all involved"
            ]
        },
        {
            "situation": "Ready golf provisions",
            "explanation": "Under Rule 6.4b(2), players encouraged to play out of turn safely when ready, often called 'ready-golf', unless player whose turn it is wants to play first.",
            "examples": [
              "Player ready with short putt while others walking to balls - may putt out",
              "Player ready with approach while others searching - may play if safe",
              "Player whose turn it is says they want to play first - others should wait",
              "Playing out of turn when endangering/distracting others - inappropriate"
            ]
        },
        {
            "situation": "Prohibited agreements for advantage",
            "explanation": "Under Rule 6.4b(1), players cannot agree to play out of turn specifically to give one player an advantage over others in the competition.",
            "examples": [
              "Agreement to let player play first to see line for putt - penalty",
              "Playing out of turn to help read green conditions - penalty",
              "Convenience-based out-of-turn play - allowed"
            ]
        }
    ]
    },
    {
        "id": "6.4c",
        "title": "Playing Provisional Ball or Another Ball from Teeing Area",
        "text": "Special order of play rules when players need to play provisional balls or additional balls from the teeing area.",
        "keywords": ["provisional ball", "teeing area", "order of play", "all players", "first stroke", "multiple provisional"],
        "conditions": [
        {
            "situation": "Provisional ball from teeing area order",
            "explanation": "Under Rule 6.4c, all other players complete their first strokes before player plays provisional from tee. Multiple provisionals follow same order.",
            "examples": [
              "Player A's ball might be lost - Players B, C, D hit first, then A plays provisional",
              "Two players need provisionals - play provisionals in same order as original shots",
              "Player decides on provisional after others hit - others don't need to wait"
            ]
        },
        {
            "situation": "Another ball from teeing area procedures",
            "explanation": "Under Rule 6.4c, when playing another ball from tee (not provisional), same order rules apply as for provisional balls.",
            "examples": [
              "Player taking stroke-and-distance from tee - others play first",
              "Ball unplayable, returning to tee - wait for others to complete first shots"
            ]
        }
    ]
    },
    {
        "id": "6.4d",
        "title": "Order When Taking Relief or Playing Provisional Ball",
        "text": "Order of play when players are taking relief or playing provisional balls from locations other than the teeing area.",
        "keywords": ["relief", "provisional ball", "order of play", "stroke and distance", "previous stroke", "original ball location"],
        "conditions": [
        {
            "situation": "Taking relief order priority",
            "explanation": "Under Rule 6.4d(1), order depends on type of relief. Stroke-and-distance based on previous stroke location; other relief based on original ball location.",
            "examples": [
              "Ball lost, taking stroke-and-distance - order based on where last stroke played",
              "Ball in penalty area, dropping - order based on where ball entered penalty area",
              "Taking relief from cart path - order based on where original ball lies"
            ]
        },
        {
            "situation": "Provisional ball order from other locations",
            "explanation": "Under Rule 6.4d(2), provisional ball played immediately after stroke that might result in lost ball, before others play.",
            "examples": [
              "Ball might be lost in trees - play provisional immediately after that stroke",
              "Waiting to see if ball is lost - provisional played when decision made",
              "Other players continue normal order after provisional is played"
            ]
        }
    ]
    },
    {
        "id": "6.5",
        "title": "Completing Play of a Hole",
        "text": "When a hole is considered complete in match play vs stroke play, and what happens if a player continues playing after completion.",
        "keywords": ["completing hole", "hole complete", "holing out", "match play", "stroke play", "conceded", "continuing play"],
        "conditions": [
        {
            "situation": "Match play completion criteria",
            "explanation": "Under Rule 6.5, in match play, hole complete when ball holed, next stroke conceded, or hole result decided through concession or penalty.",
            "examples": [
              "Ball holed or opponent says 'that's good' - hole complete",
              "Opponent concedes hole after bad shot - hole complete",
              "Player gets general penalty (loss of hole) - hole complete"
            ]
         },
        {
            "situation": "Stroke play completion criteria",
            "explanation": "Under Rule 6.5, in stroke play, must actually hole ball under Rule 3.3c. More restrictive than match play.",
            "examples": [
              "Ball must physically go in hole - no concessions in stroke play",
              "Player picks up ball before holing - hole not completed",
              "Must complete every hole unless specific rule provides exception"
            ]
        },
        {
            "situation": "Continuing play after completion",
            "explanation": "Under Rule 6.5, if player doesn't know hole is complete and continues, no penalty for practice or playing additional balls.",
            "examples": [
              "Player doesn't realize hole was conceded, keeps playing - no penalty",
              "Player continues after holing out, thinking they missed - no penalty for extra strokes",
              "Play after completion not considered practice round violation"
            ]
        }
    ]
    },

    # --- Section 7: Ball Search ---
    {
        "id": "7.1a",
        "title": "Player May Take Reasonable Actions to Find and Identify Ball",
        "text": "A player is responsible for finding their ball in play after each stroke. The player may fairly search for the ball by taking reasonable actions to find and identify it.",
        "keywords": ["ball search", "reasonable actions", "find ball", "identify ball", "fair search", "moving sand", "moving water", "bending grass", "tree branches"],
        "conditions": [
          {
            "situation": "Player responsibility for finding ball",
            "explanation": "Under Rule 7.1a, a player is responsible for finding their ball in play after each stroke and may take reasonable actions to search.",
            "examples": [
              "Ball hit into rough area - player must search for their own ball",
              "Ball may be in bushes - player can move branches to look for ball",
              "Ball potentially under leaves - player can move natural debris to search"
            ]
      },
      {
            "situation": "Reasonable actions allowed during search",
            "explanation": "Under Rule 7.1a, player may move sand and water, move or bend grass, bushes, tree branches and other natural objects, including breaking them if result of reasonable search actions.",
            "examples": [
              "Moving sand with hands or feet to find buried ball - allowed",
              "Bending tree branches back to look underneath - allowed",
              "Breaking small branch while searching that gets in the way - allowed if reasonable",
              "Deliberately breaking large branches to improve lie - not allowed, exceeds reasonable search"
            ]
      },
      {
            "situation": "Improvement to conditions affecting stroke",
            "explanation": "Under Rule 7.1a and Rule 8.1a, no penalty if improvement results from fair search, but general penalty if actions exceeded what was reasonable for search.",
            "examples": [
              "Searching moves grass that happened to improve lie - no penalty",
              "Breaking branches while searching accidentally improves swing path - no penalty",
              "Excessive clearing beyond what's needed to find ball - general penalty",
              "Using search as excuse to improve playing conditions - penalty under Rule 8.1a"
            ]
      },
      {
            "situation": "Removing impediments and obstructions during search",
            "explanation": "Under Rule 7.1a, Rule 15.1 and Rule 15.2, player may remove loose impediments and movable obstructions while trying to find and identify ball.",
            "examples": [
              "Moving loose stones, pine straw, and leaves while searching - allowed under Rule 15.1",
              "Moving rake or towel that might be covering ball - allowed under Rule 15.2",
              "Removing pine cones and twigs during search - allowed",
              "Cannot remove growing or attached natural objects beyond reasonable search actions"
            ]
      }
    ]
    },
    {
        "id": "7.1b",
        "title": "Sand Affecting Lie Moved During Search",
        "text": "What to do if sand affecting the lie of player's ball is moved while trying to find or identify it.",
        "keywords": ["sand", "original lie", "re-create lie", "covered by sand", "visible ball", "bunker search"],
        "conditions": [
      {
            "situation": "Re-creating original lie in sand",
            "explanation": "Under Rule 7.1b, player must re-create the original lie in sand, but may leave a small part of the ball visible if ball had been covered by sand.",
            "examples": [
              "Ball buried in bunker sand, sand moved during search - must re-create original buried lie",
              "Ball partially covered by sand, some sand removed while searching - recreate lie but may leave bit visible",
              "Ball completely covered, found during search - must re-bury but small part may show"
            ]
      },
      {
            "situation": "Penalty for not re-creating lie",
            "explanation": "Under Rule 7.1b, if player plays ball without having re-created the original lie in sand, player gets the general penalty.",
            "examples": [
              "Player finds buried ball but plays it from improved lie - general penalty",
              "Ball was covered, player plays it sitting on top of sand - penalty",
              "Must re-create lie before playing, even if worse than current position"
            ]
      }
    ]
    },
    {
        "id": "7.2",
        "title": "How to Identify Ball",
        "text": "A player's ball at rest may be identified in specific ways to ensure the correct ball is being played.",
        "keywords": ["identify ball", "identifying mark", "brand model number", "ball identification", "same area", "provisional ball", "original ball"],
        "conditions": [
      {
            "situation": "Identification by seeing ball come to rest",
            "explanation": "Under Rule 7.2, ball may be identified by the player or anyone else seeing a ball come to rest in circumstances where it is known to be the player's ball.",
            "examples": [
              "Player watches their ball land in specific bush - can identify by location",
              "Caddie or playing partner sees where ball went - valid identification",
              "Ball seen rolling into water hazard at specific spot - known to be player's ball"
            ]
      },
      {
            "situation": "Identification by player's marking",
            "explanation": "Under Rule 7.2 and Rule 6.3a, ball identified by seeing player's identifying mark, but not if identical marked ball also found in same area.",
            "examples": [
              "Player finds ball with their initials 'JD' - valid identification",
              "Ball marked with unique symbol or design - can identify by mark",
              "Two identical balls with same markings found together - cannot identify by mark alone",
              "Player's distinctive dot pattern on ball - valid identification method"
            ]
      },
      {
            "situation": "Identification by brand, model, number and condition",
            "explanation": "Under Rule 7.2, ball identified by finding same brand, model, number and condition in expected area, but not if identical ball in same area without way to distinguish.",
            "examples": [
              "Titleist Pro V1 #3 with scuff mark found where expected - valid identification",
              "Ball brand and number match, found in rough where shot went - can identify",
              "Two identical unmarked balls found together - cannot determine which is player's",
              "Same ball type but different condition (one scuffed, one new) - can distinguish"
            ]
      },
      {
            "situation": "Provisional ball identification issues",
            "explanation": "Under Rule 7.2 and Rule 18.3c(2), if provisional ball cannot be distinguished from original ball, specific procedures apply.",
            "examples": [
              "Both original and provisional are identical unmarked balls - see Rule 18.3c(2)",
              "Player uses identical balls for original and provisional - identification problems",
              "Should use different balls or mark them to avoid confusion"
            ]
      }
    ]
    },
    {
        "id": "7.3",
        "title": "Lifting Ball to Identify It",
        "text": "If a ball might be a player's ball but cannot be identified as it lies, specific procedures allow lifting for identification.",
        "keywords": ["lifting ball", "mark spot", "identify", "rotate ball", "clean ball", "putting green", "replace ball", "reasonably necessary"],
        "conditions": [
      {
            "situation": "Procedures for lifting to identify",
            "explanation": "Under Rule 7.3 and Rule 14.1, player may lift ball to identify it (including rotating), but must mark spot first and not clean more than needed (except on putting green).",
            "examples": [
              "Ball face-down, can't see markings - may lift and rotate to see identification",
              "Ball covered in mud, markings not visible - may clean just enough to identify",
              "Must place marker before lifting ball for identification",
              "On putting green - may lift and clean fully under Rule 13.1b"
            ]
      },
      {
            "situation": "Replacing ball after identification",
            "explanation": "Under Rule 7.3 and Rule 14.2, if lifted ball is the player's ball or another player's ball, it must be replaced on its original spot.",
            "examples": [
              "Ball lifted for identification turns out to be player's ball - must replace on original spot",
              "Ball lifted belongs to different player - still must replace where found",
              "Ball is not player's ball and not another player's ball - ball is lost, may not replace"
            ]
      },
      {
            "situation": "Penalties for improper lifting procedures",
            "explanation": "Under Rule 7.3, one penalty stroke if lifting when not reasonably necessary (except putting green), failing to mark spot, or cleaning when not allowed.",
            "examples": [
              "Ball clearly identifiable but player lifts anyway - one penalty stroke",
              "Lifting ball without marking spot first - penalty",
              "Cleaning ball more than necessary for identification - penalty",
              "On putting green, lifting is allowed under Rule 13.1b without penalty"
            ]
      }
    ]
    },
    {
        "id": "7.4",
        "title": "Ball Accidentally Moved in Trying to Find or Identify It",
        "text": "There is no penalty if the player's ball is accidentally moved while trying to find or identify it, but the ball must be replaced.",
        "keywords": ["accidentally moved", "no penalty", "replace ball", "original spot", "reasonable actions", "immovable obstruction", "sand lie", "search actions"],
        "conditions": [
      {
            "situation": "No penalty for accidental movement during search",
            "explanation": "Under Rule 7.4, no penalty if player's ball accidentally moved by player, opponent or anyone else while trying to find or identify it.",
            "examples": [
              "Ball moves when stepping near it while searching - no penalty",
              "Ball falls out of tree when shaking branches to search - no penalty, accidental movement",
              "Sweeping feet through grass to find ball causes it to move - no penalty if reasonable search",
              "Ball moves when moving sand or water during search - accidental, no penalty"
            ]
      },
      {
            "situation": "Penalty for causing movement before search begins",
            "explanation": "Under Rule 7.4 and Rule 9.4b, if player causes ball to move before starting to search for the ball, player gets one penalty stroke.",
            "examples": [
              "Player steps on ball before starting search - one penalty stroke",
              "Ball moved by player's actions before beginning to look for it - penalty applies",
              "Movement must occur during actual search process to avoid penalty"
            ]
      },
      {
            "situation": "Definition of accidentally includes reasonable search actions",
            "explanation": "Under Rule 7.4, 'accidentally' includes when ball moved by reasonable search actions likely to reveal ball's location, such as sweeping feet through grass or shaking tree.",
            "examples": [
              "Sweeping feet through long grass in systematic search - accidental if ball moves",
              "Shaking tree branch to see if ball falls out - accidental movement",
              "Moving through rough area where ball likely to be - reasonable search actions",
              "Deliberately trying to move ball is not accidental - would be penalty"
            ]
      },
      {
            "situation": "Replacing ball in original position",
            "explanation": "Under Rule 7.4 and Rule 14.2, ball must be replaced on original spot (estimated if unknown), including specific rules for obstructions and sand lies.",
            "examples": [
              "Ball was against tree trunk when moved - replace against tree in original spot",
              "Ball was under bush when found - replace under bush where it was",
              "Ball was buried in sand - re-create original lie, may leave small part visible",
              "Ball was on cart path when moved - replace on path in original position"
            ]
      },
      {
            "situation": "Special replacement rules for sand and obstructions",
            "explanation": "Under Rule 7.4, Rule 14.2c and Rule 14.2d(1), special rules apply when replacing ball that was on/under obstructions or covered by sand.",
            "examples": [
              "Ball was under immovable obstruction - replace under obstruction",
              "Ball against boundary fence when moved - replace against fence",
              "Ball covered by sand in bunker - recreate original lie, may leave small part visible",
              "Ball was buried in sand outside bunker - must recreate buried lie"
            ]
      }
      ]
      },
   

    # --- Section 8: Course Played as It Is Found ---

      {
        "id": "8.1a",
        "title": "Actions That Are Not Allowed",
        "text": "Except in limited ways allowed in Rules 8.1b, c and d, a player must not take actions that improve the conditions affecting the stroke.",
        "keywords": ["improve conditions", "not allowed", "bend or break growing objects", "move immovable obstruction", "boundary object", "tee-markers", "move into position", "alter surface", "divots", "sand soil", "dew frost water"],
        "conditions": [
          {
            "situation": "Moving, bending or breaking objects",
            "explanation": "Under Rule 8.1a(1), player must not move, bend or break growing/attached natural objects, immovable obstructions, integral objects, boundary objects, or tee-markers when playing from that teeing area.",
            "examples": [
              "Bending tree branch that interferes with swing - not allowed, general penalty",
              "Moving boundary stake that's in line of play - prohibited",
              "Breaking off dead branch hanging in swing path - not allowed",
              "Moving tee-marker to improve stance on tee - general penalty"
            ]
      },
      {
            "situation": "Moving objects into position",
            "explanation": "Under Rule 8.1a(2), player must not move loose impediment or movable obstruction into position to build stance or improve line of play.",
            "examples": [
              "Stacking stones to create level stance - not allowed",
              "Moving bench or cart to block wind - prohibited",
              "Placing towel on ground to kneel on for shot - not allowed to improve stance",
              "Building up area with loose impediments - general penalty"
            ]
      },
      {
            "situation": "Altering surface of ground",
            "explanation": "Under Rule 8.1a(3), player must not alter ground surface by replacing divots, removing/pressing down placed turf, or creating/eliminating holes or uneven surfaces.",
            "examples": [
              "Replacing divot in divot hole before playing shot - not allowed",
              "Pressing down loose divot that's behind ball - prohibited",
              "Stamping down uneven ground near ball - general penalty",
              "Creating level area for stance by moving soil - not allowed"
            ]
      },
      {
            "situation": "Removing or pressing sand or loose soil",
            "explanation": "Under Rule 8.1a(4), player must not remove or press down sand or loose soil to improve conditions affecting the stroke.",
            "examples": [
              "Brushing sand away from behind ball - not allowed",
              "Pressing down loose soil near ball lie - prohibited",
              "Smoothing sand around ball before shot - general penalty",
              "Removing sand from area of intended stance - not allowed"
            ]
      },
      {
            "situation": "Removing dew, frost or water",
            "explanation": "Under Rule 8.1a(5), player must not remove dew, frost or water that affects conditions of the stroke.",
            "examples": [
              "Wiping dew off grass around ball - not allowed, except in teeing area",
              "Removing water droplets from line of play - prohibited",
              "Brushing frost from area of stance - general penalty, except in teeing area",
              "Drying wet ground conditions near ball - not allowed"
            ]
      }
    ]
    },
    {
        "id": "8.1b",
        "title": "Actions That Are Allowed",
        "text": "In preparing for or making a stroke, a player may take certain actions without penalty even if doing so improves the conditions affecting the stroke.",
        "keywords": ["actions allowed", "no penalty", "fairly search", "remove impediments", "mark ball", "ground club", "place feet", "take stance", "backswing", "teeing area", "bunker care", "putting green"],
        "conditions": [
      {
            "situation": "Ball search and impediment removal",
            "explanation": "Under Rule 8.1b(1) and (2), player may fairly search for ball per Rule 7.1a and take reasonable actions to remove loose impediments per Rule 15.1 and movable obstructions per Rule 15.2.",
            "examples": [
              "Moving leaves and twigs while searching for ball - allowed",
              "Removing rake or towel covering ball - allowed under Rule 15.2",
              "Bending grass back to find ball - reasonable search action",
              "Moving stones and pine cones away from ball - allowed under Rule 15.1"
            ]
      },
      {
            "situation": "Ball marking and club grounding",
            "explanation": "Under Rule 8.1b(3) and (4), player may mark spot and lift/replace ball per Rules 14.1-14.2, and ground club lightly in front/behind ball using the weight of the club only (but not press down or touch sand in bunker).",
            "examples": [
              "Placing ball marker and lifting ball to clean - allowed",
              "Lightly resting club behind ball on fairway - allowed",
              "Pressing club down on ground behind ball - not allowed",
              "Touching sand with club behind ball in bunker - prohibited under Rule 12.2b(1)"
            ]
      },
      {
            "situation": "Taking stance and making stroke",
            "explanation": "Under Rule 8.1b(5), (6) and (7), player may firmly place feet and dig in reasonably, take reasonable actions for stance (but not entitled to normal stance), and make stroke/backswing.",
            "examples": [
              "Digging feet into sand for stable stance - allowed",
              "Taking slightly awkward stance to avoid tree - must use least intrusive action",
              "Not entitled to move branch for normal swing - must play around it",
              "Making backswing that moves grass - allowed during actual stroke"
            ]
      },
      {
            "situation": "Special allowances in teeing area",
            "explanation": "Under Rule 8.1b(8) and Rule 6.2b, in teeing area player may place tee, move/bend/break natural objects, alter ground surface, remove sand/soil, remove dew/frost/water.",
            "examples": [
              "Pressing down grass behind teed ball - allowed in teeing area only",
              "Breaking tree branch hanging over tee - allowed in teeing area",
              "Removing water puddle from teeing area - allowed",
              "Creating level area in teeing area with foot - allowed"
            ]
      },
      {
            "situation": "Course care and green maintenance",
            "explanation": "Under Rule 8.1b(9) and (10), player may smooth bunker sand after ball is outside bunker per Rule 12.2b(3), and remove sand/soil and repair damage on putting green per Rule 13.1c.",
            "examples": [
              "Smoothing bunker sand after playing out - allowed for course care",
              "Removing sand from putting green - allowed under Rule 13.1c",
              "Repairing ball mark on green - allowed",
              "Cannot smooth bunker while ball still in bunker - must wait until ball is out"
            ]
      },
      {
            "situation": "Testing if natural object is loose",
            "explanation": "Under Rule 8.1b(11), player may move natural object to see if it's loose, but if found to be growing/attached, must return it to original position.",
            "examples": [
              "Gently moving branch to test if it's attached - allowed",
              "Branch is attached, must put it back in original position - required",
              "Stone appears attached but moves freely - loose impediment, may remove",
              "Root system attached, must return disturbed area to original state"
            ]
      }
    ]
    },
    {
        "id": "8.1c",
        "title": "Avoiding Penalty by Restoring Conditions",
        "text": "If a player has improved conditions by moving, bending, breaking objects or moving objects into position, they may avoid penalty by restoring original conditions before making the stroke.",
        "keywords": ["avoid penalty", "restore conditions", "original position", "eliminate improvement", "boundary object", "tree branch", "cannot avoid penalty", "broken object"],
        "conditions": [
      {
            "situation": "When restoration can avoid penalty",
            "explanation": "Under Rule 8.1c, no penalty if player eliminates improvement by restoring original conditions before next stroke, but only for breaches of Rule 8.1a(1) or 8.1a(2), not for other violations.",
            "examples": [
              "Player bends branch, then returns it to original position - no penalty if properly restored",
              "Moved boundary stake, then replaces it exactly - penalty avoided",
              "Altered ground surface by stomping - cannot avoid penalty by restoration",
              "Removed sand from around ball - cannot avoid penalty, restoration not allowed"
            ]
      },
      {
            "situation": "Restoring moved, bent or broken objects",
            "explanation": "Under Rule 8.1c(1), player may avoid penalty by restoring original object to original position to eliminate improvement, but cannot use different objects or repair materials.",
            "examples": [
              "Boundary stake moved back to exact original angle - penalty avoided",
              "Tree branch returned to original position - no penalty if improvement eliminated",
              "Branch broken significantly, cannot return to original position - penalty cannot be avoided",
              "Using tape to repair broken boundary object - not allowed, penalty remains"
            ]
      },
      {
            "situation": "Restoring objects moved into position",
            "explanation": "Under Rule 8.1c(2), player may avoid penalty by removing the object that was moved into position before making the stroke.",
            "examples": [
              "Stones stacked for stance, then removed - penalty avoided if done before stroke",
              "Cart moved to block wind, then moved away - no penalty if restored before shot",
              "Towel placed for stance improvement, then removed - penalty avoided"
            ]
      },
      {
            "situation": "Limitations on restoration",
            "explanation": "Under Rule 8.1c(1), player cannot avoid penalty if improvement is not eliminated or by using anything other than original object itself to restore conditions.",
            "examples": [
              "Branch bent too far to return to original position - penalty cannot be avoided",
              "Using different stake to replace removed boundary marker - penalty remains",
              "Tying moved branch with string to hold in place - not allowed, penalty applies",
              "Original object must be restored by itself without additional materials"
            ]
      }
    ]
    },
    {
        "id": "8.1d",
        "title": "Restoring Conditions Worsened After Ball Came to Rest",
        "text": "When conditions affecting the stroke are worsened after a player's ball came to rest, restoration may or may not be allowed depending on the cause.",
        "keywords": ["worsened conditions", "restoration allowed", "other person", "animal", "lift clean replace", "most similar conditions", "not allowed", "natural forces", "wind water"],
        "conditions": [
      {
            "situation": "When restoration is allowed",
            "explanation": "Under Rule 8.1d(1), if conditions worsened by person other than player or by animal, player may restore original conditions, lift/clean/replace ball, or place ball on nearest spot with similar conditions.",
            "examples": [
              "Another player's shot creates divot hole behind ball - may restore original conditions",
              "Animal tracks worsen lie of ball - allowed to restore and clean ball if needed",
              "Spectator steps on ground near ball - may restore damaged area",
              "Maintenance crew accidentally worsens area - restoration allowed"
            ]
      },
      {
            "situation": "Placement on nearest similar spot",
            "explanation": "Under Rule 8.1d(1), if worsened conditions cannot be easily restored, lift and place ball on nearest spot (not nearer hole) with most similar conditions within one club-length in same area.",
            "examples": [
              "Large divot cannot be properly restored - place ball on similar lie within one club-length",
              "Animal damage too extensive to restore - find most similar conditions nearby",
              "Must stay in same area of course (rough, fairway, etc.) when relocating",
              "New spot must be no closer to hole than original position"
            ]
      },
      {
            "situation": "When restoration is not allowed",
            "explanation": "Under Rule 8.1d(2), player must not improve conditions worsened by the player themselves, someone acting for player, or natural forces like wind or water.",
            "examples": [
              "Player's own practice swing creates divot - cannot restore or improve",
              "Caddie accidentally damages lie - player responsible, cannot restore",
              "Wind blows sand onto ball - natural force, cannot improve by removing sand",
              "Rain creates puddle affecting stance - natural condition, cannot improve"
            ]
      },
      {
            "situation": "Exception for lifted ball situations",
            "explanation": "Under Rule 8.1d(1) Exception and Rule 14.2d, if lie worsened when/after ball lifted and before replacement, covered by Rule 14.2d unless worsened during stopped play.",
            "examples": [
              "Ball marked and lifted, lie damaged before replacement - see Rule 14.2d procedures",
              "Play stopped for weather, ball lifted, area damaged during stoppage - Rule 8.1d applies",
              "Ball lifted for identification, someone steps on spot - Rule 14.2d governs replacement"
            ]
      }
    ]
    },
    {
        "id": "8.2",
        "title": "Player's Deliberate Actions to Alter Other Physical Conditions to Affect Player's Own Ball",
        "text": "This Rule covers a player's deliberate actions to alter other physical conditions to affect their ball at rest or stroke to be made.",
        "keywords": ["deliberate actions", "other physical conditions", "affect own ball", "where ball might go", "ball at rest", "steep slope", "care for course", "smoothing bunker"],
        "conditions": [
      {
            "situation": "When Rule 8.2 applies",
            "explanation": "Under Rule 8.2a, this Rule only covers deliberate actions to alter other physical conditions to affect player's ball at rest or stroke, not actions covered by Rules 11.2, 11.3 or 8.1a.",
            "examples": [
              "Deliberately altering area where ball might roll if it moves - Rule 8.2 applies",
              "Improving conditions around current ball position - covered by Rule 8.1a instead",
              "Deflecting own ball in motion - covered by Rules 11.2 and 11.3, not this Rule"
            ]
      },
      {
            "situation": "Prohibited actions affecting ball's future position",
            "explanation": "Under Rule 8.2b, player must not deliberately take Rule 8.1a actions to alter conditions affecting where ball might go after next/later stroke or if ball moves before stroke.",
            "examples": [
              "Ball on slope, removing stones from path where it might roll - not allowed",
              "Improving area where ball likely to land after shot - prohibited",
              "Creating backstop behind ball on steep green to prevent rolling - not allowed",
              "Altering conditions to affect ball's path if it moves before stroke - prohibited"
            ]
      },
      {
            "situation": "Exception for course care",
            "explanation": "Under Rule 8.2b Exception, no penalty if player alters conditions to care for the course, such as smoothing footprints in bunker or replacing divots.",
            "examples": [
              "Smoothing bunker footprints after playing shot - allowed for course care",
              "Replacing divot in area where ball might land - allowed if genuinely caring for course",
              "Repairing damage made by previous group - course care exception applies",
              "Must be genuine course care, not disguised attempt to help own play"
            ]
      }
    ]
    },
    {
        "id": "8.3",
        "title": "Player's Deliberate Actions to Alter Physical Conditions to Affect Another Player's Ball",
        "text": "This Rule covers a player's deliberate actions to alter physical conditions to affect another player's ball at rest or stroke to be made by that other player.",
        "keywords": ["affect another player", "deliberate actions", "improve worsen conditions", "other player's ball", "stroke to be made", "care for course", "bunker footprints"],
        "conditions": [
      {
            "situation": "When Rule 8.3 applies",
            "explanation": "Under Rule 8.3a, this Rule only covers deliberate actions to alter conditions affecting another player's ball at rest or stroke, not ball in motion situations covered by Rules 11.2 and 11.3.",
            "examples": [
              "Deliberately worsening another player's lie - Rule 8.3 applies",
              "Deflecting another player's ball in motion - covered by Rules 11.2/11.3, not this Rule",
              "Improving conditions for another player's upcoming stroke - Rule 8.3 violation"
            ]
      },
      {
            "situation": "Prohibited actions affecting another player",
            "explanation": "Under Rule 8.3b, player must not deliberately take Rule 8.1a actions to improve/worsen another player's stroke conditions or alter conditions affecting where their ball might go.",
            "examples": [
              "Breaking branch that interferes with opponent's swing - not allowed",
              "Deliberately damaging another player's lie - prohibited",
              "Improving area where another player's ball might land - not allowed",
              "Creating obstacle in path of another player's potential ball movement - prohibited"
            ]
      },
      {
            "situation": "Exception for course care affecting other players",
            "explanation": "Under Rule 8.3b Exception, no penalty if player alters conditions to care for course, even if it affects another player's ball or stroke.",
            "examples": [
              "Smoothing bunker sand that happens to help another player - allowed if genuine course care",
              "Replacing divot that improves another player's lie - allowed for course maintenance",
              "Repairing damage near another player's ball for course care - no penalty",
              "Must be genuine course care, not deliberate attempt to help or hinder other player"
            ]
      },
      {
            "situation": "Team play considerations",
            "explanation": "Under Rule 8.3 and Rules 22.2, 23.5, in Foursomes and Four-Ball, partner's actions are treated as player's actions regarding ball or equipment.",
            "examples": [
              "Partner deliberately improves conditions for other side - player gets penalty",
              "Partner's actions affecting opposing team's ball - treated as player's action",
              "Both partners responsible for ensuring no deliberate interference with other players"
            ]
      }
    ]
    },

    # --- Section 9: Ball Played as It Lies ---
    {
        "id": "9.1a",
        "title": "Playing Ball from Where It Came to Rest",
        "text": "A player's ball at rest on the course must be played as it lies, except when the Rules require or allow the player to play from another place or to lift and replace the ball.",
        "keywords": ["play as it lies", "ball at rest", "came to rest", "play from another place", "lift and replace", "original spot"],
        "conditions": [
      {
            "situation": "Basic play as it lies requirement",
            "explanation": "Under Rule 9.1a, a player's ball at rest on the course must be played as it lies unless Rules require or allow playing from another place.",
            "examples": [
              "Ball comes to rest in divot hole - must play as it lies",
              "Ball against tree root in awkward position - play as it lies",
              "Ball in casual water - Rules allow relief, may lift and take relief",
              "Ball out of bounds - Rules require playing from different place"
            ]
      },
          {
            "situation": "Exceptions allowing play from different place",
            "explanation": "Under Rule 9.1a, player may play from another place when Rules require or allow it, or when Rules allow lifting and replacing on original spot.",
            "examples": [
              "Taking penalty area relief - allowed to play from different place",
              "Unplayable ball relief - Rules allow playing from different spot",
              "Ball lifted for cleaning on green - must replace on original spot",
              "Stroke and distance relief - required to play from previous spot"
            ]
      }
    ]
    },
    {
        "id": "9.1b",
        "title": "Ball Moves During Backswing or Stroke",
        "text": "If a player's ball at rest begins moving after the player has begun the stroke or backswing and the player goes on to make the stroke, specific procedures apply.",
        "keywords": ["moves during backswing", "moves during stroke", "not replaced", "play from new spot", "stroke begun", "ball moving"],
        "conditions": [
      {
            "situation": "Ball moves after stroke/backswing begun",
            "explanation": "Under Rule 9.1b, if ball moves after stroke or backswing begun and player makes stroke, ball must not be replaced and must be played from where it comes to rest after the stroke.",
            "examples": [
              "Ball starts rolling during backswing, player continues and hits it - play from where it finishes",
              "Wind moves ball as player starting downswing - continue stroke, play from new position",
              "Ball moves just as club starts down - complete stroke, play from final resting place",
              "Do not replace ball even if player caused the movement"
            ]
      },
      {
            "situation": "Penalty determination for causing movement",
            "explanation": "Under Rule 9.1b and Rule 9.4b, if player caused ball to move during stroke, see Rule 9.4b to determine if penalty applies.",
            "examples": [
              "Player accidentally kicks ball during stroke - check Rule 9.4b for penalty",
              "Ball moves due to player's practice swing before stroke - may incur penalty under Rule 9.4b",
              "Natural forces move ball during stroke - no penalty, play from new spot"
            ]
      }
    ]
    },
    {
        "id": "9.2a",
        "title": "Deciding Whether Ball Moved",
        "text": "A player's ball at rest is treated as having moved only if it is known or virtually certain that it did.",
        "keywords": ["ball moved", "known or virtually certain", "might have moved", "treated as not moved", "play as lies"],
        "conditions": [
      {
            "situation": "Standard for determining if ball moved",
            "explanation": "Under Rule 9.2a, ball is treated as having moved only if it is known or virtually certain that it did. If uncertain, treat as not having moved.",
            "examples": [
              "Ball appears to be in slightly different position but uncertain - treat as not moved",
              "Player clearly sees ball roll two inches - known that it moved",
              "Ball marker shows ball definitely in different spot - virtually certain it moved",
              "When in doubt, assume ball did not move and play as it lies"
            ]
      },
      {
            "situation": "Playing ball when movement uncertain",
            "explanation": "Under Rule 9.2a, if ball might have moved but not known or virtually certain, it is treated as not having moved and must be played as it lies.",
            "examples": [
              "Ball in rough, appears different but can't be sure - play as it lies",
              "Other players think ball moved but you're not certain - play from current position",
              "Ball on slope, might have settled slightly - if uncertain, play as lies",
              "Better to play as lies than incorrectly replace when uncertain"
            ]
      }
    ]
    },
    {
        "id": "9.2b",
        "title": "Deciding What Caused Ball to Move",
        "text": "When a player's ball at rest has moved, it must be decided what caused it to move to determine replacement and penalty requirements.",
        "keywords": ["what caused movement", "four possible causes", "natural forces", "player actions", "opponent actions", "outside influence", "known virtually certain"],
        "conditions": [
      {
            "situation": "Four recognized causes of ball movement",
            "explanation": "Under Rule 9.2b(1), Rules recognize only four possible causes: natural forces (Rule 9.3), player's actions (Rule 9.4), opponent's actions in match play (Rule 9.5), or outside influence (Rule 9.6).",
            "examples": [
              "Wind blows ball across green - natural forces cause",
              "Player accidentally steps near ball causing movement - player's actions",
              "Opponent's ball hits player's ball - opponent's actions in match play",
              "Spectator, animal, or maintenance crew moves ball - outside influence"
            ]
      },
      {
            "situation": "Standard for determining cause",
            "explanation": "Under Rule 9.2b(2), player, opponent or outside influence treated as cause only if known or virtually certain. If not, ball treated as moved by natural forces.",
            "examples": [
              "Clearly see opponent's ball hit your ball - virtually certain opponent caused it",
              "Ball moved but no clear cause visible - treat as natural forces",
              "Player obviously kicked ball while walking by - known that player caused it",
              "When cause uncertain, default to natural forces as the cause"
            ]
      },
      {
            "situation": "Information gathering for determination",
            "explanation": "Under Rule 9.2b(2), must consider all reasonably available information that player knows or can get with reasonable effort without unreasonably delaying play.",
            "examples": [
              "Ask playing partners what they saw - reasonable information gathering",
              "Check for wind conditions or slopes - relevant available information",
              "Don't spend excessive time investigating cause - avoid delaying play",
              "Use video evidence if readily available and doesn't delay play"
            ]
      },
      {
            "situation": "Team play cause attribution",
            "explanation": "Under Rule 9.2b(1) and Rules 22.2, 23.5, in Foursomes and Four-Ball, partner's actions are treated as player's actions regarding ball or equipment.",
            "examples": [
              "Partner accidentally moves your ball in Four-Ball - treated as player caused it",
              "Partner's actions in Foursomes affect ball - player is responsible",
              "Partner's caddie moves ball - attributed to player"
            ]
      }
    ]
    },
    {
        "id": "9.3",
        "title": "Ball Moved by Natural Forces",
        "text": "If natural forces cause a player's ball at rest to move, there is no penalty and the ball must be played from its new spot, with specific exceptions.",
        "keywords": ["natural forces", "wind water", "no penalty", "play from new spot", "putting green exception", "lifted and replaced", "dropped placed replaced"],
        "conditions": [
      {
            "situation": "General rule for natural forces movement",
            "explanation": "Under Rule 9.3, if natural forces like wind or water cause ball to move, there is no penalty and ball must be played from its new spot.",
            "examples": [
              "Wind blows ball on fairway to new position - play from new spot, no penalty",
              "Water current moves ball in stream - play from where it comes to rest",
              "Ball rolls down slope due to gravity - natural force, play from new position",
              "Rain causes ball to move on saturated ground - play from new spot"
            ]
      },
      {
            "situation": "Exception for ball on putting green previously lifted",
            "explanation": "Under Rule 9.3 Exception 1 and Rule 13.1d, if ball on putting green moves after having been lifted and replaced, must replace on original spot regardless of cause.",
            "examples": [
              "Ball marked, cleaned, replaced on green, then wind moves it - must replace on original spot",
              "Ball replaced on green after repair, gravity moves it down slope - replace on original spot",
              "Any movement after replacement on green requires re-replacement, even if natural forces",
              "This exception applies no matter what caused the movement on green"
            ]
      },
      {
            "situation": "Exception for ball moving to different area after being put in play",
            "explanation": "Under Rule 9.3 Exception 2 and Rule 14.2, if ball dropped/placed/replaced moves to different course area or out of bounds due to natural forces, must replace on original spot.",
            "examples": [
              "Ball dropped for relief, wind blows it from rough into fairway - must replace in rough",
              "Ball placed after penalty area relief, rolls out of bounds - replace on original spot",
              "Ball replaced after lift, natural forces move it to different area - must replace",
              "Exception protects integrity of relief and replacement procedures"
            ]
      }
    ]
    },
    {
        "id": "9.4a",
        "title": "When Player's Lifted or Moved Ball Must Be Replaced",
        "text": "If the player lifts their ball at rest or causes it to move, the ball must be replaced on its original spot with specific exceptions.",
        "keywords": ["player lifts ball", "player causes movement", "must be replaced", "original spot", "taking relief", "different spot", "stroke begun"],
        "conditions": [
      {
            "situation": "General replacement requirement",
            "explanation": "Under Rule 9.4a and Rule 14.2, if player lifts ball or causes it to move, must replace on original spot (estimated if unknown), with specific exceptions.",
            "examples": [
              "Player accidentally kicks ball while walking - must replace on original spot",
              "Player lifts ball without authority - must replace where it was",
              "Ball moves when player removes obstruction - replace on original spot",
              "Estimate original spot if exact location unknown"
            ]
      },
      {
            "situation": "Exception for lifting under Rules for relief",
            "explanation": "Under Rule 9.4a and Rules 14.2d, 14.2e, no replacement required when player lifts ball under Rule to take relief or replace ball on different spot.",
            "examples": [
              "Lifting ball to take unplayable relief - no replacement, proceed with relief",
              "Lifting ball from penalty area for relief - no replacement on original spot",
              "Lifting ball to clean on putting green - authorized lifting, replace after cleaning",
              "Taking cart path relief by lifting ball - proceed with relief procedure"
            ]
      },
      {
            "situation": "Exception for movement during stroke",
            "explanation": "Under Rule 9.4a and Rule 9.1b, no replacement required when ball moves only after stroke or backswing begun and player completes stroke.",
            "examples": [
              "Ball moves during backswing, player completes stroke - play from final position",
              "Player causes movement after starting downswing - no replacement, play result",
              "Movement occurs during actual stroke execution - continue with stroke",
              "Ball must move after stroke/backswing begun to qualify for exception"
            ]
      }
    ]
    },
    {
        "id": "9.4b",
        "title": "Penalty for Player Lifting or Causing Ball to Move",
        "text": "If the player lifts or deliberately touches their ball at rest or causes it to move, the player gets one penalty stroke, with five specific exceptions.",
        "keywords": ["one penalty stroke", "deliberately touches", "five exceptions", "allowed to lift", "accidental movement", "putting green", "applying rule", "reasonable actions"],
        "conditions": [
      {
            "situation": "Basic penalty for lifting or moving ball",
            "explanation": "Under Rule 9.4b, if player lifts or deliberately touches ball at rest or causes it to move, player gets one penalty stroke, but five exceptions apply.",
            "examples": [
              "Player picks up ball thinking hole is over - one penalty stroke",
              "Player deliberately touches ball to improve lie - penalty stroke",
              "Player accidentally steps on ball - one penalty stroke if not covered by exceptions",
              "Caddie picks up ball without authorization - player gets penalty"
            ]
      },
      {
            "situation": "Exception 1 - Authorized lifting or movement",
            "explanation": "Under Rule 9.4b Exception 1, no penalty when player lifts or moves ball under Rule that allows lifting/replacement, requires replacement, or allows dropping/placing elsewhere.",
            "examples": [
              "Lifting ball to clean on putting green under Rule 13.1b - no penalty",
              "Taking relief from cart path immovable obstruction - no penalty for lifting",
              "Marking and lifting ball that interferes with another player - authorized",
              "Any relief procedure that permits or requires lifting - no penalty"
        ]
      },
      {
            "situation": "Exception 2 - Accidental movement during search",
            "explanation": "Under Rule 9.4b Exception 2 and Rule 7.4, no penalty when player accidentally causes ball to move while trying to find or identify it.",
            "examples": [
              "Ball moves when player steps near it while searching - no penalty",
              "Ball falls from tree when shaking branches to find it - accidental during search",
              "Moving sand to find ball causes ball to shift - no penalty under Rule 7.4",
              "Must be genuine search activity to qualify for exception"
            ]
      },
      {
            "situation": "Exception 3 - Accidental movement on putting green",
            "explanation": "Under Rule 9.4b Exception 3 and Rule 13.1d, no penalty when player accidentally causes ball to move on putting green, regardless of how it happens.",
            "examples": [
              "Ball moves when player accidentally scuffs it on green - no penalty",
              "Player steps near ball on green and it moves - no penalty",
              "Player accidentally causes ball to move while placing putter behind it - no penalty",
              "Ball moved by player's shadow or equipment on green - no penalty",
              "Any accidental movement on putting green is penalty-free"
            ]
      },
          {
            "situation": "Exception 4 - Accidental movement during rule application",
            "explanation": "Under Rule 9.4b Exception 4, no penalty when accidentally moving ball while taking reasonable actions to mark/lift/replace, remove obstruction, restore conditions, take relief, or measure.",
            "examples": [
              "Ball moves when placing ball marker - no penalty during marking process",
              "Ball shifts when removing rake near it - reasonable action under Rule 15.2",
              "Ball moves while determining nearest point of relief - reasonable relief action",
              "Ball moves during measuring for order of play - measuring under Rules"
            ]
      },
      {
            "situation": "Exception 5 - Ball against player or equipment",
            "explanation": "Under Rule 9.4b Exception 5 and Rules 11.1, 14.3c(1), no penalty if ball moves when player moves after ball came to rest against player/equipment from stroke or drop.",
            "examples": [
              "Ball comes to rest against player's foot after stroke, moves when player steps away - no penalty",
              "Dropped ball stops against player's leg, moves when player shifts - no penalty",
              "Ball hits player and stops against equipment, moves when equipment removed - no penalty",
              "Only applies when ball initially came to rest against player/equipment"
            ]
      }
    ]
    },
    {
        "id": "9.5",
        "title": "Ball Lifted or Moved by Opponent in Match Play",
        "text": "When it is known or virtually certain that the opponent lifted a player's ball or caused it to move in match play, specific replacement and penalty rules apply.",
        "keywords": ["opponent actions", "match play", "lifted moved", "must replace", "one penalty stroke", "conceding stroke", "player request", "mistaken belief"],
        "conditions": [
      {
            "situation": "When opponent must replace ball",
            "explanation": "Under Rule 9.5a and Rule 14.2, if opponent lifts or moves player's ball, must replace on original spot, except when conceding or at player's request.",
            "examples": [
              "Opponent accidentally kicks player's ball - must replace on original spot",
              "Opponent picks up player's ball by mistake - replace where it was",
              "Opponent says 'that's good' and picks up ball - concession, no replacement needed",
              "Player asks opponent to move ball out of way - no replacement required"
            ]
      },
      {
            "situation": "Penalty for opponent lifting or moving ball",
            "explanation": "Under Rule 9.5b, if opponent lifts, deliberately touches, or causes player's ball to move, opponent gets one penalty stroke with several exceptions.",
            "examples": [
              "Opponent deliberately moves player's ball to worse position - opponent gets penalty",
              "Opponent picks up player's ball without conceding - one penalty stroke to opponent",
              "Opponent accidentally causes ball to move during play - penalty unless exception applies",
              "Penalty is assessed to the opponent who caused the movement"
            ]
      },
      {
            "situation": "Exception for concessions and requests",
            "explanation": "Under Rule 9.5b Exception 1 and Rule 3.2b, no penalty when opponent lifts ball while conceding stroke/hole/match or at player's request.",
            "examples": [
              "Opponent says 'pick it up, that's good' - no penalty for concession",
              "Player asks opponent to mark and lift ball that's in way - no penalty",
              "Opponent concedes hole and picks up player's ball - allowed concession action",
              "Player requests opponent move ball for relief determination - no penalty"
            ]
      },
      {
            "situation": "Exception for mistaken ball marking on green",
            "explanation": "Under Rule 9.5b Exception 2, no penalty when opponent marks and lifts player's ball on putting green in mistaken belief it's opponent's own ball.",
            "examples": [
              "Opponent marks and lifts player's ball thinking it's their own - no penalty if honest mistake",
              "Similar balls on green, opponent confused about which is theirs - no penalty for mistake",
              "Must be genuine mistake on putting green to qualify for exception",
              "Replace ball on original spot and continue play"
            ]
      },
      {
            "situation": "Other exceptions mirroring player exceptions",
            "explanation": "Under Rule 9.5b Exception 3, no penalty when opponent accidentally causes movement during actions covered by Rule 9.4b Exceptions 2, 3, 4, or 5.",
            "examples": [
              "Opponent accidentally moves ball while searching for their own - no penalty",
              "Ball moves when opponent taking relief near player's ball - reasonable action",
              "Opponent measuring distance accidentally causes movement - measuring under Rules",
              "Same accidental movement exceptions apply to opponent as to player"
            ]
      }
    ]
    },
    {
        "id": "9.6",
        "title": "Ball Lifted or Moved by Outside Influence",
        "text": "If it is known or virtually certain that an outside influence lifted or moved a player's ball at rest, there is no penalty and the ball must be replaced.",
        "keywords": ["outside influence", "other player", "another ball", "no penalty", "must replace", "ball not found", "known virtually certain", "stroke and distance"],
        "conditions": [
      {
            "situation": "Outside influence movement - no penalty replacement",
            "explanation": "Under Rule 9.6 and Rule 14.2, if outside influence (including other player in stroke play or another ball) lifts or moves ball, no penalty and must replace on original spot.",
            "examples": [
              "Spectator picks up ball thinking it's lost - no penalty, replace on original spot",
              "Another player's ball hits your ball in stroke play - no penalty, replace your ball",
              "Animal picks up ball and carries it away - outside influence, replace ball",
              "Maintenance crew accidentally moves ball - replace on original spot"
            ]
      },
      {
            "situation": "Application whether ball found or not",
            "explanation": "Under Rule 9.6, replacement rule applies whether or not the player's ball has been found after being moved by outside influence.",
            "examples": [
              "Dog carries ball away, ball recovered - replace on original spot",
              "Spectator picks up ball, ball not found - still replace another ball on original spot",
              "Another ball hits yours into water, your ball lost - replace on original spot before it went in water",
              "Can replace with another ball if original not recovered"
            ]
      },
      {
            "situation": "When outside influence cause uncertain",
            "explanation": "Under Rule 9.6 and Rule 18.2, if not known or virtually certain that outside influence moved ball and ball is lost, must take stroke-and-distance relief.",
            "examples": [
              "Ball disappears but unsure if spectator took it - if lost, take stroke-and-distance",
              "Ball missing, might be outside influence or might be lost - treat as lost ball",
              "When uncertain about cause, cannot assume outside influence moved it",
              "Default to stroke-and-distance if ball lost and cause uncertain"
            ]
      },
      {
            "situation": "Wrong ball situations",
            "explanation": "Under Rule 9.6 and Rule 6.3c(2), if player's ball played as wrong ball by another player, covered by Rule 6.3c(2), not this Rule.",
            "examples": [
              "Another player hits your ball by mistake - see Rule 6.3c(2) for procedures",
              "Other player plays your ball thinking it's theirs - wrong ball rule applies",
              "Different procedures apply when ball played vs. just moved or lifted",
              "Rule 6.3c(2) covers wrong ball situations specifically"
            ]
      }
    ]
    },
    {
        "id": "9.7",
        "title": "Ball-Marker Lifted or Moved",
        "text": "This Rule covers what to do if a ball-marker marking the spot of a lifted ball is lifted or moved before the ball is replaced.",
        "keywords": ["ball-marker", "marker moved", "natural forces", "replace ball", "place marker", "original spot", "one penalty stroke", "exceptions apply"],
        "conditions": [
      {
            "situation": "Ball-marker movement replacement requirement",
            "explanation": "Under Rule 9.7a and Rule 14.2, if ball-marker lifted or moved (including by natural forces), player must either replace ball on original spot or place ball-marker to mark that spot.",
            "examples": [
              "Wind blows coin ball-marker away - replace ball on original spot or place new marker",
              "Player accidentally kicks ball-marker - choose to replace ball or re-mark spot",
              "Another player moves marker by mistake - replace ball or mark original spot",
              "Natural forces move marker, estimate original spot for replacement"
            ]
      },
      {
            "situation": "Penalty for lifting or moving ball-marker",
            "explanation": "Under Rule 9.7b, if player or opponent in match play lifts ball-marker or causes it to move when ball is lifted and not yet replaced, one penalty stroke applies.",
            "examples": [
              "Player deliberately picks up ball-marker before replacing ball - one penalty stroke",
              "Opponent kicks player's ball-marker in match play - opponent gets penalty stroke",
              "Ball-marker moved by player's caddie - player gets penalty stroke",
              "Penalty only applies when ball is lifted and not yet replaced"
            ]
      },
      {
            "situation": "Exceptions from ball movement rules apply to markers",
            "explanation": "Under Rule 9.7b Exception, in all cases where player or opponent gets no penalty for lifting ball or accidentally causing ball movement under Rules 9.4b and 9.5b, also no penalty for ball-marker.",
            "examples": [
              "Ball-marker accidentally moved while taking authorized relief - no penalty",
              "Marker moved during accidental ball movement on putting green - no penalty",
              "Marker displaced during reasonable actions under Rules - no penalty applies",
              "Same exceptions that protect ball movement also protect marker movement"
            ]
      }
    ]
    },

    # --- Section 10: Preparing for and Making a Stroke; Advice and Help ---
    {
        "id": "10.1a",
        "title": "Fairly Striking the Ball",
        "text": "In making a stroke, the player must fairly strike at the ball with any part of the head of the club such that there is only momentary contact between the club and the ball.",
        "keywords": ["fairly strike", "head of club", "momentary contact", "cannot push scrape scoop", "accidentally hits twice", "one stroke", "no penalty"],
        "conditions": [
      {
            "situation": "Requirement for fair striking",
            "explanation": "Under Rule 10.1a, player must fairly strike at ball with any part of club head with only momentary contact and must not push, scrape or scoop the ball.",
            "examples": [
              "Clean contact with club face - proper fair striking",
              "Ball contacted with toe or heel of club - still fair strike with club head",
              "Pushing ball forward with club face - not allowed, not fair striking",
              "Scooping ball up with club - prohibited, must be striking motion"
            ]
      },
      {
            "situation": "Accidental multiple contact with ball",
            "explanation": "Under Rule 10.1a, if player's club accidentally hits ball more than once, there has been only one stroke and no penalty applies.",
            "examples": [
              "Club bounces and hits ball twice in one swing - counts as one stroke, no penalty",
              "Player double-hits the ball in the same swing - counts as one stroke, no penalty",
              "Ball hits club face multiple times during follow-through - one stroke, no penalty",
              "Ball rebounds off ground and hits club again - accidental, counts as one stroke",
              "Multiple contact must be accidental during single stroke attempt"
            ]
      }
    ]
    },
    {
        "id": "10.1b",
        "title": "Anchoring the Club",
        "text": "In making a stroke, the player must not anchor the club, either directly by holding against body or indirectly through use of an anchor point.",
        "keywords": ["anchoring club", "directly", "indirectly", "gripping hand", "forearm", "anchor point", "against body", "merely touches", "no breach"],
        "conditions": [
      {
            "situation": "Direct anchoring prohibition",
            "explanation": "Under Rule 10.1b, player must not directly anchor club by holding club or gripping hand against any part of body, except may hold against hand or forearm.",
            "examples": [
              "Holding club grip against chest during stroke - direct anchoring, not allowed",
              "Pressing gripping hand against stomach - direct anchoring, prohibited",
              "Holding one hand against other hand during stroke - allowed exception",
              "Gripping hand held against forearm - permitted under exception"
            ]
      },
      {
            "situation": "Indirect anchoring prohibition",
            "explanation": "Under Rule 10.1b, player must not use anchor point by holding forearm against body to use gripping hand as stable point around which other hand swings club.",
            "examples": [
              "Holding left forearm against side to anchor grip - indirect anchoring, not allowed",
              "Using forearm against chest as pivot point for putting stroke - prohibited",
              "Bracing forearm against body while other hand swings - indirect anchoring violation",
              "Forearm must be free to move with club during stroke"
            ]
      },
      {
            "situation": "Incidental contact allowed",
            "explanation": "Under Rule 10.1b, if club, gripping hand or forearm merely touches body or clothing during stroke without being held against body, no breach occurs.",
            "examples": [
              "Club shaft brushes against shirt during swing - merely touching, allowed",
              "Hand accidentally touches body during follow-through - incidental contact, no breach",
              "Forearm grazes clothing but not held against body - merely touching, permitted",
              "Contact must be incidental, not deliberate anchoring or holding"
            ]
      },
      {
            "situation": "Definition of forearm for this Rule",
            "explanation": "Under Rule 10.1b, 'forearm' means the part of arm below elbow joint and includes the wrist for purposes of this Rule.",
            "examples": [
              "Area from elbow to wrist counts as forearm - included in anchoring restrictions",
              "Wrist considered part of forearm for anchoring rule - same restrictions apply",
              "Upper arm above elbow not included in forearm definition - different restrictions",
              "Precise anatomical definition ensures consistent rule application"
            ]
       }
    ]
    },
    {
        "id": "10.1c",
        "title": "Making Stroke While Standing Across or on Line of Play",
        "text": "The player must not make a stroke from a stance with feet deliberately placed on each side of, or touching, the line of play or its extension behind the ball.",
        "keywords": ["stance", "foot deliberately placed", "line of play", "extension behind ball", "reasonable distance", "accidentally", "avoid another player"],
        "conditions": [
       {
            "situation": "Prohibited stance positions",
            "explanation": "Under Rule 10.1c, player must not make stroke from stance with foot deliberately placed on each side of line of play or with either foot deliberately touching line of play or extension behind ball.",
            "examples": [
              "Standing with one foot on each side of line of play - prohibited stance",
              "Foot deliberately placed on line of play - not allowed",
              "Standing on extension of line behind ball - prohibited stance position",
              "Must avoid deliberately straddling or touching the line"
            ]
      },
      {
            "situation": "Line of play definition for this Rule",
            "explanation": "Under Rule 10.1c, for this Rule only, line of play does not include a reasonable distance on either side of the line.",
            "examples": [
              "Standing slightly to side of exact line - allowed within reasonable distance",
              "Foot near but not exactly on line of play - permitted if reasonable distance away",
              "Very close to line but not touching - may be acceptable depending on distance",
              "Rule allows some practical tolerance for stance positioning"
            ]
      },
      {
            "situation": "Exception for accidental stance or avoiding other player",
            "explanation": "Under Rule 10.1c Exception, no penalty if stance taken accidentally or to avoid another player's line of play.",
            "examples": [
              "Accidentally step on line while taking stance - no penalty if unintentional",
              "Move to straddle line to avoid stepping on opponent's line - exception applies",
              "Inadvertently position foot on line without realizing - accidental, no penalty",
              "Must be genuine accident or avoiding interference with other player"
            ]       
      }
    ]
    },
    {
        "id": "10.1d",
        "title": "Playing Moving Ball",
        "text": "A player must not make a stroke at a moving ball, with specific definitions of moving and three exceptions where there is no penalty.",
        "keywords": ["moving ball", "not at rest", "wobbling oscillating", "original spot", "three exceptions", "backswing begun", "falling off tee", "moving in water"],
        "conditions": [
      {
            "situation": "Definition of moving ball",
            "explanation": "Under Rule 10.1d, ball in play is 'moving' when not at rest on a spot. Ball that wobbles but stays on or returns to original spot is treated as at rest.",
            "examples": [
              "Ball rolling down slope - moving ball, cannot play",
              "Ball wobbling in wind but stays on same spot - treated as at rest, may play",
              "Ball oscillating after landing but returns to original position - not moving",
              "Ball must actually change location to be considered moving"
            ]
      },
      {
            "situation": "Exception 1 - Ball begins moving after backswing begun",
            "explanation": "Under Rule 10.1d Exception 1 and Rule 9.1b, making stroke at moving ball when ball begins moving only after player begins backswing is covered by Rule 9.1b, not this Rule.",
            "examples": [
              "Ball starts moving during backswing, player continues stroke - see Rule 9.1b procedures",
              "Wind moves ball just as downswing begins - covered by Rule 9.1b, not penalty here",
              "Ball movement after stroke begun follows different rule procedures",
              "Timing of when movement begins relative to stroke determines applicable rule"
            ]
      },
      {
            "situation": "Exception 2 - Ball falling off tee",
            "explanation": "Under Rule 10.1d Exception 2 and Rule 6.2b(5), making stroke at ball falling off tee is covered by Rule 6.2b(5), not this Rule.",
            "examples": [
              "Ball falls off tee during address, player swings anyway - see Rule 6.2b(5)",
              "Teed ball topples and player hits it while falling - covered by teeing area rules",
              "Special rules apply to balls falling from tees during stroke attempts",
              "Teeing area has specific procedures for this situation"
            ]
      },
      {
            "situation": "Exception 3 - Ball moving in water",
            "explanation": "Under Rule 10.1d Exception 3, when ball moving in temporary water or penalty area water, player may play moving ball without penalty or take relief under Rule 16.1 or 17.",
            "examples": [
              "Ball floating and moving in temporary water - may play it or take relief",
              "Ball drifting in penalty area stream - allowed to play moving ball",
              "Ball moving in puddle on fairway - may choose to play or take relief",
              "Must not unreasonably delay to let wind/current improve ball position"
            ]
      }
    ]
    },
    {
        "id": "10.2a",
        "title": "Advice",
        "text": "During a round, a player must not give advice to anyone in the competition, ask anyone for advice other than their caddie, or touch another player's equipment to learn information.",
        "keywords": ["advice", "during round", "give advice", "ask advice", "caddie only", "touch equipment", "learn information", "before round", "play stopped"],
        "conditions": [
      {
            "situation": "Prohibited advice giving and asking",
            "explanation": "Under Rule 10.2a, during round player must not give advice to anyone in competition playing on course or ask anyone for advice other than player's caddie.",
            "examples": [
              "Telling another player what club to use - giving advice, not allowed",
              "Asking opponent about distance to pin - asking for advice, prohibited",
              "Getting advice from own caddie about club selection - allowed",
              "Asking spectator for yardage information - not allowed during round"
            ]
      },
      {
            "situation": "Prohibited touching of equipment for information",
            "explanation": "Under Rule 10.2a, player must not touch another player's equipment to learn information that would be advice if given by or asked of the other player.",
            "examples": [
              "Touching opponent's clubs to determine club selection - prohibited",
              "Feeling weight of another player's putter - seeking advice through equipment",
              "Any equipment contact to gain strategic information is prohibited"
            ]
      },
      {
            "situation": "When advice restrictions do not apply",
            "explanation": "Under Rule 10.2a, restrictions do not apply before round, while play stopped under Rule 5.7a, or between rounds in competition.",
            "examples": [
              "Discussing strategy before first tee - allowed before round begins",
              "Getting advice during weather delay when play stopped - permitted",
              "Talking about course conditions between rounds - not restricted",
              "Practice round advice sharing - allowed as not during competition round"
            ]
      },
      {
            "situation": "Penalty timing for advice violations",
            "explanation": "Under Rule 10.2a, penalty applied based on when violation occurs: on hole being played/completed if during hole play, or on next hole if between holes.",
            "examples": [
              "Give advice while playing 5th hole - penalty applied to 5th hole",
              "Ask for advice walking to 6th tee - penalty applied to 6th hole",
              "Advice given after holing out but before leaving green - penalty on completed hole",
              "Timing determines which hole receives the penalty"
            ]
      }
    ]
    },
    {
        "id": "10.2b",
        "title": "Other Help",
        "text": "Rules governing other forms of help the player may receive, including line of play assistance, physical help, and positioning restrictions for caddies.",
        "keywords": ["other help", "line of play", "directional information", "caddie limitations", "set object down", "aiming", "restricted area", "physical help", "protection elements"],
        "conditions": [
      {
            "situation": "Caddie help with line of play restrictions",
            "explanation": "Under Rule 10.2b(1), when caddie helping with line of play, must not set object down for help, must not stand for player to play towards during stroke, and must not be in restricted area when prohibited.",
            "examples": [
              "Caddie placing towel on ground to show line - not allowed, cannot set object down",
              "Caddie standing where player should aim during stroke - prohibited during stroke",
              "Caddie pointing out direction before stroke - allowed if not during stroke",
              "Caddie providing aiming point before stroke with standing position - allowed if not during stroke",
              "Caddie providing aiming point before stroke by pointing a flagstick, or any other object - allowed if not during stroke",
              "Caddie attending flagstick close to hole - allowed exception"
            ]
      },
      {
            "situation": "Help from non-caddie persons",
            "explanation": "Under Rule 10.2b(2), player must not get line of play help from non-caddie except: public information about objects, standing to aim at (but must move before stroke).",
            "examples": [
              "Person pointing out tree showing center line of blind fairway - allowed public information",
              "Non-caddie standing to show direction on tee shot - allowed if moves before stroke",
              "Spectator giving specific distance information - not allowed, not public info",
              "Anyone attending flagstick close to hole - allowed exception"
            ]
      },
      {
            "situation": "Prohibition on setting objects for aiming",
            "explanation": "Under Rule 10.2b(3), player must not set object down to help with aiming, taking stance, or swinging, including marking sand or dew for similar purpose.",
            "examples": [
              "Placing club on ground to show aim direction - not allowed",
              "Setting down alignment stick behind ball - prohibited",
              "Making mark in sand to show swing path - not allowed",
              "Putting coin down to line up feet for stance - prohibited aiming aid"
            ]
      },
      {
            "situation": "Restricted area limitations for caddie",
            "explanation": "Under Rule 10.2b(4), from when player begins taking stance until stroke made, caddie restrictions apply for standing on extension of line of play behind ball.",
            "examples": [
              "Caddie standing behind player to help with aim as player begins taking stance - not allowed in restricted area",
              "Caddie checking for tree interference during backswing - may be in restricted area if moves before stroke",
              "Caddie inadvertently in restricted area - no penalty if unintentional",
              "Non-caddie tracking ball flight from behind - allowed for non-caddies"
            ]
      },
      {
            "situation": "Physical help and protection restrictions",
            "explanation": "Under Rule 10.2b(5), player must not make stroke while getting physical help or with anyone deliberately positioned to eliminate distractions or protect from elements.",
            "examples": [
              "Caddie holding player steady during stroke - physical help not allowed",
              "Person deliberately blocking sun during stroke - not allowed",
              "Caddie holding umbrella over player during swing - prohibited protection",
              "Player wearing own rain gear during stroke - allowed self-protection"
            ]
      }
    ]
    },
    {
        "id": "10.3a",
        "title": "Caddie May Help Player During Round",
        "text": "A player may have a caddie to carry clubs and give advice with specific limitations on number and purpose of caddies.",
        "keywords": ["one caddie", "carry transport handle", "give advice", "change caddies", "not temporarily", "other person", "shared caddie", "specific direction"],
        "conditions": [
      {
            "situation": "One caddie limitation and changing caddies",
            "explanation": "Under Rule 10.3a(1), player must not have more than one caddie at any time, may change caddies during round, but not temporarily for sole purpose of getting advice.",
            "examples": [
              "Having two people both carrying clubs - not allowed, only one caddie",
              "Replacing injured caddie with new caddie for rest of round - allowed permanent change",
              "Bringing in friend for one hole to get advice then switching back - not allowed temporary change",
              "Person carrying rain gear without clubs is not caddie unless named as such"
            ]
      },
      {
            "situation": "Defining who counts as caddie",
            "explanation": "Under Rule 10.3a(1), person walking with player or carrying other items is not caddie unless named as such by player or also carries/transports/handles clubs.",
            "examples": [
              "Friend walking along carrying umbrella - not caddie unless carries clubs too",
              "Person designated as caddie even if only carrying bag - is caddie",
              "Spectator helping with yardages but not carrying clubs - not caddie",
              "Anyone handling clubs becomes caddie even if not formally designated"
            ]
      },
      {
            "situation": "Shared caddie procedures",
            "explanation": "Under Rule 10.3a(2), when shared caddie's action needs attribution: specific direction determines player, ball involvement determines player, or all sharing players get penalty.",
            "examples": [
              "Shared caddie acts on specific instruction from Player A - action attributed to Player A",
              "Shared caddie accidentally moves Player B's ball - action attributed to Player B",
              "Shared caddie breaks rule with no specific direction or ball involvement - all players penalized",
              "Clear hierarchy for determining responsibility in shared caddie situations"
            ]
      }
    ]
    },
    {
        "id": "10.3b",
        "title": "What a Caddie May Do",
        "text": "Specific examples of actions that are always allowed, allowed only with authorization, and never allowed for caddies.",
        "keywords": ["always allowed", "carry transport", "search ball", "give advice", "smooth bunkers", "attend flagstick", "only with authorization", "not allowed", "concede", "replace ball", "drop place"],
        "conditions": [
      {
            "situation": "Actions always allowed for caddie",
            "explanation": "Under Rule 10.3b(1), caddie may always carry equipment, search for ball, give advice/information, care for course, remove sand/repair on green, attend flagstick, lift ball when relief certain, mark/lift/replace on green, clean ball, remove impediments/obstructions.",
            "examples": [
              "Carrying golf bag and driving cart - always allowed",
              "Searching in rough for player's ball - always allowed under Rule 7.1",
              "Giving yardage and club advice - always allowed",
              "Smoothing bunker after shot, repairing divots - course care always allowed",
              "Removing sand from green and fixing ball marks - always allowed under Rule 13.1c"
            ]
      },
      {
            "situation": "Actions requiring specific player authorization",
            "explanation": "Under Rule 10.3b(2), caddie may restore worsened conditions under Rule 8.1d and lift ball requiring replacement (except on green) only with specific authorization each time, not general permission.",
            "examples": [
              "Restoring area damaged by previous group - needs specific authorization each time",
              "Lifting ball for identification in rough - requires specific player authorization",
              "Cannot give general permission for round - must authorize each specific instance",
              "Player must explicitly approve each action, not blanket permission"
            ]
      },
      {
            "situation": "Actions never allowed for caddie",
            "explanation": "Under Rule 10.3b(3), caddie not allowed to concede in match play, replace ball (unless caddie moved it), drop/place ball in relief, or decide to take relief.",
            "examples": [
              "Caddie saying 'that putt is good' to concede - not allowed, only player can concede",
              "Caddie dropping ball in penalty area relief - not allowed, player must drop",
              "Caddie deciding ball is unplayable - not allowed, caddie can advise but player decides",
              "Caddie replacing ball that player moved - not allowed unless caddie moved it"
            ]
      }
    ]
    },
    {
        "id": "10.3c",
        "title": "Player Responsible for Caddie's Actions and Rule Breaches",
        "text": "A player is responsible for their caddie's actions during a round and gets penalty if caddie breaches Rules, with player's knowledge including caddie's knowledge.",
        "keywords": ["player responsible", "during round", "play stopped", "not before after", "caddie breaches rule", "player gets penalty", "player knowledge", "caddie knowledge"],
        "conditions": [
      {
            "situation": "Scope of player responsibility for caddie",
            "explanation": "Under Rule 10.3c, player responsible for caddie's actions during round and while play stopped under Rule 5.7a, but not before or after round.",
            "examples": [
              "Caddie moves ball during round - player gets penalty",
              "Caddie damages green during weather delay - player responsible during stopped play",
              "Caddie's actions before round starts - player not responsible",
              "Caddie behavior after round completion - not player's responsibility"
            ]
      },
          {
            "situation": "Penalty attribution for caddie rule breaches",
            "explanation": "Under Rule 10.3c, if caddie's action breaches Rule or would breach Rule if taken by player, player gets penalty under that Rule.",
            "examples": [
              "Caddie moves another player's ball - player gets penalty under ball movement rules",
              "Caddie improves lie by breaking branch - player gets general penalty under Rule 8.1a",
              "Caddie gives advice to opponent - player gets advice penalty",
              "Player receives same penalty caddie's action would carry if player did it"
            ]
      },
      {
            "situation": "Player knowledge includes caddie knowledge",
            "explanation": "Under Rule 10.3c, when Rule application depends on whether player aware of certain facts, player's knowledge treated as including whatever caddie knows.",
            "examples": [
              "Caddie sees ball move but player doesn't - player treated as knowing ball moved",
              "Caddie aware of relief area boundary but player isn't - player treated as knowing",
              "Caddie observes penalty area margin - player knowledge includes caddie's observation",
              "Cannot claim ignorance of facts that caddie observed or knew"
            ]
      }
    ]
    },




    # --- Section 11: Ball in Motion ---
    {
        "id": "11.1a",
        "title": "No Penalty for Accidental Contact",
        "text": "If a player's ball in motion accidentally hits any person or outside influence, there is no penalty to any player, with one exception in stroke play.",
        "keywords": ["accidentally hits", "no penalty", "any person", "outside influence", "player opponent", "caddies equipment", "exception stroke play", "putting green", "both balls"],
        "conditions": [
          {
            "situation": "General no penalty rule for accidental contact",
            "explanation": "Under Rule 11.1a, if player's ball in motion accidentally hits any person (including player) or outside influence, there is no penalty to any player.",
            "examples": [
              "Ball hits player after bouncing off tree - no penalty, accidental contact",
              "Ball strikes opponent's caddie walking nearby - no penalty to anyone",
              "Ball hits spectator and deflects toward hole - no penalty, play as it lies",
              "Ball bounces off cart or equipment - accidental contact, no penalty"
            ]
      },
      {
            "situation": "Exception for balls on putting green in stroke play",
            "explanation": "Under Rule 11.1a Exception, if player's ball in motion hits another ball at rest on putting green and both balls were on green before stroke, player gets general penalty (two strokes).",
            "examples": [
              "Putt hits another ball at rest on green in stroke play - two penalty strokes",
              "Both balls on green before stroke, one hits other - general penalty applies",
              "Ball played from off green hits ball on green - no penalty, exception doesn't apply",
              "Match play ball collision on green - no penalty, exception only applies to stroke play"
            ]
      }
    ]
    },
    {
        "id": "11.1b1",
        "title": "Ball Played from Anywhere Except Putting Green",
        "text": "When ball played from anywhere except putting green accidentally hits person or outside influence, normally play as it lies unless ball comes to rest on person, animal or moving object.",
        "keywords": ["anywhere except green", "play as lies", "comes to rest on", "person animal", "moving outside influence", "relief area", "one club-length", "same area", "not nearer hole"],
        "conditions": [
          {
            "situation": "Normal play as it lies rule",
            "explanation": "Under Rule 11.1b(1), if ball played from anywhere except putting green accidentally hits person or outside influence, ball must normally be played as it lies.",
            "examples": [
              "Ball hits tree and bounces into rough - play from rough where it stops",
              "Ball strikes spectator and deflects to fairway - play from fairway position",
              "Ball hits equipment and rolls backward - play from where it comes to rest",
              "Accept result whether favorable or unfavorable"
            ]
      },
      {
            "situation": "Relief when ball comes to rest on person/animal/moving object off green",
            "explanation": "Under Rule 11.1b(1), if ball comes to rest on person, animal or moving outside influence located anywhere except putting green, must drop within one club-length relief area in same area, not nearer hole.",
            "examples": [
              "Ball lands on spectator's shoulder - drop within one club-length of estimated point underneath",
              "Ball comes to rest on moving cart - relief area from estimated point under ball",
              "Ball stops on dog in fairway - drop in relief area, must stay in fairway",
              "Cannot leave ball on person/animal - must take relief"
            ]
      },
      {
            "situation": "Relief when ball comes to rest on person/animal/moving object on green",
            "explanation": "Under Rule 11.1b(1) and Rules 14.2b(2), 14.2e, if ball comes to rest on person, animal or moving outside influence on putting green, must place ball on estimated spot underneath.",
            "examples": [
              "Ball comes to rest on spectator standing on green - place ball on estimated spot under ball",
              "Ball stops on animal crossing green - place at estimated point underneath",
              "Ball lands on moving equipment on green - place ball, don't drop",
              "Use placing procedure for putting green, not dropping"
            ]
      }
    ]
    },
    {
        "id": "11.1b2",
        "title": "Ball Played from Putting Green",
        "text": "When ball played from putting green accidentally hits person or outside influence, normally play as it lies, but must replay stroke if hits specific objects on green.",
        "keywords": ["played from green", "play as lies", "replay stroke", "known virtually certain", "person other than player", "movable obstruction", "animal", "flagstick attendance"],
        "conditions": [
          {
            "situation": "Normal play as it lies from putting green",
            "explanation": "Under Rule 11.1b(2), if ball played from putting green accidentally hits player or outside influence, must normally be played as it lies.",
            "examples": [
              "Putt hits player's foot and deflects - play from where ball stops",
              "Ball hits player's equipment on green - normally play as it lies",
              "Putt strikes player accidentally - play from final resting position",
              "Default rule is play as it lies even from putting green"
            ]
      },
      {
            "situation": "Replay required for specific objects hit on green",
            "explanation": "Under Rule 11.1b(2) and Rule 14.6, if known or virtually certain ball hit person (other than player/flagstick attendant), movable obstruction (except club/marker/ball/flagstick), or animal on green, must replay stroke.",
            "examples": [
              "Putt hits another player on green - must replay stroke, not play as lies",
              "Ball hits rake left on green - movable obstruction, replay stroke",
              "Ball hits a player's golf club accidentally left on green - movable obstruction, replay stroke",
              "Putt strikes bird on green - animal contact, must replay",
              "Ball hits flagstick attendant - no replay required, play as lies"
            ]
      },
      {
            "situation": "Exceptions to replay requirement",
            "explanation": "Under Rule 11.1b(2), no replay required if ball hits player themselves, flagstick attendant, club used for stroke, ball-marker, ball at rest, or flagstick (see Rule 13.2b(2)).",
            "examples": [
              "Ball hits player who made stroke - no replay, play as it lies",
              "Putt hits person attending flagstick - covered by Rule 13.2b(2), not replay rule",
              "Ball hits ball-marker on green - no replay required",
              "Ball hits putter used for stroke - no replay needed"
            ]
      },
      {
            "situation": "Penalty for replay violations",
            "explanation": "Under Rule 11.1b(2) and Rule 14.7, if player replays from wrong place, gets general penalty. If doesn't replay when required, gets general penalty but stroke counts and not wrong place.",
            "examples": [
              "Required to replay but plays from different spot - general penalty for wrong place",
              "Should replay but continues play instead - general penalty, stroke counts",
              "Replaying from correct spot - no penalty",
              "Not replaying when required is penalty but not wrong place violation"
            ]
      }
    ]
    },
    {
        "id": "11.2a",
        "title": "When Rule 11.2 Applies - Deliberate Deflection",
        "text": "This Rule applies when it is known or virtually certain that a player's ball in motion was deliberately deflected or stopped by a person.",
        "keywords": ["known virtually certain", "deliberately deflected stopped", "deliberately touches", "deliberately positioned", "equipment object", "deflect stop", "match play concession", "no reasonable chance"],
        "conditions": [
          {
            "situation": "Definition of deliberate deflection or stopping",
            "explanation": "Under Rule 11.2a, applies when known or virtually certain ball deliberately deflected/stopped by person deliberately touching ball or ball hitting deliberately positioned equipment/object/person.",
            "examples": [
              "Player deliberately catches ball with hand - deliberate touching",
              "Caddie deliberately positioned to stop ball - deliberately positioned person",
              "Equipment placed to deflect ball from water hazard - deliberately positioned object",
              "Ball hits accidentally positioned person - not covered by this rule"
            ]
      },
      {
            "situation": "Exception for match play concessions",
            "explanation": "Under Rule 11.2a Exception and Rules 3.2a(1), 3.2b(1), opponent's ball deliberately deflected when no reasonable chance to be holed as concession or when needed to tie hole covered by concession rules, not this Rule.",
            "examples": [
              "Opponent picks up ball rolling past hole as concession - covered by Rule 3.2, not penalty",
              "Ball deflected when clearly cannot be holed and conceding - concession rule applies",
              "Ball needed to tie hole, opponent stops it when no chance - see concession procedures",
              "Must be genuine concession situation to qualify for exception"
            ]
      }
    ]
    },
    {
        "id": "11.2b",
        "title": "Penalty for Deliberate Deflection",
        "text": "A player gets the general penalty if they deliberately deflect or stop any ball in motion, whether their own ball or another player's ball.",
        "keywords": ["general penalty", "deliberately deflects stops", "own ball", "opponent ball", "another player", "exception ball moving water", "temporary water", "penalty area"],
        "conditions": [
          {
            "situation": "General penalty for deliberate deflection",
            "explanation": "Under Rule 11.2b, player gets general penalty if they deliberately deflect or stop any ball in motion, whether own ball or ball played by opponent or another player.",
            "examples": [
              "Player stops own ball rolling toward water - general penalty",
              "Player deflects opponent's ball in stroke play - general penalty",
              "Caddie catches player's ball on instruction - player gets general penalty",
              "Penalty applies regardless of whose ball is deflected"
            ]
      },
      {
            "situation": "Exception for ball moving in water",
            "explanation": "Under Rule 11.2b Exception and Rules 10.1d Exception 3, 16.1, 17, no penalty if player lifts their ball moving in water in temporary water or penalty area when taking relief.",
            "examples": [
              "Ball moving in temporary water puddle, player lifts for relief - no penalty",
              "Ball floating in penalty area stream, lifted for relief - exception applies",
              "Ball drifting in water hazard, player takes relief - no penalty for lifting moving ball",
              "Exception only applies when taking legitimate relief from water"
            ]
      }
    ]
    },
    {
        "id": "11.2c",
        "title": "Relief from Deliberate Deflection - Stroke from Anywhere Except Green",
        "text": "When ball deliberately deflected and stroke made from anywhere except putting green, relief based on estimated spot where ball would have come to rest.",
        "keywords": ["stroke anywhere except green", "estimated spot", "would have come to rest", "one club-length", "same area", "not nearer hole", "penalty area exception", "out of bounds", "stroke and distance"],
        "conditions": [
          {
            "situation": "Relief area for estimated spot on course except green",
            "explanation": "Under Rule 11.2c(1) and Rule 14.3, when ball would have come to rest anywhere on course except putting green, drop within one club-length relief area from estimated spot in same area, not nearer hole.",
            "examples": [
              "Ball deflected from fairway, would have landed in rough - drop in rough relief area",
              "Ball stopped before reaching bunker - relief area from estimated final spot",
              "Deflected ball estimated to stop in different area - relief area in that estimated different area",
              "Must estimate where ball would have come to rest without interference"
            ]
      },
      {
            "situation": "Relief when ball estimated to come to rest on putting green",
            "explanation": "Under Rule 11.2c(1) and Rules 14.2b(2), 14.2e, when ball would have come to rest on putting green, place ball on estimated spot using ball replacement procedures.",
            "examples": [
              "Ball deflected before reaching green, would have landed on green - place on estimated spot",
              "Ball heading for green when stopped - place ball, don't drop",
              "Use placing procedures for putting green relief",
              "Estimate where ball would have finished on green"
            ]
      },
      {
            "situation": "Special situations - penalty area and out of bounds",
            "explanation": "Under Rule 11.2c(1), if estimated spot in penalty area, player not required to take relief under this Rule and may take penalty area relief under Rule 17.1d. If estimated out of bounds, take stroke-and-distance under Rule 18.2.",
            "examples": [
              "Ball deflected, estimated to land in penalty area - may take penalty area relief instead",
              "Ball stopped before going out of bounds - stroke-and-distance relief",
              "Player choice for penalty area situations - this Rule relief or penalty area relief",
              "Out of bounds estimates require stroke-and-distance"
            ]
      }
    ]
    },
    {
        "id": "11.2c2",
        "title": "Relief from Deliberate Deflection - Stroke from Putting Green",
        "text": "When ball deliberately deflected and stroke made from putting green, must replay the stroke from original spot.",
        "keywords": ["stroke from green", "replay stroke", "original spot", "wrong place replay", "general penalty", "stroke counts", "not wrong place"],
        "conditions": [
          {
            "situation": "Replay requirement for strokes from putting green",
            "explanation": "Under Rule 11.2c(2) and Rule 14.6, player must replay stroke by playing original ball or another ball from spot where stroke was made.",
            "examples": [
              "Putt deliberately deflected by opponent - replay from original putting spot",
              "Ball stopped by spectator on green - replay the putt",
              "Caddie catches ball after putt - replay from where putt was made",
              "Use original ball or another ball for replay"
            ]
      },
      {
            "situation": "Penalties for replay violations",
            "explanation": "Under Rule 11.2c(2) and Rule 14.7, if player replays from wrong place gets general penalty. If doesn't replay when required, gets general penalty and stroke counts but not wrong place.",
            "examples": [
              "Replays putt from different spot on green - general penalty for wrong place",
              "Required to replay but plays next stroke instead - general penalty, stroke counts",
              "Fails to replay when required - penalty but original stroke still counts",
              "Not replaying is penalty but doesn't create wrong place violation"
            ]
      }
    ]
    },
    {
        "id": "11.3",
        "title": "Deliberately Removing Objects or Altering Conditions",
        "text": "When a ball is in motion, a player must not deliberately take actions to affect where any ball might come to rest by altering conditions or removing objects.",
        "keywords": ["ball in motion", "deliberately take actions", "affect where comes to rest", "alter physical conditions", "lift remove", "loose impediment", "movable obstruction", "flagstick", "equipment", "ball at rest green"],
        "conditions": [
          {
            "situation": "Prohibited actions while ball in motion",
            "explanation": "Under Rule 11.3 and Rule 8.1a, when ball in motion, player must not deliberately alter physical conditions by taking actions listed in Rule 8.1a or lift/remove loose impediments or movable obstructions.",
            "examples": [
              "Ball rolling toward divot, player replaces divot to help ball - not allowed",
              "Removing stones from ball's path while ball moving - prohibited",
              "Moving cart out of way while ball in motion - not allowed",
              "Pressing down raised turf while ball rolling - prohibited condition alteration"
            ]
      },
      {
            "situation": "Penalty applies regardless of effect",
            "explanation": "Under Rule 11.3, player breaches Rule for taking deliberate actions even if action does not affect where ball comes to rest.",
            "examples": [
              "Player removes obstacle but ball goes different direction anyway - still penalty",
              "Action taken to help but ball not affected - breach occurred when action taken",
              "Attempted interference that fails to change outcome - still rule violation",
              "Intent and action matter, not whether ball was actually affected"
            ]
      },
      {
            "situation": "Exception for moving specific items",
            "explanation": "Under Rule 11.3 Exception and Rules 9.4, 9.5, 13.2, 14.1, Rule does not prohibit lifting/moving removed flagstick, ball at rest on putting green, or equipment (except ball at rest off green or ball-marker).",
            "examples": [
              "Moving removed flagstick while ball in motion - allowed exception",
              "Lifting ball at rest on green while another ball rolling - allowed",
              "Moving player equipment (clubs, bag) while ball in motion - permitted",
              "Cannot move ball at rest off green or ball-marker anywhere"
            ]
      },
      {
            "situation": "Flagstick removal covered by different rule",
            "explanation": "Under Rule 11.3 and Rule 13.2, removing flagstick from hole (including attending it) while ball in motion covered by Rule 13.2, not this Rule.",
            "examples": [
              "Removing flagstick while ball approaches hole - see Rule 13.2 procedures",
              "Attending flagstick while ball rolling - covered by flagstick rules",
              "Different rules and penalties apply to flagstick situations",
              "This Rule doesn't cover flagstick removal from hole"
            ]
      }
    ]
    },

    # --- Section 12: Bunkers ---
    {
        "id": "12",
        "title": "Bunkers",
        "text": "Rule 12 is a specific Rule for bunkers, which are specially prepared areas intended to test the player's ability to play a ball from the sand. To make sure the player confronts this challenge, there are some restrictions on touching the sand before the stroke is made and on where relief may be taken for a ball in a bunker.",
        "keywords": ["bunkers", "sand", "specially prepared areas", "test player ability", "restrictions", "touching sand", "relief", "ball in bunker"],
        "examples": [
            "playing from sand bunker",
            "bunker relief options",
            "touching sand restrictions",
            "sand trap rules"
        ]
    },
    {
        "id": "12.1",
        "title": "When Ball Is in Bunker",
        "text": "A ball is in a bunker when any part of the ball touches sand on the ground inside the edge of the bunker, or is inside the edge of the bunker and rests on ground where sand would normally be, or in/on objects that touch sand in the bunker. If a ball lies on soil, grass or other growing objects inside the bunker without touching sand, the ball is not in the bunker.",
        "keywords": ["ball in bunker", "any part", "touches sand", "inside edge", "ground where sand normally would be", "loose impediment", "movable obstruction", "soil grass", "not in bunker"],
        "examples": [
            "determining if ball is in bunker",
            "ball touching sand",
            "ball on grass in bunker",
            "sand blown away from bunker"
        ],
        "conditions": [
        {
            "situation": "Ball touches sand on ground inside bunker edge",
            "explanation": "Under Rule 12.1, a ball is in a bunker when any part of the ball touches sand on the ground inside the edge of the bunker.",
            "examples": ["any part touching sand counts", "ball partially in sand", "ball on edge touching sand", "sand contact determines bunker status"]
        },
        {
            "situation": "Ball inside bunker edge on ground where sand normally would be",
            "explanation": "Under Rule 12.1, a ball is in a bunker when it's inside the edge and rests on ground where sand normally would be, such as where sand was blown or washed away by wind or water.",
            "examples": ["sand blown away by wind", "sand washed away by water", "hard ground where sand should be", "bunker bottom without sand"]
        },
        {
            "situation": "Ball on objects that touch sand in bunker",
            "explanation": "Under Rule 12.1, a ball is in a bunker when it rests in or on a loose impediment, movable obstruction, abnormal course condition or integral object that touches sand in the bunker or is on ground where sand normally would be.",
            "examples": ["ball on rake touching sand", "ball on leaves in sand", "ball on obstruction in bunker", "object touching sand makes ball in bunker"]
        },
        {
            "situation": "Ball on soil, grass or growing objects without touching sand",
            "explanation": "Under Rule 12.1, if a ball lies on soil or grass or other growing or attached natural objects inside the edge of the bunker without touching any sand, the ball is not in the bunker.",
            "examples": ["ball on grass island in bunker", "ball on soil not touching sand", "growing plants in bunker", "attached natural objects"]
        },
        {
            "situation": "Ball partly in bunker and partly in another area",
            "explanation": "Under Rule 12.1, if part of the ball is both in a bunker and in another area of the course, see Rule 2.2c for determining which area the ball is considered to be in.",
            "examples": ["ball straddling bunker edge", "part in bunker part on fairway", "mixed area situations", "refer to Rule 2.2c"]
        }
    ]
    },
    {
        "id": "12.2",
        "title": "Playing Ball in Bunker",
        "text": "This Rule applies both during a round and while play is stopped under Rule 5.7a. Players may remove loose impediments and movable obstructions before playing from a bunker, but there are restrictions on touching sand to test conditions or with the club in certain areas and situations.",
        "keywords": ["playing ball", "bunker", "during round", "play stopped", "remove impediments", "obstructions", "restrictions", "touching sand", "test conditions", "club"],
        "examples": [
            "removing objects from bunker",
            "touching sand penalties",
            "club grounding restrictions",
            "practice swing in bunker"
        ]
    },
    {
        "id": "12.2a",
        "title": "Removing Loose Impediments and Movable Obstructions",
        "text": "Before playing a ball in a bunker, a player may remove loose impediments under Rule 15.1 and movable obstructions under Rule 15.2. This includes any reasonable touching or movement of the sand in the bunker that happens while doing so.",
        "keywords": ["remove loose impediments", "movable obstructions", "Rule 15.1", "Rule 15.2", "reasonable touching", "movement of sand", "while doing so"],
        "examples": [
            "removing leaves from bunker",
            "moving rake from bunker",
            "touching sand while removing objects",
            "clearing debris from sand"
        ],      
    "conditions": [
        {
            "situation": "Removing loose impediments from bunker",
            "explanation": "Under Rule 12.2a, before playing a ball in a bunker, a player may remove loose impediments under Rule 15.1, including reasonable touching or movement of sand that happens while removing them.",
            "examples": ["removing leaves and twigs", "moving stones from sand", "touching sand while removing impediments", "clearing natural debris"]
        },
        {
            "situation": "Removing movable obstructions from bunker",
            "explanation": "Under Rule 12.2a, before playing a ball in a bunker, a player may remove movable obstructions under Rule 15.2, including reasonable touching or movement of sand that happens while removing them.",
            "examples": ["removing rake from bunker", "moving water bottles", "removing scorecard from sand", "touching sand while removing obstructions"]
        }
    ]
    },
    {
        "id": "12.2b",
        "title": "Restrictions on Touching Sand in Bunker",
        "text": "Before making a stroke at a ball in a bunker, a player must not deliberately touch sand to test conditions or touch sand with a club in specific restricted areas or situations. However, many other ways of touching sand are allowed without penalty, but general penalty applies if actions improve conditions affecting the stroke.",
        "keywords": ["restrictions", "touching sand", "before stroke", "deliberately touch", "test conditions", "club", "restricted areas", "allowed without penalty", "improve conditions"],
        "examples": [
            "testing sand condition penalty",
            "grounding club behind ball",
            "practice swing touching sand",
            "allowed sand touching"
        ],
    "conditions": [
        {
            "situation": "When touching sand results in penalty",
            "explanation": "Under Rule 12.2b(1), before making a stroke at a ball in a bunker, a player must not: deliberately touch sand with hand, club, rake or other object to test the condition; touch sand with club in the area right in front of or behind the ball (except when searching under Rule 7.1a or removing impediments under Rule 12.2a); touch sand with club in making a practice swing; or touch sand with club in making the backswing for a stroke.",
            "examples": ["testing sand with hand penalty", "grounding club behind ball penalty", "practice swing hitting sand", "backswing touching sand penalty"]
        },
        {
            "situation": "When touching sand does not result in penalty",
            "explanation": "Under Rule 12.2b(2), except as covered above, touching sand is allowed including: digging in with feet for stance; smoothing bunker for course care; placing clubs/equipment in bunker; measuring, marking, lifting, replacing or other rule actions; leaning on club for balance; or striking sand in frustration. However, general penalty applies if actions improve conditions affecting the stroke in breach of Rule 8.1a.",
            "examples": ["digging feet for stability", "smoothing after shot", "placing clubs in sand", "leaning for balance", "condition improvement penalty still applies"]
        },
        {
            "situation": "No restrictions after ball played out of bunker",
            "explanation": "Under Rule 12.2b(3), after a ball is played out of the bunker or player takes/intends relief outside bunker, player may touch sand and smooth bunker without penalty, even if required to take stroke-and-distance back into bunker or sand is on line of play. Restrictions reapply if ball returns to bunker, relief is taken in bunker, or player decides not to take outside relief.",
            "examples": ["ball successfully played out", "taking relief outside bunker", "touch sand freely", "smooth bunker for course care", "restrictions reapply if ball returns"]
        },
        {
            "situation": "Disability modifications for sand touching",
            "explanation": "Under Rule 12.2b(1), see Rule 25.2f for modifications for players who are blind, and Rule 25.4l for application for players who use assistive mobility devices.",
            "examples": ["blind player modifications", "assistive mobility device rules", "disability accommodations", "special provisions"]
        }
    ]
    },
    {
        "id": "12.2 Penalty",
        "title": "Penalty for Breach of Rule 12.2",
        "text": "Penalty for Breach of Rule 12.2: General Penalty.",
        "keywords": ["penalty", "breach", "Rule 12.2", "general penalty"],
        "examples": [
            "penalty for touching sand illegally",
            "general penalty for bunker violations",
            "two strokes or loss of hole"
        ],
    "conditions": [
        {
            "situation": "General penalty for Rule 12.2 violations",
            "explanation": "Under Rule 12.2, any breach of Rule 12.2 (touching sand illegally, testing conditions, etc.) results in the general penalty (loss of hole in match play, two strokes in stroke play).",
            "examples": ["illegal sand touching", "testing sand conditions", "grounding club illegally", "general penalty applies"]
        }
    ]
    },
    {
        "id": "12.3",
        "title": "Specific Rules for Relief for Ball in Bunker",
        "text": "When a ball is in a bunker, specific relief Rules may apply for interference by abnormal course conditions (Rule 16.1c), interference by dangerous animal conditions (Rule 16.2), and unplayable ball situations (Rule 19.3).",
        "keywords": ["specific relief rules", "ball in bunker", "abnormal course conditions", "Rule 16.1c", "dangerous animal conditions", "Rule 16.2", "unplayable ball", "Rule 19.3"],
        "examples": [
            "water in bunker relief",
            "dangerous animal in bunker",
            "unplayable ball in bunker",
            "bunker relief options"
        ],
    "conditions": [
        {
            "situation": "Abnormal course conditions in bunker",
            "explanation": "Under Rule 12.3, when a ball is in a bunker and there's interference by abnormal course conditions, specific relief rules apply under Rule 16.1c.",
            "examples": ["casual water in bunker", "ground under repair in bunker", "immovable obstruction in bunker", "see Rule 16.1c procedures"]
        },
        {
            "situation": "Dangerous animal conditions in bunker",
            "explanation": "Under Rule 12.3, when a ball is in a bunker and there's interference by dangerous animal conditions, specific relief rules apply under Rule 16.2.",
            "examples": ["snake in bunker", "bee nest in bunker", "dangerous animal near ball", "see Rule 16.2 procedures"]
        },
        {
            "situation": "Unplayable ball in bunker",
            "explanation": "Under Rule 12.3, when a ball is in a bunker and the player declares it unplayable, specific relief rules apply under Rule 19.3.",
            "examples": ["ball buried in bunker", "impossible lie in sand", "player declares unplayable", "see Rule 19.3 procedures"]
        }
    ]
    },

    # --- Section 13: Putting Greens ---
    {
        "id": "13",
        "title": "Putting Greens",
        "text": "Rule 13 is a specific Rule for putting greens. Putting greens are specially prepared for playing the ball along the ground and there is a flagstick for the hole on each putting green, so certain different Rules apply than for other areas of the course.",
        "keywords": ["putting greens", "specially prepared", "playing ball along ground", "flagstick", "hole", "different rules", "other areas"],
        "examples": [
            "putting green rules",
            "flagstick procedures",
            "green maintenance allowed",
            "ball marking on green"
        ]
    },
    {
        "id": "13.1",
        "title": "Actions Allowed or Required on Putting Greens",
        "text": "This Rule allows the player to do things on the putting green that are normally not allowed off the putting green, such as being allowed to mark, lift, clean and replace a ball. A ball is on the putting green when any part touches the green or lies on objects inside the green's edge.",
        "keywords": ["actions allowed", "mark lift clean replace", "ball on putting green", "any part touches", "objects inside edge", "normally not allowed"],
        "examples": [
            "marking ball on green",
            "cleaning ball on green",
            "determining if ball on green",
            "ball on obstruction on green"
        ],
        "conditions": [
        {
            "situation": "When ball is on putting green",
            "explanation": "Under Rule 13.1a, a ball is on the putting green when any part of the ball touches the putting green, or lies on or in anything (such as a loose impediment or an obstruction) and is inside the edge of the putting green. If part of the ball is both on the putting green and in another area of the course, see Rule 2.2c.",
            "examples": ["any part touching green surface", "ball on leaves on green", "ball on rake on green", "ball straddling green edge"]
        },
        {
            "situation": "Marking, lifting and cleaning ball on green",
            "explanation": "Under Rule 13.1b, a ball on the putting green may be lifted and cleaned (see Rule 14.1). The spot of the ball must be marked before it is lifted and the ball must be replaced on its original spot (see Rule 14.2).",
            "examples": ["mark before lifting", "clean ball on green", "replace on marked spot", "follow Rule 14.1 procedures"]
        }
    ]
    },
    {
        "id": "13.1c",
        "title": "Improvements Allowed on Putting Green",
        "text": "During a round and while play is stopped, a player may remove sand and loose soil on the putting green without penalty, and repair damage on the putting green by taking reasonable actions to restore the green as nearly as possible to its original condition using appropriate tools without unreasonably delaying play.",
        "keywords": ["improvements allowed", "remove sand", "loose soil", "repair damage", "reasonable actions", "original condition", "appropriate tools", "delay play"],
        "examples": [
            "removing sand from green",
            "repairing ball marks",
            "fixing spike marks",
            "using repair tool"
        ],
        "conditions": [
        {
            "situation": "Removal of sand and loose soil",
            "explanation": "Under Rule 13.1c(1), sand and loose soil on the putting green may be removed without penalty.",
            "examples": ["brush away sand", "remove loose dirt", "clear putting line", "no penalty for removal"]
        },
        {
            "situation": "Repair of damage - allowed procedures",
            "explanation": "Under Rule 13.1c(2), a player may repair damage on the putting green without penalty by taking reasonable actions to restore the putting green as nearly as possible to its original condition, but only by using their hand, foot or other part of the body or a normal ball-mark repair tool, tee, club or similar item of normal equipment, and without unreasonably delaying play.",
            "examples": ["use hand foot body", "ball-mark repair tool", "tee or club", "normal equipment only", "don't delay play"]
        },
        {
            "situation": "Definition of repairable damage",
            "explanation": "Under Rule 13.1c(2), 'damage on the putting green' means any damage caused by any person or outside influence, such as: ball marks, shoe damage (spike marks) and scrapes from equipment or flagstick; old hole plugs, turf plugs, seams of cut turf and maintenance tool indentations; animal tracks or hoof indentations; and embedded objects (stone, acorn, hail, tee) and their indentations.",
            "examples": ["ball marks and spike marks", "equipment indentations", "old hole plugs", "animal tracks", "embedded objects"]
        },
        {
            "situation": "What is NOT considered repairable damage",
            "explanation": "Under Rule 13.1c(2), 'damage on the putting green' does not include: normal maintenance practices (aeration holes, vertical mowing grooves); irrigation, rain or natural forces; natural surface imperfections (weeds, bare/diseased/uneven growth); or natural wear of the hole.",
            "examples": ["aeration holes", "irrigation effects", "natural imperfections", "normal hole wear"]
        },
        {
            "situation": "Penalty for excessive improvement",
            "explanation": "Under Rule 13.1c(2), if the player improves the putting green by taking actions that exceed what is reasonable to restore the green to its original condition (such as creating a pathway to the hole or using unauthorized objects), the player gets the general penalty for breach of Rule 8.1a.",
            "examples": ["creating pathway to hole", "using unauthorized objects", "excessive improvement", "general penalty applies"]
        }
    ]
    },
    {
        "id": "13.1d",
        "title": "When Ball or Ball-Marker Moves on Putting Green",
        "text": "There is no penalty if the player, opponent or another player accidentally moves the player's ball or ball-marker on the putting green. Different procedures apply depending on whether the ball was previously lifted and replaced and what caused the movement (natural forces vs accidental contact).",
        "keywords": ["ball moves", "ball-marker moves", "no penalty", "accidentally moves", "lifted and replaced", "natural forces", "accidental contact", "different procedures"],
        "examples": [
            "accidentally kick ball on green",
            "wind moves ball on green",
            "ball previously lifted and replaced",
            "replacing moved ball"
        ],
        "conditions": [
        {
            "situation": "No penalty for accidental movement on green",
            "explanation": "Under Rule 13.1d(1), there is no penalty if the player, opponent or another player in stroke play accidentally moves the player's ball or ball-marker on the putting green. The player must replace the ball on its original spot (estimated if unknown) or place a ball-marker to mark that original spot.",
            "examples": ["accidentally kick ball", "accidentally move marker", "no penalty on green", "replace on original spot"]
        },
        {
            "situation": "Exception for ball moving during stroke",
            "explanation": "Under Rule 13.1d(1), Exception – Ball Must Be Played as It Lies When Ball Begins to Move During Backswing or Stroke and Stroke Is Made (see Rule 9.1b).",
            "examples": ["ball moves during backswing", "stroke is made", "play as it lies", "see Rule 9.1b"]
        },
        {
            "situation": "Ball moved by natural forces - previously lifted and replaced",
            "explanation": "Under Rule 13.1d(2), if natural forces cause a ball on the putting green to move, and the ball had already been lifted and replaced on the putting green, the ball must be replaced on the spot it moved from (estimated if unknown), even though moved by natural forces (see Rule 9.3, Exception).",
            "examples": ["ball previously lifted and replaced", "wind moves ball", "must replace again", "estimate spot if unknown"]
        },
        {
            "situation": "Ball moved by natural forces - not previously lifted",
            "explanation": "Under Rule 13.1d(2), if natural forces move a ball that was not already lifted and replaced, the ball must be played from its new spot (see Rule 9.3).",
            "examples": ["ball not previously lifted", "wind moves ball", "play from new spot", "see Rule 9.3"]
        },
        {
            "situation": "Deliberate lifting procedures",
            "explanation": "Under Rule 13.1d(1), if the player or opponent deliberately lifts the player's ball or ball-marker on the putting green, see Rules 9.4 or 9.5 to determine if there is a penalty.",
            "examples": ["deliberate lifting", "see Rule 9.4", "see Rule 9.5", "penalty determination"]
        }
    ]
    },
    {
        "id": "13.1e",
        "title": "No Deliberate Testing of Greens",
        "text": "During a round and while play is stopped, a player must not deliberately test the putting green or a wrong green by rubbing the surface or rolling a ball, except between holes on the completed hole's green and practice greens.",
        "keywords": ["no deliberate testing", "during round", "play stopped", "rubbing surface not allowed", "rolling ball", "except between holes", "completed hole", "practice greens"],
        "examples": [
            "cannot test green surface",
            "cannot roll ball to test",
            "testing between holes allowed",
            "practice green testing allowed"
        ],
        "conditions": [
        {
            "situation": "Prohibited testing actions",
            "explanation": "Under Rule 13.1e, during a round and while play is stopped under Rule 5.7a, a player must not deliberately take either of these actions to test the putting green or a wrong green: rub the surface, or roll a ball. Penalty: General Penalty.",
            "examples": ["cannot rub surface", "cannot roll ball", "deliberate testing prohibited", "general penalty"]
        },
        {
            "situation": "Exception for testing between holes",
            "explanation": "Under Rule 13.1e Exception, between two holes, a player may rub the surface or roll a ball on the putting green of the hole just completed and on any practice green (see Rule 5.5b).",
            "examples": ["between holes testing allowed", "completed hole green", "practice green", "see Rule 5.5b"]
        },
        {
            "situation": "Committee Local Rule option",
            "explanation": "Under Rule 13.1e, the Committee may adopt a Local Rule prohibiting a player from rolling a ball on the putting green of the hole just completed (see Committee Procedures, Section 8; Model Local Rule I-2).",
            "examples": ["committee may prohibit", "local rule option", "rolling ball restriction", "completed hole prohibition"]
        }
    ]
    },
    {
        "id": "13.1f",
        "title": "Relief Must Be Taken from Wrong Green",
        "text": "When there is interference by a wrong green (ball touching wrong green or wrong green interfering with stance/swing), a player must not play the ball as it lies and must take free relief by dropping in a relief area, unless interference exists only because of clearly unreasonable choices.",
        "keywords": ["relief must be taken", "wrong green", "interference", "touching wrong green", "stance swing", "free relief", "dropping", "relief area", "clearly unreasonable"],
        "examples": [
            "ball on wrong green relief",
            "wrong green interfering with stance",
            "mandatory relief from wrong green",
            "unreasonable club choice"
        ],
        "conditions": [
        {
            "situation": "When interference by wrong green exists",
            "explanation": "Under Rule 13.1f(1), interference exists when: any part of the player's ball touches a wrong green or lies on or in anything inside the edge of a wrong green, or a wrong green physically interferes with the player's area of intended stance or area of intended swing.",
            "examples": ["ball touching wrong green", "ball on objects on wrong green", "stance on wrong green", "swing through wrong green"]
        },
        {
            "situation": "Mandatory relief procedures",
            "explanation": "Under Rule 13.1f(2), when there is interference by a wrong green, a player must not play the ball as it lies. Instead, must take free relief by dropping the original ball or another ball in a relief area: Reference Point is the nearest point of complete relief in the same area of the course; Relief Area is one club-length from reference point, in same area, not nearer hole, with complete relief from wrong green interference.",
            "examples": ["cannot play as lies", "must take relief", "nearest point complete relief", "one club-length relief area"]
        },
        {
            "situation": "No relief for clearly unreasonable choices",
            "explanation": "Under Rule 13.1f(3), there is no relief under Rule 13.1f if interference exists only because the player chooses a club, type of stance or swing or direction of play that is clearly unreasonable under the circumstances.",
            "examples": ["unreasonable club selection", "unreasonable stance", "unreasonable swing", "circumstances don't justify relief"]
        },
        {
            "situation": "Committee Local Rule option",
            "explanation": "Under Rule 13.1f, the Committee may adopt a Local Rule denying relief from a wrong green that only interferes with the area of intended stance (see Committee Procedures, Section 8; Model Local Rule D-3).",
            "examples": ["committee may deny relief", "stance interference only", "local rule option", "Model Local Rule D-3"]
        }
    ]
    },
    {
        "id": "13.2",
        "title": "The Flagstick",
        "text": "This Rule covers the player's choices for dealing with the flagstick. The player may leave the flagstick in the hole or have it removed (including having someone attend the flagstick), but must decide before making a stroke. There is normally no penalty if a ball in motion hits the flagstick. This Rule applies to a ball played from anywhere on the course.",
        "keywords": ["flagstick", "player choices", "leave in hole", "removed", "attend flagstick", "decide before stroke", "no penalty", "ball hits", "anywhere on course"],
        "examples": [
            "leaving flagstick in hole",
            "removing flagstick before putting",
            "ball hitting flagstick",
            "flagstick attendance procedures"
        ]
    },
    {
        "id": "13.2a",
        "title": "Leaving Flagstick in Hole",
        "text": "The player may make a stroke with the flagstick left in the hole. If the ball hits the flagstick, there is no penalty and the ball is played as it lies. There are limitations on moving the flagstick while the ball is in motion and restrictions on other players interfering with the flagstick.",
        "keywords": ["leaving flagstick", "stroke", "ball hits flagstick", "no penalty", "play as lies", "limitations moving", "ball in motion", "other players", "interfering"],
        "examples": [
            "putting with flagstick in",
            "ball hitting flagstick in hole",
            "cannot move flagstick during ball motion in some cases",
            "other player interference restrictions"
        ],
        "conditions": [
        {
            "situation": "Decision to leave flagstick and positioning",
            "explanation": "Under Rule 13.2a(1), the player may make a stroke with the flagstick left in the hole by either: leaving the flagstick where it is or moving it to be centred in the hole, or having a removed flagstick put back. The player must not try to gain advantage by deliberately moving the flagstick to a position other than centred - if done and ball hits flagstick, general penalty applies.",
            "examples": ["leave where it is", "centre in hole", "put back removed flagstick", "no advantage seeking"]
        },
        {
            "situation": "No penalty when ball hits flagstick left in hole",
            "explanation": "Under Rule 13.2a(2), if the player makes a stroke with the flagstick left in the hole and the ball in motion hits the flagstick, there is no penalty (except for advantage-seeking positioning) and the ball must be played as it lies.",
            "examples": ["no penalty for contact", "except advantage seeking", "play as it lies", "normal flagstick contact"]
        },
        {
            "situation": "Player cannot move flagstick to affect ball in motion",
            "explanation": "Under Rule 13.2a(3), after making a stroke with flagstick left in hole, the player and caddie must not deliberately move or remove the flagstick to affect where the ball might come to rest (like avoiding a hit). General penalty if done. No penalty if done for other reasons when reasonably believing ball won't hit flagstick.",
            "examples": ["cannot move to affect ball", "cannot remove to avoid hit", "general penalty", "other reasons allowed if ball won't hit"]
        },
        {
            "situation": "Other players cannot interfere with flagstick",
            "explanation": "Under Rule 13.2a(4), when player has left flagstick in hole without authorizing attendance, another player must not deliberately move or remove flagstick to affect the ball's movement. Other player gets general penalty if done before/during stroke or while ball in motion. No penalty if done for legitimate reasons (reasonably believe won't hit, not aware of play/ball motion).",
            "examples": ["other player cannot interfere", "other player gets penalty", "before during or after stroke", "legitimate reasons exception"]
        }
    ]
    },
    {
        "id": "13.2b",
        "title": "Removing Flagstick from Hole",
        "text": "The player may make a stroke with the flagstick removed from the hole by having it removed before playing or authorizing someone to attend it. If the ball hits the flagstick or person attending, the outcome depends on whether it was accidental or deliberate.",
        "keywords": ["removing flagstick", "removed before playing", "authorize", "attend flagstick", "ball hits", "person attending", "accidental", "deliberate"],
        "examples": [
            "remove flagstick before shot",
            "authorize flagstick attendance",
            "ball hits removed flagstick",
            "deliberate deflection by attendant"
        ],
        "conditions": [
        {
            "situation": "Decision to remove flagstick and attendance authorization",
            "explanation": "Under Rule 13.2b(1), the player may make a stroke with flagstick removed by either: having it removed before playing, or authorizing someone to attend it (hold it in/above/next to hole to show location, then remove during/after stroke). Player is treated as authorizing if: caddie is attending or standing next to hole; player asks someone to attend; or player sees someone attending and doesn't ask them to move.",
            "examples": ["remove before playing", "authorize attendance", "caddie attending automatically", "see person attending and don't object"]
        },
        {
            "situation": "Ball accidentally hits flagstick or attending person",
            "explanation": "Under Rule 13.2b(2), if the player's ball accidentally hits the flagstick or person who removed/attended it (or anything they're holding), there is no penalty and the ball must be played as it lies.",
            "examples": ["accidental contact", "no penalty", "play as it lies", "removed or attending flagstick"]
        },
        {
            "situation": "Ball deliberately deflected by attending person",
            "explanation": "Under Rule 13.2b(2), if the person attending deliberately deflects or stops the ball, Rule 11.2c applies: player must take relief under Rule 11.2c, not play as it lies. If the person was a player or caddie, that player gets general penalty. 'Deliberately deflected' includes: deliberately positioned removed flagstick, deliberately failed to remove attended flagstick, or deliberately failed to move out of ball's way.",
            "examples": ["deliberate deflection", "Rule 11.2c applies", "must take relief", "general penalty if player or caddie", "deliberate positioning or failure to move"]
        }
    ]
    },
    {
        "id": "13.2c",
        "title": "Ball Resting Against Flagstick in Hole",
        "text": "If a player's ball comes to rest against the flagstick left in the hole, it is treated as holed if any part is below the surface of the putting green. If no part is below the surface, the ball is not holed and specific procedures apply if the flagstick is removed.",
        "keywords": ["ball resting against", "flagstick in hole", "treated as holed", "part below surface", "putting green", "not holed", "flagstick removed", "specific procedures"],
        "examples": [
            "ball against flagstick in hole",
            "part of ball below surface",
            "ball considered holed",
            "flagstick removal procedures"
        ],
        "conditions": [
        {
            "situation": "Ball holed when part below surface",
            "explanation": "Under Rule 13.2c, if any part of the ball is in the hole below the surface of the putting green, the ball is treated as holed even if the entire ball is not below the surface.",
            "examples": ["part below surface", "treated as holed", "entire ball not required below", "holing out achieved"]
        },
        {
            "situation": "Ball not holed when no part below surface",
            "explanation": "Under Rule 13.2c, if no part of the ball is below the surface: the ball is not holed and must be played as it lies. If the flagstick is removed and the ball moves (falls in or moves away), there is no penalty and the ball must be replaced on the lip of the hole (see Rule 14.2).",
            "examples": ["no part below surface", "not holed", "play as it lies", "replace on lip if moves when flagstick removed"]
        },
        {
            "situation": "Penalties for violations",
            "explanation": "Under Rule 13.2c, penalty for playing from wrong place: General Penalty under Rule 14.7a. In stroke play, player is disqualified if they fail to hole out as required under Rule 3.3c.",
            "examples": ["wrong place penalty", "general penalty", "stroke play disqualification", "must hole out"]
        }
    ]
    },
    {
        "id": "13.3",
        "title": "Ball Overhanging Hole",
        "text": "If any part of a player's ball overhangs the lip of the hole, the player gets reasonable time to reach the hole plus ten seconds to wait. Different outcomes apply depending on when the ball falls and what happens during the waiting period.",
        "keywords": ["ball overhanging", "lip of hole", "reasonable time", "ten seconds", "wait", "when ball falls", "waiting period", "different outcomes"],
        "examples": [
            "ball hanging on lip of hole",
            "ten second waiting period",
            "ball falls after time limit",
            "opponent moves overhanging ball"
        ],
        "conditions": [
        {
            "situation": "Waiting time allowance and outcomes",
            "explanation": "Under Rule 13.3a, if any part of a ball overhangs the lip: player gets reasonable time to reach hole plus ten seconds to wait. If ball falls within this time, player has holed out with previous stroke. If ball doesn't fall in time, it's treated as at rest - if it then falls before being played, player has holed out with previous stroke but gets one penalty stroke added.",
            "examples": ["reasonable time plus ten seconds", "falls within time = holed with previous stroke", "doesn't fall = at rest", "falls after time = previous stroke plus penalty"]
        },
        {
            "situation": "Ball lifted or moved before waiting time ends",
            "explanation": "Under Rule 13.3b, if ball is lifted/moved (other than by natural forces) before waiting time ends: ball is treated as at rest, must be replaced on lip, waiting time no longer applies. See Rule 9.3 if replaced ball then moved by natural forces.",
            "examples": ["lifted before time ends", "treated as at rest", "replace on lip", "waiting time no longer applies"]
        },
        {
            "situation": "Opponent or other player deliberately moves overhanging ball",
            "explanation": "Under Rule 13.3b, if opponent (match play) deliberately moves overhanging ball before time ends: ball treated as holed with previous stroke, no penalty to opponent. If another player (stroke play) does this: that player gets general penalty (two strokes), ball replaced on lip.",
            "examples": ["opponent in match play = ball holed", "other player in stroke play = ball replaced and other player gets penalty", "replace on lip in stroke play", "different outcomes by format"]
        }
    ]
    }, 

    # --- Section 14: Procedures for Ball ---
    {
        "id": "14.1",
        "title": "Marking, Lifting and Cleaning Ball",
        "text": "A ball to be lifted under a Rule must be marked before it is lifted. This is done by placing a ball-marker, small coin or other similar object right behind or right next to the ball. The player can also hold a club on the ground right behind or next to the ball. If the spot is not marked before lifting or if the ball is cleaned when not allowed, the player gets one penalty stroke.",
        "keywords": ["mark", "lift", "clean", "ball-marker", "coin", "behind", "next to", "spot", "penalty", "stroke"],
        "examples": [
            "how to mark a golf ball",
            "cleaning ball when not on green",
            "penalty for improper marking"
        ],
        "conditions": [
        {
            "situation": "Who may lift the ball",
            "explanation": "The player's ball by be lifted under the rules by the player, or anyone the player authorizes, but such authorization must be given each time before the ball is lifted rather than generally for the entire round. The player's caddie may lift the player's ball without authorization when the ball is on the putting green or it is reasonable to conclude that the player will take relief under a Rule.",
            "examples": ["picking up the ball", "who mark the ball", "do I have to mark the ball", "can my caddie mark the ball for me"]
        },
        {
            "situation": "Cleaning the ball",
            "explanation": "A ball lifted from the putting green may always be cleaned. A ball lifted from anywhere else may always be cleaned except when it is lifted to see if it is cut or cracked, to identify it, because it interferes with play, or to see if it lies in a condition where relief is allowed. If a player cleans their ball when not allowed under this rule, they incur a one stroke penalty and must replace the ball.",
            "examples": ["when to clean the ball", "when to not clean the ball", "clean ball on the green"]
        },
        ]
    },
    {
        "id": "14.2",
        "title": "Replacing Ball on Spot",
        "text": "This Rule applies whenever a ball is lifted or moved and a Rule requires it to be replaced on a spot. The original ball must be used when replacing a ball, with limited exceptions. The ball must be replaced by the player or person who lifted it, by setting it down by hand on the required spot and letting it go so that it stays on that spot.",
        "keywords": ["replace", "spot", "placed", "released", "stays", "original", "second time", "nearest", "rest"],
        "examples": [
            "how to replace a ball",
            "replacing ball after marking on the green",
            "procedure when ball rolls away",
            "replacing ball after relief",
            "replacing ball after interference"
        ]
    },
    {
        "id": "14.2a",
        "title": "Original Ball Must Be Used",
        "text": "The original ball must be used when replacing a ball. Exception – Another Ball May Be Used When: The original ball cannot be recovered with reasonable effort and in a few seconds, so long as the player did not deliberately cause the ball to become unrecoverable, the original ball is cut or cracked, play resumes after it had been stopped, or the original ball was played by another player as a wrong ball.",
        "keywords": ["original ball", "must be used", "replacing", "exception", "another ball", "recovered", "reasonable effort", "few seconds", "cut", "cracked", "play resumes", "wrong ball"],
        "examples": [
            "using same ball after marking",
            "substituting when ball is damaged",
            "using different ball when original lost",
            "replacing with new ball after play stopped"
        ],
        "conditions": [
        {
            "situation": "Original ball required",
            "explanation": "When replacing a ball, you must use the same ball that was lifted or moved, not a different ball.",
            "examples": ["putting back the same ball you marked", "replacing the exact ball that moved", "using original ball after taking relief"]
        },
        {
            "situation": "Exception - Ball cannot be recovered",
            "explanation": "You may use another ball if the original cannot be recovered with reasonable effort and in a few seconds, as long as you didn't deliberately cause it to become unrecoverable.",
            "examples": ["ball rolled into water after marking", "ball blown away by wind", "ball accidentally kicked into bushes"]
        },
        {
            "situation": "Exception - Ball is damaged",
            "explanation": "You may use another ball if the original ball is cut or cracked (see Rule 4.2c).",
            "examples": ["ball cracked during play", "ball cut by sharp object", "ball damaged and unfit for play"]
        },
        {
            "situation": "Exception - Play resumption",
            "explanation": "You may use another ball when play resumes after it had been stopped (see Rule 5.7d).",
            "examples": ["using different ball after weather delay", "substituting ball when play resumes next day"]
        },
        {
            "situation": "Exception - Wrong ball played",
            "explanation": "You may use another ball if the original ball was played by another player as a wrong ball (see Rule 6.3c(2)).",
            "examples": ["another player hit your ball by mistake", "your ball was played as wrong ball"]
        }
    ]
    },
    {
        "id": "14.2b",
        "title": "Who Must Replace Ball and How It Must Be Replaced",
        "text": "The player's ball must be replaced under the Rules only by: The player, or any person who lifted the ball or caused it to move. If the player plays a ball that was replaced by someone not allowed to do so, the player gets one penalty stroke. The ball must be replaced by setting it down by hand on the required spot and letting it go so that it stays on that spot.",
        "keywords": ["who must replace", "player", "person who lifted", "caused to move", "penalty stroke", "setting down", "by hand", "required spot", "letting go", "stays"],
        "examples": [
            "player replacing own ball",
            "caddie replacing ball they lifted",
            "opponent replacing ball they moved",
            "penalty for improper replacement"
        ],
        "conditions": [
        {
            "situation": "Who may replace the ball",
            "explanation": "Only the player or the person who lifted the ball or caused it to move may replace it. Anyone else replacing the ball results in a one-stroke penalty for the player.",
            "examples": ["you replace your own marked ball", "caddie replaces ball they lifted", "playing partner replaces ball they accidentally moved"]
        },
        {
            "situation": "Proper replacement method",
            "explanation": "The ball must be replaced by setting it down by hand on the required spot and letting it go so that it stays on that spot. If replaced in the wrong way but on the right spot, it's a one-stroke penalty.",
            "examples": ["placing ball by hand, not dropping", "letting go so ball stays in place", "not rolling or pushing ball into position"]
        },
        {
            "situation": "Penalty for unauthorized replacement",
            "explanation": "If someone not authorized to replace the ball does so and you play it, you get one penalty stroke.",
            "examples": ["another player replaces your ball without authority", "spectator replaces your ball", "unauthorized person handles your ball"]
        }
    ]
    },
    {
        "id": "14.2c",
        "title": "Spot Where Ball Is Replaced",
        "text": "The ball must be replaced on its original spot (which if not known must be estimated), except when the ball must be replaced on a different spot under Rules 14.2d(2) and 14.2e or when the player will take relief under a Rule. If the ball was at rest on, under or against any immovable obstruction, integral object, boundary object or growing or attached natural object: The 'spot' of the ball includes its vertical location relative to the ground.",
        "keywords": ["original spot", "estimated", "different spot", "relief", "on under against", "immovable obstruction", "integral object", "boundary object", "growing", "attached", "vertical location"],
        "examples": [
            "replacing ball on exact spot",
            "estimating position when uncertain",
            "replacing ball against tree",
            "maintaining vertical position"
        ],
        "conditions": [
        {
            "situation": "Original spot required",
            "explanation": "Replace the ball on its original spot. If you don't know the exact spot, you must estimate where it was.",
            "examples": ["putting ball back where marked", "estimating spot when marker moved", "best guess of original position"]
        },
        {
            "situation": "Vertical position matters",
            "explanation": "If the ball was resting on, under, or against an immovable obstruction, integral object, boundary object, or growing/attached natural object, you must replace it in the same vertical position.",
            "examples": ["ball was resting against tree trunk", "ball was under overhanging branch", "ball was on top of cart path"]
        },
        {
            "situation": "Loose impediments don't need replacement",
            "explanation": "If loose impediments were removed when the ball was lifted or moved, or before replacement, they don't need to be put back.",
            "examples": ["leaves that were moved don't need replacing", "pine needles cleared during lifting", "sand that was disturbed"]
        }
    ]
    },
    {
        "id": "14.2d",
        "title": "Where to Replace Ball When Original Lie Altered",
        "text": "If the lie of a lifted or moved ball that must be replaced is altered, the player must replace the ball by re-creating the original lie (for balls in sand) or placing it on the nearest spot with the most similar lie within one club-length, not nearer the hole, and in the same area of the course.",
        "keywords": ["lie altered", "lifted", "moved", "re-creating", "original lie", "sand", "nearest spot", "similar lie", "one club-length", "not nearer hole", "same area"],
        "examples": [
            "lie changed after lifting ball",
            "footprint in sand altered",
            "grass flattened where ball was",
            "finding similar lie nearby"
        ],
        "conditions": [
        {
            "situation": "Ball in sand - recreate original lie",
            "explanation": "When the ball was in sand (bunker or elsewhere), recreate the original lie as much as possible. You may leave a small part of the ball visible if it was covered by sand.",
            "examples": ["recreating footprint in bunker", "making depression in sand", "partially burying ball if it was buried"]
        },
        {
            "situation": "Ball anywhere except sand - find similar lie",
            "explanation": "When the ball was anywhere except sand, place it on the nearest spot with the most similar lie within one club-length of the original spot, not nearer the hole, in the same area of course.",
            "examples": ["finding similar grass lie nearby", "matching slope and firmness", "staying in same area of fairway or rough"]
        },
        {
            "situation": "Unknown original lie",
            "explanation": "If you know the lie was altered but don't know what it was, estimate the original lie and replace accordingly.",
            "examples": ["estimating how ball sat in grass", "guessing original sand lie", "best estimate of ball position"]
        }
    ]
    },
    {
        "id": "14.2e",
        "title": "What to Do If Replaced Ball Does Not Stay on Original Spot",
        "text": "If the player tries to replace a ball but it does not stay on its original spot, the player must try a second time. If the ball again does not stay on that spot, the player must replace the ball by placing it on the nearest spot where the ball will stay at rest, with limits depending on where the original spot is located.",
        "keywords": ["replaced ball", "does not stay", "original spot", "second time", "again", "nearest spot", "stay at rest", "limits", "original spot located"],
        "examples": [
            "ball rolling away after placement",
            "trying second time to replace",
            "finding nearest stable spot",
            "ball won't stay on slope after placement"
        ],
        "conditions": [
        {
            "situation": "Try twice to replace on original spot",
            "explanation": "First try to replace the ball on its original spot. If it doesn't stay, try a second time. Only after two attempts can you place it elsewhere.",
            "examples": ["ball rolls down slope first try", "second attempt also fails", "ball keeps rolling away"]
        },
        {
            "situation": "General area - stay in general area",
            "explanation": "If the original spot was in the general area, find the nearest spot where the ball will stay at rest in the general area, not nearer the hole.",
            "examples": ["finding stable spot in fairway", "staying in rough if originally there", "avoiding nearer position to hole"]
        },
        {
            "situation": "Bunker or penalty area - stay in same area",
            "explanation": "If the original spot was in a bunker or penalty area, the nearest spot must be in the same bunker or same penalty area, not nearer the hole.",
            "examples": ["finding stable spot in same bunker", "staying within same penalty area", "not moving to different hazard"]
        },
        {
            "situation": "Putting green - green or general area",
            "explanation": "If the original spot was on the putting green, the nearest spot must be either on the putting green or in the general area, not nearer the hole.",
            "examples": ["finding stable spot on green", "moving to fringe if necessary", "staying on putting surface if possible"]
        }
    ]
    },
    {
        "id": "14.3",
        "title": "Dropping Ball in Relief Area",
        "text": "When taking relief, a player must drop a ball in the relief area. The ball must be dropped by the player from knee height straight down without touching the player or equipment. If the dropped ball does not come to rest in the relief area, the player must drop again. After two drops, the ball must be placed.",
        "keywords": ["drop", "relief area", "knee height", "straight down", "touching", "equipment", "come to rest", "again", "placed"],
        "examples": [
            "proper way to drop a ball",
            "relief area dimensions",
            "ball rolling out of relief area",
            "improving relief area before dropping"
        ]
    },
    {
        "id": "14.3a",
        "title": "Original Ball or Another Ball May Be Used",
        "text": "The player may use the original ball or another ball. This means that the player may use any ball each time they drop or place a ball under this Rule.",
        "keywords": ["original ball", "another ball", "any ball", "substitute", "drop", "place", "relief"],
        "examples": [
            "can I use a different ball for relief",
            "using new ball when taking relief",
            "substituting ball during relief procedure",
            "any ball allowed for relief"
        ],
        "conditions": [
        {
            "situation": "Can I use a different ball when taking relief",
            "explanation": "Under Rule 14.3a, you may use the original ball or another ball when dropping or placing during relief. This means you can use any conforming ball each time you drop or place under this rule.",
            "examples": ["using new ball for relief", "substituting ball during relief", "any conforming ball allowed", "don't need to use original ball"]
        },
        {
            "situation": "Do I have to use the same ball throughout the relief procedure",
            "explanation": "Under Rule 14.3a, you may use any ball each time you drop or place. This means you could use one ball for the first drop, a different ball for the second drop, and yet another ball when placing if needed.",
            "examples": ["different ball for each drop", "changing balls during relief", "any ball for placing after drops"]
        }
    ]
    },
    {
         "id": "14.3b",
        "title": "Ball Must Be Dropped in Right Way",
        "text": "The player must drop a ball in the right way, which means meeting all the requirements in (1), (2) and (3): Player must drop ball, ball must be dropped straight down from knee height without touching player or equipment, and ball must be dropped in relief area.",
        "keywords": ["right way", "requirements", "proper drop", "knee height", "player must drop", "straight down", "relief area"],
        "examples": [
            "how to drop a ball correctly",
            "proper dropping procedure",
            "requirements for valid drop",
            "dropping from knee height"
        ],
        "conditions": [
        {
            "situation": "Who is allowed to drop the ball",
            "explanation": "Under Rule 14.3b(1), the ball must be dropped only by the player. Neither the player's caddie nor anyone else may do so. Exception: Players with certain disabilities may give general authorization to another person to drop their ball.",
            "examples": ["can my caddie drop the ball", "only player may drop", "disability accommodation for dropping", "no one else can drop"]
        },
        {
            "situation": "How high should I drop the ball from",
            "explanation": "Under Rule 14.3b(2), you must drop the ball from knee height. Knee height means the height of your knee when in a standing position. The ball must fall straight down without throwing, spinning, or rolling it.",
            "examples": ["dropping from knee height", "what is knee height", "standing position knee height", "not waist height or shoulder height"]
        },
        {
            "situation": "Can the ball touch me or my equipment when dropping",
            "explanation": "Under Rule 14.3b(2), the ball must not touch any part of your body or equipment before it hits the ground. It must fall straight down without any contact with you or your gear.",
            "examples": ["ball cannot touch player before hitting ground", "no contact with equipment", "ball hits my leg while dropping", "ball touches club before ground"]
        },
        {
            "situation": "Can I spin or throw the ball when dropping",
            "explanation": "Under Rule 14.3b(2), you must let the ball fall straight down without throwing, spinning, rolling it, or using any other motion that might affect where the ball comes to rest.",
            "examples": ["no spinning when dropping", "no throwing the ball", "cannot roll ball", "must fall straight down"]
        },
        {
            "situation": "Where exactly should I drop the ball",
            "explanation": "Under Rule 14.3b(3), the ball must be dropped in the relief area. You may stand either inside or outside the relief area when dropping. For back-on-the-line relief, the ball must be dropped on the line.",
            "examples": ["drop within relief area", "can I stand outside relief area", "back-on-line relief procedure", "dropping on the line"]
        },
        {
            "situation": "What if I drop the ball incorrectly",
            "explanation": "Under Rule 14.3b(4), if you drop the ball in the wrong way, you must drop again correctly with no limit on attempts. An incorrectly dropped ball doesn't count toward the two-drop limit before placing.",
            "examples": ["penalty for dropping incorrectly", "dropping from wrong height", "must re-drop if done wrong", "unlimited re-drops for incorrect technique"]
        },
        {
            "situation": "Penalty for playing ball dropped incorrectly",
            "explanation": "Under Rule 14.3b(4), if you play a ball that was dropped in the wrong way: one penalty stroke if played from the relief area, or general penalty if played from outside the relief area or if placed when it should have been dropped.",
            "examples": ["playing incorrectly dropped ball", "one stroke penalty in relief area", "general penalty outside relief area", "placing instead of dropping penalty"]
        }
    ]
    },
    {
         "id": "14.3c",
        "title": "Ball Dropped in Right Way Must Come to Rest in Relief Area",
        "text": "This Rule applies only when a ball is dropped in the right way under Rule 14.3b. The ball must come to rest in the relief area to complete the relief procedure.",
        "keywords": ["right way", "come to rest", "relief area", "complete relief", "stays in area", "rolls out"],
        "examples": [
            "ball must stay in relief area",
            "what if ball rolls out of relief area",
            "completing relief procedure",
            "ball doesn't stay in area"
        ],
        "conditions": [
        {
            "situation": "Ball stays in relief area after dropping correctly",
            "explanation": "Under Rule 14.3c(1), when a ball dropped correctly comes to rest in the relief area, you have completed taking relief and must play the ball as it lies. It doesn't matter if the ball touches any person, equipment, or outside influence after hitting the ground but before coming to rest.",
            "examples": ["relief completed when ball stays", "play ball as it lies", "ball can hit equipment after bouncing", "ball touches caddie after dropping"]
        },
        {
            "situation": "Ball rolls out of relief area after correct drop",
            "explanation": "Under Rule 14.3c(2), if the ball comes to rest outside the relief area, you must drop a ball a second time. If the second drop also comes to rest outside the relief area, you must place a ball on the spot where the second dropped ball first touched the ground.",
            "examples": ["drop again if ball rolls out", "second drop also fails", "place after two unsuccessful drops", "spot where second ball hit ground"]
        },
        {
            "situation": "Ball won't stay when placed after two drops",
            "explanation": "Under Rule 14.3c(2), if the placed ball doesn't stay on the spot, place it again. If it still won't stay after the second placement, place it on the nearest spot where it will stay at rest, subject to the limits in Rule 14.2e.",
            "examples": ["ball won't stay when placed", "try placing twice", "nearest spot if ball keeps rolling", "ball rolls away from placement spot"]
        },
        {
            "situation": "No penalty when dropped ball accidentally hits someone",
            "explanation": "Under Rule 14.3c(1), there is no penalty to any player if a ball dropped in the right way accidentally hits any person, equipment, or other outside influence before coming to rest.",
            "examples": ["ball accidentally hits caddie", "ball bounces off cart", "no penalty for accidental contact", "ball hits another player accidentally"]
        }
    ]
    },
    {
         "id": "14.3d",
        "title": "What to Do if Ball Dropped in Right Way is Deliberately Deflected or Stopped by Person",
        "text": "This rule covers situations where a dropped ball is deliberately deflected or stopped by any person before it comes to rest, including when equipment is deliberately positioned to affect the ball.",
        "keywords": ["deliberately deflected", "deliberately stopped", "person", "equipment positioned", "touches ball", "deflect", "stop"],
        "examples": [
            "deliberately stopping dropped ball",
            "ball hits deliberately placed equipment",
            "intentional deflection of dropped ball",
            "positioning equipment to stop ball"
        ],
        "conditions": [
        {
            "situation": "Someone deliberately stops or deflects my dropped ball",
            "explanation": "Under Rule 14.3d, if any person deliberately deflects or stops a dropped ball before it comes to rest, you must drop again using Rule 14.3b procedures. The deflected ball doesn't count toward the two-drop limit. If a player or caddie does this, they get the general penalty.",
            "examples": ["deliberately stopping dropped ball", "penalty for deflecting drop", "must drop again after deflection", "caddie deliberately touches ball"]
        },
        {
            "situation": "Ball hits equipment that was deliberately positioned",
            "explanation": "Under Rule 14.3d, a ball is considered deliberately deflected if it hits equipment, objects, or persons that were deliberately positioned to deflect or stop the ball. This requires dropping again and may result in penalties.",
            "examples": ["equipment placed to stop ball", "deliberately positioned cart", "bag placed to deflect ball", "caddie standing to block ball"]
        },
        {
            "situation": "Ball is deflected when it obviously won't stay in relief area",
            "explanation": "Under Rule 14.3d exception, if a ball is deliberately deflected when there's no reasonable chance it would stay in the relief area anyway, there's no penalty and the ball is treated as coming to rest outside the area (counts as one of the two drops).",
            "examples": ["no penalty when ball clearly going outside", "deflection of ball obviously rolling away", "exception to deflection penalty", "ball clearly rolling downhill"]
        },
        {
            "situation": "What counts as deliberate deflection or stopping",
            "explanation": "Under Rule 14.3d, deliberate deflection occurs when: (1) a person deliberately touches the ball in motion after it hits the ground, or (2) the ball hits equipment/objects/persons that were deliberately positioned to affect the ball's movement.",
            "examples": ["deliberately touching moving ball", "positioning equipment to affect ball", "intentional contact with dropped ball", "strategic placement to deflect"]
        }
    ]
    },
    {
        "id": "14.4",
        "title": "When Player's Ball is Back in Play after Original Ball No Longer in Play",
        "text": "When a player's ball in play is lifted from the course or is lost or out of bounds, the ball is no longer in play. The player has a ball back in play only when they play a ball from the teeing area or the original ball or another ball is replaced, dropped or placed on the course with the intent for that ball to be in play.",
        "keywords": ["in play", "back in play", "replaced", "original ball", "lifted", "picked up", "substituted", "no longer", "drop", "dropped", "out of play"],
        "examples": [
            "ball is lifted from play",
            "ball is lost or out of bounds",
            "ball is dropped",
            "ball is back in play after relief",
            "ball is picked up",
            "when a new ball is in play",
            "substituting ball after out of bounds"
        ],
        "conditions": [
        {
            "situation": "If a ball is returned to the course in any way with the intent for it to be in play, the ball is in play",
            "explanation": "Under Rule 14.4, whenever a ball is returned to the course with intention for it to be in play, the ball is in play even if it was done so incorrectly or when not allowed by the Rules.",
            "examples": ["ball was substituted for original ball when not allowed", "ball placed, dropped, or replaced in the wrong place", "ball was placed, dropped, or replaced in the wrong way", "ball was placed, dropped, or replaced by using a procedure that did not apply", "a replaced ball is in play even if the ball marker marking its spot has not been removed."]
        }
    ]
    },
    {
        "id": "14.5",
        "title": "Correcting Mistake Made in Substituting, Replacing, Dropping or Placing Ball",
        "text": "A player may lift a ball without penalty and correct a mistake before playing the ball, when the player has substituted another ball when not allowed or the ball was replaced, dropped or placed (1) in a wrong place or (2) in a wrong way.",
        "keywords": ["correct", "mistake", "substitute", "replace", "drop", "place", "wrong place", "wrong way", "lift", "penalty"],
        "examples": [
            "fixing incorrect drop",
            "wrong ball substitution correction",
            "replacing ball in wrong place",
            "correcting a relief mistake"
        ]
    },
    {
        "id": "14.5a",
        "title": "Player May Correct Mistake Before Ball Is Played",
        "text": "When a player has substituted another ball for the original ball when not allowed under the Rules or the player's ball in play was replaced, dropped or placed (1) in a wrong way, (2) in a wrong place or (3) by using a procedure that did not apply: The player may correct the mistake without penalty. But this is allowed only before the ball is played.",
        "keywords": ["correct mistake", "before ball played", "substituted", "not allowed", "wrong way", "wrong place", "procedure did not apply", "without penalty"],
        "examples": [
            "can I fix my mistake before hitting the ball",
            "correcting wrong substitution",
            "fixing incorrect drop before playing",
            "mistake in relief procedure"
        ],
        "conditions": [
        {
            "situation": "Can I correct a mistake before playing the ball",
            "explanation": "Under Rule 14.5a, you may correct a mistake without penalty, but only before the ball is played. Once you make a stroke at the ball, you cannot correct the mistake and penalties may apply.",
            "examples": ["fix mistake before hitting ball", "no correction after stroke made", "must correct before playing", "deadline is making the stroke"]
        },
        {
            "situation": "I substituted a ball when I wasn't allowed to",
            "explanation": "Under Rule 14.5a, if you substituted another ball when the Rules required you to use the original ball, you may correct this mistake by lifting the substituted ball and using the original ball, but only before playing the substituted ball.",
            "examples": ["used wrong ball for replacement", "substituted when should use original", "wrong ball for marking on green", "correction requires original ball"]
        },
        {
            "situation": "I dropped or placed my ball in the wrong way",
            "explanation": "Under Rule 14.5a, if you replaced, dropped, or placed your ball using incorrect procedures (like wrong height, wrong person dropping, or improper placement), you may correct this by using the proper procedure, but only before playing the ball.",
            "examples": ["dropped from wrong height", "caddie dropped instead of player", "placed instead of dropped", "incorrect replacement procedure"]
        },
        {
            "situation": "I dropped or placed my ball in the wrong place",
            "explanation": "Under Rule 14.5a, if you put your ball in play in the wrong location (outside relief area, wrong reference point, etc.), you may correct this by placing the ball in the correct location, but only before playing the ball.",
            "examples": ["dropped outside relief area", "wrong reference point used", "placed on wrong spot", "incorrect relief area"]
        },
        {
            "situation": "I used a relief procedure that didn't apply",
            "explanation": "Under Rule 14.5a, if you took relief under a Rule that didn't apply to your situation, you may correct this by using the proper Rule or replacing the ball, but only before playing the ball.",
            "examples": ["took unplayable relief in penalty area", "used wrong relief rule", "relief didn't apply to situation", "incorrect procedure for condition"]
        }
    ]
    },
    {
        "id": "14.5b",
        "title": "When Player May Change to a Different Rule or Relief Option When Correcting Mistake in Taking Relief",
        "text": "When correcting a mistake in taking relief, whether the player must use the same Rule and relief option originally used or may change to a different Rule or relief option depends on the nature of the mistake.",
        "keywords": ["change rule", "relief option", "correcting mistake", "same rule", "different rule", "nature of mistake"],
        "examples": [
            "can I change relief options when correcting",
            "same rule vs different rule correction",
            "relief option flexibility when fixing mistake"
        ],
        "conditions": [
        {
            "situation": "Ball was dropped correctly in right place but procedure requires dropping again",
            "explanation": "Under Rule 14.5b(1), when the ball was put in play under the correct Rule and dropped in the right relief area, but the Rule requires the ball to be dropped or placed again (like ball rolled out of area), you must continue using the same Rule and same relief option when correcting.",
            "examples": ["ball rolled out of lateral relief area", "must continue with same lateral relief option", "same unplayable relief option required", "cannot switch relief types mid-procedure"]
        },
        {
            "situation": "Ball was dropped under correct rule but in wrong place",
            "explanation": "Under Rule 14.5b(2), when you used the correct Rule but dropped or placed the ball in the wrong location, you must continue under the same Rule but may choose any relief option under that Rule that applies to your situation.",
            "examples": ["dropped outside relief area for unplayable", "can switch to different unplayable option", "same rule but different relief choice", "flexibility in relief options"]
        },
        {
            "situation": "Ball was put in play under rule that didn't apply",
            "explanation": "Under Rule 14.5b(3), when you used a Rule that didn't apply to your situation, you may use any Rule that does apply. You have full flexibility to choose the appropriate Rule and relief option.",
            "examples": ["took unplayable relief in penalty area", "must use penalty area rules instead", "complete flexibility in rule choice", "any applicable rule allowed"]
        },
        {
            "situation": "Example - lateral relief mistake with ball rolling out",
            "explanation": "Under Rule 14.5b(1), if taking lateral relief for unplayable ball under Rule 19.2c, and the ball was dropped in the right relief area but came to rest outside it, when correcting you must continue with the same lateral relief option under Rule 19.2c.",
            "examples": ["lateral relief ball rolled out", "must stick with lateral option", "cannot switch to back-on-line", "same relief option required"]
        },
        {
            "situation": "Example - lateral relief dropped in wrong place",
            "explanation": "Under Rule 14.5b(2), if taking lateral relief for unplayable ball under Rule 19.2c but mistakenly dropped outside the required relief area, when correcting you must use Rule 19.2 but may choose any relief option (lateral, back-on-line, or stroke-and-distance).",
            "examples": ["lateral relief in wrong place", "can switch to any unplayable option", "flexibility after wrong place error", "any 19.2 option available"]
        },
        {
            "situation": "Example - unplayable relief in penalty area",
            "explanation": "Under Rule 14.5b(3), if you mistakenly took unplayable ball relief when your ball was in a penalty area (which Rule 19.1 doesn't allow), you may correct by either replacing the ball if it was lifted, or taking penalty relief under Rule 17 with any applicable option.",
            "examples": ["unplayable relief not allowed in penalty area", "must use penalty area rules", "replace ball or take penalty relief", "full flexibility after wrong rule"]
        }
    ]
    },
    {
        "id": "14.5c",
        "title": "No Penalty For Actions Taken After Mistake That Related to Original Ball",
        "text": "When a player corrects a mistake under Rule 14.5a, any penalty for actions that were taken after the mistake and which relate solely to the original ball do not count. But if those same actions would also be a penalty for the ball put in play to correct the mistake, the penalty applies to the ball now in play.",
        "keywords": ["no penalty", "actions after mistake", "original ball", "relate solely", "ball in play", "penalty applies"],
        "examples": [
            "penalties cancelled when correcting mistake",
            "actions affecting original ball vs new ball",
            "penalty protection when fixing errors"
        ],
        "conditions": [
        {
            "situation": "Penalties relating only to original ball are cancelled",
            "explanation": "Under Rule 14.5c, when you correct a mistake, any penalties for actions taken after the mistake that relate solely to the original ball (like accidentally moving it or improving conditions around it) do not count.",
            "examples": ["accidentally moved original ball after mistake", "improved lie around original ball", "penalties for original ball actions cancelled", "fresh start with correction"]
        },
        {
            "situation": "Penalties that affect both balls still apply",
            "explanation": "Under Rule 14.5c, if actions taken after the mistake would also be penalties for the ball you're now playing (like improving conditions that affect the new ball position), those penalties still apply to the ball now in play.",
            "examples": ["improved conditions affect new ball position", "actions benefit both old and new position", "penalty applies to current ball", "no escape from penalties affecting new ball"]
        },
        {
            "situation": "Example - moving original ball after wrong drop",
            "explanation": "Under Rule 14.5c, if you dropped in the wrong place, then accidentally moved the original ball while looking for it, when you correct the drop mistake, the penalty for moving the original ball is cancelled because it relates solely to the original ball.",
            "examples": ["moved original ball after drop error", "penalty cancelled when correcting drop", "original ball movement irrelevant", "no penalty for original ball actions"]
        },
        {
            "situation": "Example - improving conditions that help both positions",
            "explanation": "Under Rule 14.5c, if you dropped in wrong place, then improved conditions (like bending branches) that would help both the wrong position and the correct position, the penalty for improving conditions applies to your corrected ball position.",
            "examples": ["bent branches helping both positions", "condition improvement affects new ball", "penalty applies to corrected position", "cannot escape penalties affecting new ball"]
        },
        {
            "situation": "Exception for deliberately deflecting dropped ball",
            "explanation": "Under Rule 14.5c exception, in stroke play, if you get the general penalty for deliberately deflecting or stopping your dropped ball under Rule 14.3d, you still get that penalty even if you drop again to correct the mistake.",
            "examples": ["deliberately stopped dropped ball", "penalty remains even when correcting", "cannot escape deflection penalty", "exception to penalty cancellation rule"]
        }
    ]
    },
    {
        "id": "14.6",
        "title": "Making Next Stroke from Where Previous Stroke Made",
        "text": "This Rule applies whenever a player is required or allowed under the Rules to make the next stroke from where a previous stroke was made (such as, when taking stroke-and-distance relief, or playing again after a stroke that is cancelled or otherwise does not count). How the player must put a ball in play depends on the area of the course where that previous stroke was made. In all of these situations, the player may use either the original ball or another ball.",
        "keywords": ["next stroke", "previous stroke", "made", "stroke-and-distance", "cancelled", "does not count", "area of course", "original ball", "another ball"],
        "examples": [
            "stroke and distance relief",
            "playing from previous spot",
            "teeing area after penalty",
            "playing again after cancelled stroke",
            "replay from same location"
        ]
    },
    {
        "id": "14.6a", 
        "title": "Previous Stroke Made from Teeing Area",
        "text": "The original ball or another ball must be played from anywhere inside the teeing area (and may be teed) under Rule 6.2b.",
        "keywords": ["teeing area", "anywhere inside", "may be teed", "original ball", "another ball", "Rule 6.2b"],
        "examples": [
            "playing again from tee",
            "stroke and distance from teeing area", 
            "can I tee up when replaying from tee",
            "where to play from in teeing area"
        ],
        "conditions": [
        {
            "situation": "Playing again from the teeing area",
            "explanation": "Under Rule 14.6a, when you must play from where a previous stroke was made in the teeing area, you may play from anywhere inside the teeing area, not necessarily the exact spot where the previous stroke was made.",
            "examples": ["stroke and distance from tee", "can play from anywhere in teeing area", "not restricted to exact previous spot", "full teeing area available"]
        },
        {
            "situation": "Can I tee the ball when replaying from teeing area",
            "explanation": "Under Rule 14.6a, when playing from the teeing area after a previous stroke was made there, you may tee the ball just like any other stroke from the teeing area, following Rule 6.2b.",
            "examples": ["may tee ball when replaying", "same tee rules apply", "can use tee for stroke and distance", "teeing allowed for replay"]
        },
        {
            "situation": "Can I use a different ball when replaying from tee",
            "explanation": "Under Rule 14.6a, you may use either the original ball or another ball when playing from the teeing area after a previous stroke was made there.",
            "examples": ["any ball allowed for replay", "can substitute ball from tee", "original or different ball permitted", "ball choice flexibility from tee"]
        }
    ]
    },
    {
        "id": "14.6b",
        "title": "Previous Stroke Made from General Area, Penalty Area or Bunker", 
        "text": "The original ball or another ball must be dropped in this relief area (see Rule 14.3): Reference Point: The spot where the previous stroke was made (which if not known must be estimated). Size of Relief Area: One club-length from reference point. Limits: Must be in the same area of the course as the reference point, and must not be nearer the hole than the reference point.",
        "keywords": ["general area", "penalty area", "bunker", "dropped", "relief area", "reference point", "spot", "estimated", "one club-length", "same area", "not nearer hole"],
        "examples": [
            "stroke and distance from fairway",
            "replaying from rough", 
            "dropping after penalty in bunker",
            "one club length relief area",
            "staying in same area of course"
        ],
        "conditions": [
        {
            "situation": "Where is the reference point for replaying from general area, penalty area, or bunker",
            "explanation": "Under Rule 14.6b, the reference point is the spot where the previous stroke was made. If you don't know the exact spot, you must estimate where it was.",
            "examples": ["exact spot of previous stroke", "estimate if unsure of location", "where ball was when previous stroke made", "reference point for relief area"]
        },
        {
            "situation": "How big is the relief area when replaying",
            "explanation": "Under Rule 14.6b, you get a relief area of one club-length from the reference point (spot of previous stroke), but with specific limitations on where you can drop.",
            "examples": ["one club-length from previous spot", "measure from reference point", "relief area size", "club-length measurement"]
        },
        {
            "situation": "Where can I drop when replaying from general area, penalty area, or bunker",
            "explanation": "Under Rule 14.6b, you must drop in the same area of the course as the reference point and not nearer to the hole than the reference point. You must use the dropping procedures in Rule 14.3.",
            "examples": ["stay in same area of course", "cannot get nearer to hole", "fairway to fairway, bunker to bunker", "follow Rule 14.3 dropping procedures"]
        },
        {
            "situation": "Must I stay in the exact same area when replaying",
            "explanation": "Under Rule 14.6b, the relief area must be in the same area of the course as the reference point. If previous stroke was in general area, drop in general area; if in bunker, drop in bunker; if in penalty area, drop in penalty area.",
            "examples": ["bunker stroke replayed in bunker", "fairway stroke replayed in general area", "penalty area stroke in penalty area", "cannot change area of course"]
        },
        {
            "situation": "Can I use a different ball when replaying from these areas",
            "explanation": "Under Rule 14.6b, you may use either the original ball or another ball when dropping in the relief area for a replay stroke.",
            "examples": ["any ball allowed for replay", "can substitute ball", "original or different ball permitted", "ball choice flexibility"]
        },
        {
            "situation": "What if I can't get nearer to the hole within one club-length",
            "explanation": "Under Rule 14.6b, even if the one club-length relief area would naturally put you closer to the hole, you must not drop nearer to the hole than the reference point. This may restrict your relief area.",
            "examples": ["limited relief area on slopes", "cannot advance toward hole", "reference point restriction", "may have smaller area available"]
        }
    ]
    },
    {
        "id": "14.6c",
        "title": "Previous Stroke Made from Putting Green",
        "text": "The original ball or another ball must be placed on the spot where the previous stroke was made (which if not known must be estimated) (see Rule 14.2), using the procedures for replacing a ball under Rules 14.2b(2) and 14.2e.",
        "keywords": ["putting green", "placed", "spot", "previous stroke", "estimated", "Rule 14.2", "replacing procedures", "14.2b(2)", "14.2e"],
        "examples": [
            "replaying putt from same spot",
            "placing ball on green for replay", 
            "stroke and distance on putting green",
            "exact spot placement on green"
        ],
        "conditions": [
        {
            "situation": "How to replay from the putting green",
            "explanation": "Under Rule 14.6c, when you must play from where a previous stroke was made on the putting green, you must place (not drop) the ball on the exact spot where the previous stroke was made.",
            "examples": ["place ball on exact spot", "no dropping on green", "placement not dropping required", "precise spot placement"]
        },
        {
            "situation": "What if I don't know the exact spot on the green",
            "explanation": "Under Rule 14.6c, if you don't know the exact spot where the previous stroke was made on the putting green, you must estimate where it was and place the ball there.",
            "examples": ["estimate spot if unsure", "best guess of previous location", "reasonable estimate required", "approximate placement when uncertain"]
        },
        {
            "situation": "What procedures do I follow for placing on the green",
            "explanation": "Under Rule 14.6c, you must use the procedures for replacing a ball under Rules 14.2b(2) and 14.2e, including trying to place twice and finding nearest spot if ball won't stay.",
            "examples": ["follow ball replacement procedures", "try placing twice if won't stay", "nearest spot if ball rolls away", "Rule 14.2 placement procedures"]
        },
        {
            "situation": "Can I use a different ball when replaying from green",
            "explanation": "Under Rule 14.6c, you may use either the original ball or another ball when placing on the putting green for a replay stroke.",
            "examples": ["any ball allowed for replay", "can substitute ball on green", "original or different ball permitted", "ball choice flexibility on green"]
        },
        {
            "situation": "Example - stroke and distance after ball goes off green",
            "explanation": "Under Rule 14.6c, if you putt from the green and the ball goes into a penalty area, when taking stroke-and-distance relief you must place a ball on the spot where the putt was made, not drop it.",
            "examples": ["putt into water hazard", "place ball where putt was made", "stroke and distance from green", "placement required not dropping"]
        },
        {
            "situation": "If I'm on the green, then putt the ball off the green and into a bunker, can I take a drop?",
            "explanation": "Under Rule 14.6c, if you putt from the green, you may take a stroke and distance penalty of one stroke by placing the your original ball or a new ball from the same spot as the original putt.",
            "examples": ["putt into bunker", "place ball where putt was made", "stroke and distance from green", "replacement of ball on green when taking a penalty"]
        }
    ]
    },
        {
        "id": "14.6 Penalty",
        "title": "Penalty for Playing Ball from Wrong Place in Breach of Rule 14.6",
        "text": "Penalty for Playing Ball from a Wrong Place in Breach of Rule 14.6: General Penalty Under Rule 14.7a.",
        "keywords": ["penalty", "wrong place", "breach", "Rule 14.6", "general penalty", "Rule 14.7a"],
        "examples": [
            "penalty for wrong replay location",
            "playing from incorrect spot when replaying",
            "general penalty for wrong place"
        ],
        "conditions": [
        {
            "situation": "Penalty for playing replay stroke from wrong place",
            "explanation": "Under Rule 14.6, if you play your replay stroke from the wrong place (wrong area, nearer the hole, incorrect procedure), you get the general penalty under Rule 14.7a (loss of hole in match play, two strokes in stroke play).",
            "examples": ["dropped in wrong area for replay", "played nearer to hole than allowed", "used wrong procedure for replay", "general penalty applies"]
        }
    ]
    },  
    {
        "id": "14.7",
        "title": "Playing from Wrong Place",
        "text": "A player must not make a stroke from a wrong place. In stroke play, a player who has played from a wrong place must add two penalty strokes and must play out the hole with the ball played from the wrong place. In match play, the hole is lost if playing from a wrong place is a serious breach.",
        "keywords": ["wrong place", "stroke", "penalty", "stroke play", "match play", "serious breach", "two strokes", "hole lost", "serious", "advantage"],
        "examples": [
            "penalty for playing from wrong spot",
            "serious breach wrong place",
            "playing from incorrect teeing area",
            "wrong place violation"
            ]
    },
       {
        "id": "14.7a",
        "title": "Place from Where Ball Must Be Played",
        "text": "After starting a hole: A player must make each stroke from where their ball comes to rest, except when the Rules require or allow the player to play a ball from another place (see Rule 9.1). A player must not play their ball in play from a wrong place. Penalty for Playing Ball from a Wrong Place in Breach of Rule 14.7a: General Penalty.",
        "keywords": ["ball comes to rest", "stroke", "except", "rules require", "rules allow", "another place", "wrong place", "general penalty"],
        "examples": [
            "playing ball as it lies",
            "when can I play from different spot",
            "wrong place penalty",
            "ball comes to rest rule"
        ],
        "conditions": [
        {
            "situation": "Where must I play my ball from",
            "explanation": "Under Rule 14.7a, after starting a hole, you must make each stroke from where your ball comes to rest, except when the Rules specifically require or allow you to play from another place.",
            "examples": ["play ball as it lies", "stroke from where ball rests", "follow ball to its location", "ball comes to rest principle"]
        },
        {
            "situation": "When am I allowed to play from a different place",
            "explanation": "Under Rule 14.7a, you may only play from a place other than where your ball lies when the Rules specifically require or allow it, such as when taking relief, stroke-and-distance, or other authorized procedures.",
            "examples": ["taking relief allows different place", "stroke and distance from previous spot", "rules-authorized movement only", "specific rule permission required"]
        },
        {
            "situation": "What is a wrong place",
            "explanation": "Under Rule 14.7a, a wrong place is any location other than where your ball lies or where the Rules specifically require or allow you to play from. Playing from a wrong place results in the general penalty.",
            "examples": ["playing from unauthorized location", "moving ball without rule authority", "incorrect relief area", "unauthorized position"]
        },
        {
            "situation": "Penalty for playing from wrong place",
            "explanation": "Under Rule 14.7a, playing from a wrong place results in the general penalty (loss of hole in match play, two penalty strokes in stroke play).",
            "examples": ["general penalty applies", "two strokes in stroke play", "loss of hole in match play", "standard wrong place penalty"]
        }
    ]
    },
        {
        "id": "14.7b", 
        "title": "How to Complete a Hole after Playing from Wrong Place in Stroke Play",
        "text": "What a player does next depends on whether it was a serious breach – that is, whether the player could have gained a significant advantage by playing from a wrong place. The player must decide whether to play out the hole with the ball played from wrong place or to correct the mistake.",
        "keywords": ["complete hole", "stroke play", "serious breach", "significant advantage", "play out hole", "correct mistake", "wrong place"],
        "examples": [
            "completing hole after wrong place error",
            "serious breach determination",
            "correcting wrong place mistake",
            "two ball procedure"
        ],
        "conditions": [
        {
            "situation": "Not a serious breach - what to do",
            "explanation": "Under Rule 14.7b(1), if playing from the wrong place was not a serious breach (no significant advantage gained), you must play out the hole with the ball played from the wrong place without correcting the mistake. You get the general penalty (two strokes).",
            "examples": ["minor wrong place error", "no significant advantage", "continue with same ball", "cannot correct minor breach"]
        },
        {
            "situation": "Serious breach - what to do", 
            "explanation": "Under Rule 14.7b(1), if playing from the wrong place was a serious breach (significant advantage gained), you must correct the mistake by playing out the hole with a ball played from the right place. If you don't correct before starting next hole or returning scorecard, you're disqualified.",
            "examples": ["significant advantage gained", "must correct the mistake", "play from right place", "disqualification if not corrected"]
        },
        {
            "situation": "Uncertain if breach is serious - two ball procedure",
            "explanation": "Under Rule 14.7b(1), if you're uncertain whether the breach is serious, you should play out the hole with both the ball played from the wrong place and a second ball played from the right place under the Rules.",
            "examples": ["unsure if serious breach", "play two balls", "one from wrong place, one from right place", "protection against disqualification"]
        },
        {
            "situation": "What makes a breach serious",
            "explanation": "Under Rule 14.7b(1), a serious breach occurs when you could have gained a significant advantage by playing from the wrong place, such as a much easier shot, avoiding hazards, or getting substantially closer to the hole.",
            "examples": ["much easier shot from wrong place", "avoided penalty area", "significantly closer to hole", "substantial advantage gained"]
        },
        {
            "situation": "Must report two ball situation to committee",
            "explanation": "Under Rule 14.7b(2), if you're uncertain whether playing from wrong place was serious and play two balls, you must report the facts to the Committee before returning your scorecard. Failure to report results in disqualification.",
            "examples": ["must report to committee", "before returning scorecard", "failure to report means disqualification", "required even if same score with both balls"]
        },
        {
            "situation": "Committee decides score when two balls played",
            "explanation": "Under Rule 14.7b(3), when you play two balls, the Committee determines if there was a serious breach and which score counts, adding the appropriate penalties.",
            "examples": ["committee makes final decision", "determines which ball counts", "adds appropriate penalties", "serious breach determination by committee"]
        },
        {
            "situation": "Committee finds no serious breach with two balls",
            "explanation": "Under Rule 14.7b(3), if Committee decides no serious breach occurred, the score with the ball from wrong place counts plus two penalty strokes. All strokes with the other ball don't count.",
            "examples": ["wrong place ball score counts", "add two penalty strokes", "other ball strokes cancelled", "no serious breach ruling"]
        },
        {
            "situation": "Committee finds serious breach with two balls", 
            "explanation": "Under Rule 14.7b(3), if Committee decides serious breach occurred, the score with the correcting ball counts plus two penalty strokes. The stroke from wrong place and subsequent strokes with that ball don't count.",
            "examples": ["correcting ball score counts", "add two penalty strokes", "wrong place strokes cancelled", "serious breach ruling"]
        },
        {
            "situation": "Both balls played from wrong place",
            "explanation": "Under Rule 14.7b(3), if the correcting ball was also played from wrong place: not serious breach = four total penalty strokes (two for each wrong place); serious breach = disqualification.",
            "examples": ["both balls from wrong place", "four penalty strokes if not serious", "disqualification if serious", "compounding wrong place errors"]
        }
    ]
    },

    # --- Section 15: Relief from Loose Impediments and Movable Obstructions ---
    {
        "id": "15.1",
        "title": "Loose Impediments",
        "text": "Without penalty, a player may remove a loose impediment anywhere on or off the course, and may do so in any way (such as by using a hand or foot, using a club or other equipment, getting help from others or breaking off part of a loose impediment). But there are exceptions for removing loose impediments where a ball must be replaced and restrictions on deliberately removing loose impediments to affect a ball in motion.",
        "keywords": ["loose impediments", "remove", "penalty", "anywhere", "on course", "off course", "causes", "ball", "move", "replaced"],
        "examples": [
            "removing sticks near ball",
            "removing loose stones",
            "clearing pine needles",
            "removing loose sand or dirt",
            "removing leaves near ball",
            "loose leaves causing ball to move",
            "definition of loose impediment"
        ]
    },
    {
        "id": "15.1a",
        "title": "Removal of Loose Impediment",
        "text": "Without penalty, a player may remove a loose impediment anywhere on or off the course, and may do so in any way (such as by using a hand or foot, using a club or other equipment, getting help from others or breaking off part of a loose impediment). But there are two exceptions for removing loose impediments where ball must be replaced and restrictions on deliberately removing loose impediments to affect ball in motion.",
        "keywords": ["removal", "loose impediment", "without penalty", "anywhere", "hand", "foot", "club", "equipment", "help", "breaking", "exceptions"],
        "examples": [
            "using hand to remove leaves",
            "using club to move branches",
            "getting help to move large branch",
            "breaking off part of dead branch"
        ],
        "conditions": [
        {
            "situation": "General removal allowed",
            "explanation": "You may remove loose impediments anywhere on or off the course using any method - hands, feet, clubs, other equipment, or getting help from others. You may also break off parts of loose impediments.",
            "examples": ["picking up leaves by hand", "using putter to move pine cones", "asking playing partner to help move large branch"]
        },
        {
            "situation": "Exception 1 - Ball replacement situations",
            "explanation": "Before replacing a ball that was lifted or moved from anywhere except the putting green, you must not deliberately remove a loose impediment that would likely have caused the ball to move if removed before the ball was lifted.",
            "examples": ["not removing leaves that were supporting the ball before it was marked", "avoiding removal of impediments that were affecting ball's lie"]
        },
        {
            "situation": "Exception 2 - Ball in motion restrictions",
            "explanation": "You cannot deliberately remove loose impediments to affect a ball in motion (covered under Rule 11.3).",
            "examples": ["not removing leaves while ball is rolling toward them", "not clearing path for moving ball"]
        }
    ]
    },
    {
        "id": "15.1b",
        "title": "Ball Moved When Removing Loose Impediment",
        "text": "If a player's removal of a loose impediment causes their ball to move: The ball must be replaced on its original spot (which if not known must be estimated). If the moved ball had been at rest anywhere except on the putting green or in the teeing area, the player gets one penalty stroke under Rule 9.4b, except when Rule 7.4 applies (no penalty for ball moved during search) or when another exception to Rule 9.4b applies.",
        "keywords": ["ball moved", "removing", "loose impediment", "replaced", "original spot", "estimated", "penalty stroke", "putting green", "teeing area", "search"],
        "examples": [
            "ball moves when removing leaves",
            "replacing ball after moving twig",
            "penalty for ball movement in fairway",
            "no penalty on putting green"
        ],
        "conditions": [
        {
            "situation": "Ball must be replaced",
            "explanation": "If your ball moves when you remove a loose impediment, you must replace it on its original spot. If you don't know the exact spot, you must estimate where it was.",
            "examples": ["ball rolls when removing leaves", "ball shifts when moving pine cone", "estimating original position when uncertain"]
        },
        {
            "situation": "Penalty stroke applies in most areas",
            "explanation": "You get one penalty stroke if the ball was at rest anywhere except on the putting green or in the teeing area when it moved due to removing a loose impediment.",
            "examples": ["penalty in fairway", "penalty in rough", "penalty in bunker", "no penalty on tee", "no penalty on green"]
        },
        {
            "situation": "Exceptions to penalty",
            "explanation": "No penalty applies when the ball moves during search (Rule 7.4) or when other exceptions to Rule 9.4b apply, such as on the putting green or teeing area.",
            "examples": ["searching for ball and it moves", "removing impediments on putting green", "cleaning area around ball on tee"]
        }
    ]
    },

    {
        "id": "15.2",
        "title": "Movable Obstructions",
        "text": "This Rule covers free relief that is allowed from artificial objects that meet the definition of movable obstruction. It does not give relief from immovable obstructions (a different type of free relief is allowed under Rule 16.1) or boundary objects or integral objects (no free relief is allowed).",
        "keywords": ["movable obstruction", "remove", "penalty", "anywhere", "on course", "off course", "ball moves", "no penalty", "replaced", "original spot"],
        "examples": [
            "moving rakes from bunker",
            "removing water bottles near ball",
            "ball moves when moving cart"
        ]
    },
    {
        "id": "15.2a",
        "title": "Relief from Movable Obstruction",
        "text": "Without penalty, a player may remove a movable obstruction anywhere on or off the course and may do so in any way. If a player's ball moves while they are removing a movable obstruction: There is no penalty, and the ball must be replaced on its original spot. Specific relief procedures apply when the ball is in or on a movable obstruction.",
        "keywords": ["relief", "movable obstruction", "remove", "without penalty", "ball moves", "no penalty", "replaced", "original spot"],
        "examples": [
            "removing rake near ball",
            "moving cart away from ball",
            "lifting towel that ball is on",
            "moving scorecard from line of play"
        ],
        "conditions": [
        {
            "situation": "General removal allowed",
            "explanation": "You may remove any movable obstruction anywhere on or off the course in any way you choose, without penalty.",
            "examples": ["picking up rake from bunker", "moving cart from fairway", "removing water bottle from rough"]
        },
        {
            "situation": "No penalty if ball moves during removal",
            "explanation": "If your ball moves while you're removing a movable obstruction, there is no penalty and you must replace the ball on its original spot.",
            "examples": ["ball rolls when moving cart", "ball shifts when lifting rake", "replacing ball after it moves"]
        },
        {
            "situation": "Exception 1 - Tee markers",
            "explanation": "Tee markers must not be moved when a ball will be played from the teeing area (see Rules 6.2b(4) and 8.1a(1)).",
            "examples": ["cannot move tee markers before teeing off", "tee markers define teeing area boundaries"]
        },
        {
            "situation": "Exception 2 - Ball in motion restrictions",
            "explanation": "You cannot deliberately remove movable obstructions to affect a ball in motion (see Rule 11.3).",
            "examples": ["not moving obstruction while ball is rolling", "not clearing path for ball in motion"]
        }
    ]
    },
    {
        "id": "15.2a(2)",
        "title": "Relief When Ball Is in or on Movable Obstruction Anywhere on Course Except on Putting Green",
        "text": "The player may take free relief by lifting the ball, removing the movable obstruction and dropping the original ball or another ball in this relief area: Reference Point: The estimated point right under where the ball was at rest in or on the movable obstruction. Size of Relief Area: One club-length from reference point. Limits: Must be in the same area of the course as the reference point, and must not be nearer the hole than the reference point.",
        "keywords": ["ball in obstruction", "free relief", "lifting", "removing", "dropping", "reference point", "one club-length", "same area", "not nearer hole"],
        "examples": [
            "ball in cart",
            "ball on towel",
            "ball in bunker rake",
            "ball on scorecard",
            "ball in water bottle"
        ],
        "conditions": [
        {
            "situation": "Ball in or on movable obstruction",
            "explanation": "When your ball is in or on a movable obstruction anywhere except the putting green, you may take free relief by lifting the ball, removing the obstruction, and dropping within one club-length of the reference point.",
            "examples": ["ball sitting in cart", "ball resting on rake in bunker", "ball on top of towel"]
        },
        {
            "situation": "Reference point determination",
            "explanation": "The reference point is the estimated point right under where the ball was at rest in or on the movable obstruction.",
            "examples": ["point under ball in cart", "spot under ball on rake", "location under ball on towel"]
        },
        {
            "situation": "Relief area limitations",
            "explanation": "Drop within one club-length of the reference point, in the same area of the course, and not nearer to the hole than the reference point.",
            "examples": ["drop in fairway if reference point in fairway", "drop in rough if reference point in rough", "ensure drop is not closer to hole"]
        }
    ]
    },
    {
        "id": "15.2a(3)",
        "title": "Relief When Ball Is in or on Movable Obstruction on Putting Green",
        "text": "The player may take free relief by: Lifting the ball and removing the movable obstruction, and placing the original ball or another ball on the estimated spot right under where the ball was at rest in or on the movable obstruction, using the procedures for replacing a ball under Rule 14.2b(2) and 14.2e.",
        "keywords": ["putting green", "ball in obstruction", "lifting", "removing", "placing", "estimated spot", "replacing procedures"],
        "examples": [
            "ball on rake on green",
            "ball in cup on green",
            "ball on towel on green",
            "ball on scorecard on green"
        ],
        "conditions": [
        {
            "situation": "Ball on movable obstruction on putting green",
            "explanation": "When your ball is in or on a movable obstruction on the putting green, lift the ball, remove the obstruction, and place the ball on the estimated spot where it was resting.",
            "examples": ["ball on rake left on green", "ball sitting on towel on green", "ball resting on scorecard on green"]
        },
        {
            "situation": "Placement procedure",
            "explanation": "Place (don't drop) the ball on the estimated spot right under where it was at rest, following the ball replacement procedures in Rule 14.2.",
            "examples": ["placing ball exactly where it was under obstruction", "using replacement procedures if ball won't stay"]
        }
    ]
    },
    {
        "id": "15.2b",
        "title": "Relief for Ball Not Found but in or on Movable Obstruction",
        "text": "If a player's ball has not been found and it is known or virtually certain that it came to rest in or on a movable obstruction on the course, the player may use this relief option instead of taking stroke-and-distance relief: The player may take free relief under Rule 15.2a(2) or 15.2a(3), using the estimated point right under where the ball last crossed the edge of the movable obstruction on the course as the reference point.",
        "keywords": ["ball not found", "known or virtually certain", "movable obstruction", "relief option", "stroke-and-distance", "last crossed", "edge", "reference point"],
        "examples": [
            "ball lost in large cart",
            "ball disappeared into equipment bag",
            "ball not found but went into obstruction",
            "ball lost in large rake collection"
        ],
        "conditions": [
        {
            "situation": "Ball not found but known to be in obstruction",
            "explanation": "If your ball wasn't found but it's known or virtually certain it came to rest in or on a movable obstruction, you may take relief instead of stroke-and-distance penalty.",
            "examples": ["ball went into cart and wasn't found", "ball clearly went into equipment and disappeared"]
        },
        {
            "situation": "Reference point for relief",
            "explanation": "Use the estimated point where the ball last crossed the edge of the movable obstruction as your reference point for taking relief under Rules 15.2a(2) or 15.2a(3).",
            "examples": ["where ball entered the cart", "point where ball went into equipment bag"]
        },
        {
            "situation": "Original ball no longer in play",
            "explanation": "Once you put another ball in play under this rule, the original ball is no longer in play and must not be played, even if found within the search time.",
            "examples": ["cannot play original ball if found after taking relief", "new ball is now the ball in play"]
        }
    ]
    },
    {
        "id": "15.3",
        "title": "Ball or Ball-Marker Helping or Interfering with Play",
        "text": "If a player believes a ball might help another player's play, the player may mark and lift the ball if it is their own or have any other ball lifted. A player must not lift their ball just because they think it might interfere with another player's play. In stroke play, a player required to lift their ball may play first instead.",
        "keywords": ["helping", "interfering", "play", "mark", "lift", "another player", "believes", "might", "required", "play first"],
        "examples": [
            "ball on line of another player's putt",
            "requesting ball marked on green",
            "ball acting as backstop"
        ]
    },
    {
        "id": "15.3a",
        "title": "Ball on Putting Green Helping Play",
        "text": "If a player reasonably believes that another player's ball might help their own play, the player may have that ball marked and lifted. If a player reasonably believes their own ball might help another player's play, the player may mark and lift their ball. A ball that might help another player's play must not be lifted by the player whose play might be helped.",
        "keywords": ["helping", "another player", "play", "reasonably believes", "marked", "lifted", "must not", "lift", "whose play"],
        "examples": [
            "ball could act as backstop for another player's shot",
            "marking ball that might help opponent",
            "requesting another player's ball be marked",
            "ball near hole acting as potential backstop"
        ],
        "conditions": [
        {
            "situation": "Player believes another ball might help their play",
            "explanation": "If you reasonably believe another player's ball might help your shot (for example, by acting as a backstop), you may request that the other player mark and lift their ball before you play.",
            "examples": ["another player's ball is behind the hole and might stop your ball", "ball on green could deflect your chip shot toward the hole"]
        },
        {
            "situation": "Player believes their ball might help another player",
            "explanation": "If you think your ball might help another player's shot, you may mark and lift it. However, you cannot be required to lift it unless the other player makes the request.",
            "examples": ["your ball is positioned where it might help another player's putt", "your ball could act as a backstop for another player's approach shot"]
        },
        {
            "situation": "Ball must not be lifted by the player who would be helped",
            "explanation": "A player whose play might be helped by another ball is not allowed to lift that ball themselves. Only the owner of the ball or someone acting with their permission may lift it.",
            "examples": ["you cannot mark another player's ball that might help your shot", "asking permission before marking another player's ball"]
        },
        {
            "situation": "In a stroke play match, the player who is required to lift their ball may play first instead",
            "explanation": "In stroke play only, rather than marking their ball at the request of another player, the player may elect to instead play their ball first. In match play, if your opponent asks you to mark and lift your ball under these rules, you must do so and cannot choose to play first instead.",
            "examples": ["in a stroke play event, your ball is positioned where it might help another player's putt", "in stroke play, your ball could act as a backstop for another player's approach shot", "choosing to putt first rather than mark ball"]
        },
          {
            "situation": "In stroke play, two or more players cannot agree to leave a ball in place to benefit a player.",
            "explanation": "In stroke play only, if two or more players agree to leave a ball in place to help any player, and that player then makes a stroke with the helping ball left in place, each player who made the agreement gets a general penalty of 2 strokes.",
            "examples": ["protecting the field", "two players try to help their playing partner by leaving a ball in place that could help the playing partner"]
        }
        ]
    },
    {
        "id": "15.3b",
        "title": "Ball Anywhere on Course Interfering with Play",
        "text": "If a player reasonably believes that another player's ball might interfere with their own play, the player may require the other player to mark and lift their ball. But the player must not make this request if there is no reasonable basis for thinking the other player's ball might interfere with their own play.",
        "keywords": ["interfering", "another player", "play", "reasonably believes", "mark", "lift", "must not", "no reasonable basis"],
        "examples": [
            "another player's ball in line of play",
            "another player's ball in my stance area",
            "another player's ball too close to own ball",
            "ball interfering with putting line"
        ],
        "conditions": [ 
        {
            "situation": "Another player's ball may interfere with own play",
            "explanation": "If you reasonably believe another player's ball might interfere with your own stroke, stance, or swing, you may require that the other player mark and lift it. This includes situations where their ball is on your line of play or in your intended stance area.",
            "examples": ["another player's ball is on your putting line", "another player's ball is so close that I might accidentally hit it", "another player's ball is where you need to stand", "another player's ball is close enough to distract you"]
        },
        {
            "situation": "No reasonable basis for interference",
            "explanation": "You must not lift your ball unless there is a reasonable basis for believing it might interfere. Simply being visible to another player or being generally in the area is not sufficient grounds for lifting.",
            "examples": ["ball is far from another player's line", "ball would not affect another player's stance or swing", "lifting ball when there's no real interference"]
        },
        {
            "situation": "No cleaning the ball",
            "explanation": "When a player is required to mark the spot and lift their ball anywhere on the course other than the putting green, the ball must not be cleaned and must be returned to its original spot.",
            "examples": ["clean the ball", "return to original spot", "no club length relief"]
        }
        ]
    },
    {
        "id": "15.3c",
        "title": "Ball-Marker Helping or Interfering with Play",
        "text": "If a ball-marker might help or interfere with play, a player may: Move the ball-marker out of the way if it is their own, or if the ball-marker belongs to another player, require that player to move the ball-marker out of the way, for the same reasons as they may require a ball to be lifted under Rules 15.3a and 15.3b. The ball-marker must be moved out of the way to a new spot measured from its original spot, such as by using one or more clubhead-lengths. When moving the ball-marker back, the player should do so by measuring from the new spot and reversing the steps used to move the ball-marker out of the way. The same process should be applied if a player moved an interfering ball out of the way by measuring from the ball.",
        "keywords": ["ball-marker", "helping", "interfering", "play", "move", "out of the way", "clubhead-lengths", "measure", "new spot", "original spot", "reversing", "moved"],
        "examples": [
            "ball marker on another player's putting line",
            "moving ball marker one club length to the side",
            "measuring to move marker out of the way",
            "returning marker to original position",
            "ball marker interfering with stance"
        ],
        "conditions": [
        {
            "situation": "Moving your own ball-marker",
            "explanation": "If your ball-marker might help or interfere with another player's play, you may move it out of the way by measuring one or more clubhead-lengths to a new spot away from the line of play or stance area.",
            "examples": ["your marker is on another player's putting line", "marker is where another player needs to stand", "marker could help deflect another player's ball"]
        },
        {
            "situation": "Requesting another player move their ball-marker",
            "explanation": "You may require another player to move their ball-marker if it might help or interfere with your play, using the same criteria as for requiring a ball to be lifted under Rules 15.3a and 15.3b.",
            "examples": ["another player's marker is on your putting line", "marker interferes with your stance", "marker might help your ball stay near the hole"]
        },
        {
            "situation": "Proper measurement procedure",
            "explanation": "The ball-marker must be moved by measuring from its original spot to a new location (typically one or more clubhead-lengths). When replacing, measure from the new spot back to the original position using the reverse of the same steps.",
            "examples": ["measure one putter length to the right", "use two club lengths if one isn't enough", "return by measuring back from temporary position"]
        },
        {
            "situation": "Same process applies to moved balls",
            "explanation": "If you moved an interfering ball out of the way by measuring (rather than lifting and marking), the same measurement and replacement procedure should be used.",
            "examples": ["ball moved by measuring rather than marking", "returning moved ball to exact original position", "using consistent measurement method"]
        }
    ]
    },

    # --- Section 16: Relief from Abnormal Course Conditions ---
    {
        "id": "16.1",
        "title": "Abnormal Course Conditions (Including Immovable Obstructions)",
        "text": "When a player's ball lies in or touches an abnormal course condition or when an abnormal course condition physically interferes with the player's area of intended stance or area of intended swing, the player may take free relief by dropping the original ball or another ball in the relief area.",
        "keywords": ["abnormal course condition", "standing water", "puddle", "sprinkler head", "cart path", "casual water", "temporary water", "ground under repair", "immovable obstruction", "animal hole", "lies in", "touches", "physically interferes", "stance", "swing", "free relief", "drop", "relief area"],
        "examples": [
            "ball in casual water",
            "relief from cart path",
            "ground under repair rules",
            "ball in puddle",
            "ball in animal hole",
            "ground under repair",
            "standing on sprinkler head",
            "standing on cart path",
            "ball on cart path"
        ]
    },
    {
        "id": "16.1a",
        "title": "When Relief Is Allowed from Abnormal Course Conditions",
        "text": "Interference exists when any one of these is true: (1) The player's ball touches or is in or on an abnormal course condition, (2) An abnormal course condition physically interferes with the player's area of intended stance or area of intended swing, or (3) Only when the ball is on the putting green, an abnormal course condition on or off the putting green intervenes on the line of play.",
        "keywords": ["interference", "touches", "in", "on", "physically", "intended stance",  "intended swing", "putting green", "intervenes", "line of play", "abnormal course condition", "relief", "allowed", "casual water", "ground under repair", "animal hole", "immovable obstruction"
        ],
        "examples": [
        "when can I take relief from abnormal condition",
        "cart path interfering with stance",
        "ground under repair blocking line of putt",
        "ball in casual water",
        "sprinkler head on line of putt",
        "ball touching ground under repair",
        "animal hole interfering with swing"
        ],
    "conditions": [
        {
            "situation": "Ball touches or is in/on abnormal condition",
            "explanation": "Relief is allowed when your ball is touching, sitting in, or on top of any abnormal course condition including casual water, ground under repair, animal holes, or immovable obstructions like cart paths, sprinkler heads, or artificially surfaced roads.",
            "examples": ["ball sitting in puddle", "ball on cart path", "ball touching ground under repair stake"]
        },
        {
            "situation": "Abnormal condition interferes with stance or swing",
            "explanation": "Relief is allowed when an abnormal course condition physically interferes with where you intend to stand or swing, even if your ball isn't in or touching the condition. This includes situations where you would need to stand in casual water or on a cart path to play your shot.",
            "examples": ["need to stand on cart path", "swing would hit sprinkler head", "standing in casual water"]
        },
        {
            "situation": "Abnormal condition intervenes on putting line",
            "explanation": "When your ball is on the putting green only, you may take relief if an abnormal course condition (on or off the green) is on your line of play. This includes situations like ground under repair or a sprinkler head being between your ball and the hole.",
            "examples": ["sprinkler between ball and hole on green", "ground under repair on line of putt", "drainage grate affecting putt line"]
        },
        {
            "situation": "Exceptions - When relief is NOT allowed",
            "explanation": "Relief is not allowed when an abnormal course condition only interferes with your play because of something other than the situations above. Relief is also not allowed when the ball is in a penalty area. Relief is also not allowed when interference is clearly unreasonable to play your ball because of something else (like severe lie in rough or a tree between your ball and the hole).",
            "examples": ["tree between ball and hole", "abnormal condition only affecting line of play for ball in general area", "ball in penalty area", "only reasonable play is in different direction from condition"]
        }
    ]
    },
    {
        "id": "16.1b",
        "title": "Relief for Ball in General Area",
        "text": "If the player's ball is in the general area and there is interference by an abnormal course condition, the player may take free relief by dropping the original ball or another ball in this relief area: Reference Point: The nearest point of complete relief in the general area. Size of Relief Area: One club-length from the reference point, but with these limits: Limits on Location of Relief Area: Must be in the general area, must not be nearer the hole than the reference point, and there must be complete relief from all interference by the abnormal course condition.",
        "keywords": ["general area", "free relief", "complete relief", "nearest point", "reference point", "one club-length", "not nearer hole", "dropping", "original ball", "another ball"],
        "examples": [
            "relief from cart path in fairway",
            "nearest point of complete relief",
            "how to measure one club length for relief"
        ]
    },
    {
        "id": "16.1c",
        "title": "Relief for Ball in Bunker",
        "text": "If the player's ball is in a bunker and there is interference by an abnormal course condition, the player may take either (1) Free Relief: Under Rule 16.1b, except that the nearest point of complete relief must be in the bunker and the ball must be dropped in the bunker, or (2) Penalty Relief: For one penalty stroke, the player may drop a ball outside the bunker keeping the point where the ball would have come to rest directly between the hole and the spot where the ball is dropped.",
        "keywords": ["bunker", "sand trap", "free relief", "penalty relief", "one stroke penalty", "outside bunker", "nearest point", "complete relief", "back-on-the-line", "dropped"],
        "examples": [
            "water in bunker relief options",
            "casual water in sand trap",
            "puddle in the bunker",
            "taking relief outside bunker with penalty"
        ],
        "conditions": [
        {
            "situation": "There is no such nearest point of complete relief",
            "explanation": "Relief is allowed using the point of maximum available relief, which is the estimated point where the ball would lie that is: 1) nearest to the ball's original spot, but not nearer to the hole in that spot, 2) in the required area of the course, in this case the bunker, and 3) where that abnormal course condition least interferes with the stroke the player would have made from the original spot if the condition was not there.",
            "examples": ["ball is in a puddle that encompasses the majority of the bunker whereby there is no point of complete relief, the player may take relief at the point of maximum available relief, which may be a shallower part of the puddle"]
    }
        ]
    },
    {
        "id": "16.1d",
        "title": "Relief for Ball on Putting Green",
        "text": "If the player's ball is on the putting green and there is interference by an abnormal course condition, the player may take free relief by placing the original ball or another ball on the spot of the nearest point of complete relief, which must be either on the putting green or in the general area.",
        "keywords": ["putting green", "free relief", "place", "nearest point", "complete relief", "place", "original ball", "another ball", "general area"],
        "examples": [
            "casual water on putting green",
            "place ball at nearest point of relief on green",
            "abnormal conditions affecting putt line"
        ],
        "conditions": [
        {
            "situation": "There is no such nearest point of complete relief",
            "explanation": "The player may take relief using the point of maximum available relief, which is the estimated point where the ball would lie that is: 1) nearest to the ball's original spot, but not nearer to the hole in that spot, 2) in the required area of the course, in this case on the green or in the general area, and 3) where that abnormal course condition least interferes with the stroke the player would have made from the original spot if the condition was not there.",
            "examples": ["an obstruction encompasses the entire area whereby the player has no unobstructed line to the hole and therefore no point of complete relief, the player may take relief at the point of maximum available relief, which may still include the obstruction but to a lesser degree."]
    }
        ]
    },
    {
        "id": "16.1e",
        "title": "Relief for Ball Not Found but in or on Abnormal Course Condition",
        "text": "If the player's ball has not been found and it is known or virtually certain that the ball came to rest in or on an abnormal course condition, the player may use this relief option instead of taking stroke-and-distance relief. The player may take relief under 16.1b, c or d, using the estimated point where the ball last crossed the edge of the abnormal course condition as the spot of the ball for finding the nearest point of complete relief.",
        "keywords": ["not found", "known or virtually certain", "came to rest", "estimated point", "last crossed", "edge", "instead of", "stroke-and-distance", "nearest point", "complete relief"],
        "examples": [
            "ball lost in ground under repair",
            "ball disappeared into casual water",
            "taking relief when ball not found in abnormal condition"
        ]
    },
    {
        "id": "16.2",
        "title": "Dangerous Animal Condition",
        "text": "A 'dangerous animal condition' exists when a dangerous animal (like venomous snakes, stinging bees, alligators, fire ants or bears) near a ball could cause serious physical injury to the player if they had to play the ball as it lies. A player may take relief from interference by a dangerous animal condition no matter where their ball is on the course.",
        "keywords": ["dangerous animal condition", "venomous snakes", "stinging bees", "alligators", "fire ants", "bears", "serious physical injury", "relief", "anywhere on course"],
        "examples": [
            "snake near golf ball",
            "bee hive by ball",
            "alligator near ball",
            "dangerous animal relief options"
        ]
    },
    {
        "id": "16.2a",
        "title": "When Relief Is Allowed",
        "text": "A 'dangerous animal condition' exists when a dangerous animal near a ball could cause serious physical injury to the player if they had to play the ball as it lies. A player may take relief under Rule 16.2b from interference by a dangerous animal condition no matter where their ball is on the course. This Rule does not apply to other situations that could cause physical harm.",
        "keywords": ["when relief allowed", "dangerous animal", "serious physical injury", "play ball as lies", "anywhere on course", "not apply", "other situations", "physical harm"],
        "examples": [
            "snake threatening player safety",
            "bee nest creating danger",
            "relief allowed anywhere on course",
            "cactus not covered by rule"
        ],
    "conditions": [
        {
            "situation": "Definition of dangerous animal condition",
            "explanation": "Under Rule 16.2a, a 'dangerous animal condition' exists when a dangerous animal (such as venomous snakes, stinging bees, alligators, fire ants or bears) near a ball could cause serious physical injury to the player if they had to play the ball as it lies.",
            "examples": ["venomous snakes", "stinging bees", "alligators", "fire ants", "bears", "serious physical injury threat"]
        },
        {
            "situation": "Relief allowed anywhere on course",
            "explanation": "Under Rule 16.2a, a player may take relief under Rule 16.2b from interference by a dangerous animal condition no matter where their ball is on the course.",
            "examples": ["general area", "bunker", "putting green", "penalty area", "anywhere on course"]
        },
        {
            "situation": "Rule does not apply to other hazardous situations",
            "explanation": "Under Rule 16.2a, this Rule does not apply to other situations on the course that could cause physical harm (such as a cactus).",
            "examples": ["cactus not covered", "other physical hazards", "non-animal dangers", "different relief rules may apply"]
        }
    ]
    },
    {
        "id": "16.2b",
        "title": "Relief for Dangerous Animal Condition",
        "text": "When there is interference by a dangerous animal condition, relief options depend on where the ball lies. Different procedures apply for balls in the general area, bunker, putting green, or penalty area. Free relief is not allowed when playing the ball is clearly unreasonable for other reasons or when interference exists only because of unreasonable choices.",
        "keywords": ["relief", "dangerous animal condition", "interference", "depends where ball lies", "general area", "bunker", "putting green", "penalty area", "free relief not allowed", "clearly unreasonable"],
        "examples": [
            "relief options by ball location",
            "free relief in general area",
            "penalty area relief choices",
            "no relief when unreasonable"
        ],
        "conditions": [
        {
            "situation": "Relief when ball is anywhere except penalty area",
            "explanation": "Under Rule 16.2b(1), when ball is anywhere except penalty area, the player may take relief under Rule 16.1b, c or d, depending on whether the ball is in the general area, in a bunker or on the putting green.",
            "examples": ["general area use Rule 16.1b", "bunker use Rule 16.1c", "putting green use Rule 16.1d", "follow normal abnormal condition relief"]
        },
        {
            "situation": "Free relief when ball is in penalty area",
            "explanation": "Under Rule 16.2b(2), when ball is in penalty area, player may take free relief under Rule 16.1b, except that the nearest point of complete relief and the relief area must be in the penalty area.",
            "examples": ["free relief in penalty area", "nearest point in penalty area", "relief area in penalty area", "stay within penalty area"]
        },
        {
            "situation": "Penalty relief when ball is in penalty area",
            "explanation": "Under Rule 16.2b(2), when ball is in penalty area, player may take penalty relief under Rule 17.1d. If there is interference by dangerous animal condition where ball would be played after taking this penalty relief outside the penalty area, player may take further relief under Rule 16.2b(1) without additional penalty.",
            "examples": ["penalty relief under Rule 17.1d", "relief outside penalty area", "further relief if still dangerous", "no additional penalty"]
        },
        {
            "situation": "No free relief when clearly unreasonable to play ball",
            "explanation": "Under Rule 16.2b(3), there is no free relief when: playing the ball as it lies is clearly unreasonable because of something from which the player is not allowed to take free relief (such as when unable to make a stroke because of where ball lies in a bush), or when interference exists only because player chooses a club, type of stance or swing or direction of play that is clearly unreasonable under the circumstances.",
            "examples": ["ball in bush unplayable", "unreasonable club choice", "unreasonable stance", "unreasonable swing direction"]
        },
        {
            "situation": "Definition of nearest point of complete relief",
            "explanation": "Under Rule 16.2b, for purposes of this Rule, the 'nearest point of complete relief' means the nearest point (not nearer the hole) where the dangerous animal condition does not exist.",
            "examples": ["nearest point no danger", "not nearer to hole", "where animal condition doesn't exist", "complete relief from danger"]
        },
        {
            "situation": "Penalty for playing from wrong place",
            "explanation": "Under Rule 16.2, penalty for Playing Ball from a Wrong Place in Breach of Rule 16.2: General Penalty Under Rule 14.7a.",
            "examples": ["wrong place penalty", "general penalty", "Rule 14.7a", "two strokes or loss of hole"]
        }
    ]
    },
    {
        "id": "16.3",
        "title": "Embedded Ball",
        "text": "When a player's ball is embedded in the general area, the player may take free relief by dropping the original ball or another ball in the relief area directly behind where the ball was embedded, within one club-length of the reference point and in the general area.",
        "keywords": ["embedded", "ball", "general area", "free relief", "drop", "behind", "relief area", "one club-length", "reference point"],
        "examples": [
            "ball plugged in fairway",
            "embedded ball relief procedure",
            "when is a ball considered embedded"
        ],
        "conditions": [
        {
            "situation": "When relief is allowed for embedded ball",
            "explanation": "Under Rule 16.3a(1), relief is allowed only when a player's ball is embedded in the general area. There is no relief under this Rule if the ball is embedded anywhere except in the general area.",
            "examples": ["ball embedded in fairway", "ball embedded in rough", "no relief in bunker if embedded", "no relief in penalty area if embedded"]
        },
        {
            "situation": "Embedded ball on putting green",
            "explanation": "Under Rule 16.3a(1), if the ball is embedded on the putting green, the player may mark the spot of the ball and lift and clean the ball, repair the damage caused by the ball's impact, and replace the ball on its original spot (see Rule 13.1c(2)).",
            "examples": ["ball embedded on green", "mark lift clean repair replace", "repair ball impact damage", "putting green embedded ball procedure"]
        },
        {
            "situation": "Exception - embedded in sand not cut to fairway height",
            "explanation": "Under Rule 16.3a(1), there is no relief when the ball is embedded in sand in a part of the general area that is not cut to fairway height or less.",
            "examples": ["embedded in sand in rough", "sand area not cut short", "no relief in uncut sand areas", "fairway height requirement"]
        },
        {
            "situation": "Exception - clearly unreasonable to play",
            "explanation": "Under Rule 16.3a(1), there is no relief when playing the ball as it lies is clearly unreasonable because of something from which the player is not allowed to take free relief (such as when unable to make a stroke because of where the ball lies in a bush).",
            "examples": ["ball embedded in bush", "unreasonable to play", "cannot make stroke", "no free relief available"]
        },
        {
            "situation": "Definition of embedded ball",
            "explanation": "Under Rule 16.3a(2), a player's ball is embedded only if it is in its own pitch-mark made as a result of the player's previous stroke, and part of the ball is below the level of the ground.",
            "examples": ["in own pitch-mark", "from previous stroke", "part below ground level", "ball's own impact mark"]
        },
        {
            "situation": "Uncertain if ball is in own pitch-mark",
            "explanation": "Under Rule 16.3a(2), if the player cannot tell for sure whether the ball is in its own pitch-mark or a pitch-mark made by another ball, the player may treat the ball as embedded if it is reasonable to conclude from the available information that the ball is in its own pitch-mark.",
            "examples": ["uncertainty about pitch-mark", "reasonable to conclude", "available information", "may treat as embedded"]
        },
        {
            "situation": "When ball is not considered embedded",
            "explanation": "Under Rule 16.3a(2), a ball is not embedded if it is below the level of the ground as a result of anything other than the player's previous stroke, such as when pushed into ground by stepping, driven straight without becoming airborne, or dropped in taking relief.",
            "examples": ["stepped on and pushed down", "driven straight into ground", "ball dropped in relief", "not from previous stroke"]
        },
        {
            "situation": "Relief procedure for embedded ball",
            "explanation": "Under Rule 16.3b, when relief is allowed, player may take free relief by dropping the original ball or another ball in relief area with reference point at spot right behind where ball is embedded, within one club-length, in general area, not nearer the hole.",
            "examples": ["drop behind embedded ball", "one club-length relief", "in general area", "not nearer hole"]
        },
        {
            "situation": "Committee Local Rule option",
            "explanation": "Under Rule 16.3b, the Committee may adopt a Local Rule allowing relief only for a ball embedded in an area cut to fairway height or less (Model Local Rule F-2).",
            "examples": ["committee local rule", "fairway height only", "Model Local Rule F-2", "restricted embedded relief"]
        },
        {
            "situation": "Penalty for wrong place",
            "explanation": "Under Rule 16.3, penalty for playing ball from wrong place in breach of Rule 16.3 is general penalty under Rule 14.7a.",
            "examples": ["wrong place penalty", "general penalty", "Rule 14.7a", "two strokes or loss of hole"]
        }
    ]
    },
    {
        "id": "16.4",
        "title": "Lifting Ball to See If It Lies in Condition Where Relief Allowed",
        "text": "If a player reasonably believes their ball lies in a condition where free relief is allowed but cannot decide without lifting the ball, the player may mark and lift the ball to see if relief is allowed. The lifted ball must not be cleaned except to the extent necessary to see if it lies in the condition.",
        "keywords": ["lift", "see", "condition", "relief", "allowed", "reasonably believes", "mark", "not cleaned", "necessary", "extent"],
        "examples": [
            "lifting ball to check for damage",
            "checking if ball is in ground under repair",
            "cleaning restrictions when checking condition"
        ],
        "conditions": [
        {
            "situation": "When lifting is allowed to check for relief conditions",
            "explanation": "Under Rule 16.4, if a player reasonably believes that their ball lies in a condition where free relief is allowed under Rule 15.2 (movable obstructions), 16.1 (abnormal course conditions) or 16.3 (embedded ball), but cannot decide without lifting the ball, the player may lift the ball to see if relief is allowed.",
            "examples": ["reasonably believes relief available", "cannot decide without lifting", "Rules 15.2, 16.1, or 16.3", "may lift to check"]
        },
        {
            "situation": "Requirements when lifting to check conditions",
            "explanation": "Under Rule 16.4, when lifting to check conditions, the spot of the ball must first be marked, and the lifted ball must not be cleaned (except on the putting green) (see Rule 14.1).",
            "examples": ["must mark spot first", "cannot clean ball", "except on putting green", "follow Rule 14.1"]
        },
        {
            "situation": "Penalty for lifting without reasonable belief",
            "explanation": "Under Rule 16.4, if the player lifts the ball without having reasonable belief that relief is allowed (except on the putting green where the player may lift under Rule 13.1b), they get one penalty stroke.",
            "examples": ["no reasonable belief", "one penalty stroke", "putting green exception", "Rule 13.1b allows lifting"]
        },
        {
            "situation": "No penalty when relief is taken",
            "explanation": "Under Rule 16.4, if relief is allowed and the player takes relief, there is no penalty even if the player did not mark the spot of the ball before lifting it or cleaned the lifted ball.",
            "examples": ["relief allowed and taken", "no penalty", "marking not required if relief taken", "cleaning allowed if relief taken"]
        },
        {
            "situation": "Penalties when relief not allowed or not taken",
            "explanation": "Under Rule 16.4, if relief is not allowed, or if the player chooses not to take relief that is allowed: the player gets one penalty stroke if they did not mark the spot of the ball before lifting it or cleaned the lifted ball when not allowed, and the ball must be replaced on its original spot.",
            "examples": ["relief not allowed", "chose not to take relief", "one penalty for improper procedure", "must replace on original spot"]
        },
        {
            "situation": "Ball replacement requirement",
            "explanation": "Under Rule 16.4, when relief is not allowed or not taken, the ball must be replaced on its original spot (see Rule 14.2).",
            "examples": ["must replace ball", "original spot", "Rule 14.2 procedures", "replacement required"]
        },
        {
            "situation": "Penalty for wrong place",
            "explanation": "Under Rule 16.4, penalty for playing ball from wrong place in breach of Rule 16.4 is general penalty under Rule 14.7a.",
            "examples": ["wrong place penalty", "general penalty", "Rule 14.7a", "two strokes or loss of hole"]
        }
    ]
    },

    # --- Section 17: Penalty Areas ---
    {
        "id": "17.1",
        "title": "Options for Ball in Penalty Area",
        "text": "Penalty areas are defined as either red or yellow. This affects the player's relief options (see Rule 17.1d). A player may stand in a penalty area to play a ball outside the penalty area, including after taking relief from the penalty area.",
        "keywords": ["penalty area", "red", "yellow", "relief options", "stand in penalty area", "ball outside", "water hazard"],
        "examples": [
            "ball in water hazard",
            "red vs yellow stakes difference",
            "options for penalty area",
            "standing in water to play ball",
            "penalty area relief"
        ]
    },
    {
        "id": "17.1a",
        "title": "When Ball Is in Penalty Area",
        "text": "A ball is in a penalty area when any part of the ball: Lies on or touches the ground or anything else (such as any natural or artificial object) inside the edge of the penalty area, or Is above the edge or any other part of the penalty area. If part of the ball is both in a penalty area and in another area of the course, see Rule 2.2c.",
        "keywords": ["ball in penalty area", "any part", "lies on", "touches", "ground", "inside edge", "above edge", "natural object", "artificial object"],
        "examples": [
            "determining if ball is in penalty area",
            "ball touching water",
            "ball above penalty area",
            "part of ball in hazard"
        ],
        "conditions": [
        {
            "situation": "How to determine if ball is in penalty area",
            "explanation": "Under Rule 17.1a, a ball is in a penalty area when any part of the ball lies on or touches the ground or anything else inside the edge of the penalty area, or is above the edge or any other part of the penalty area.",
            "examples": ["any part touching counts", "ball on edge of water", "ball above penalty area", "touching objects in penalty area"]
        },
        {
            "situation": "Ball touching penalty area boundary",
            "explanation": "Under Rule 17.1a, if any part of the ball touches or lies on anything inside the edge of the penalty area, the ball is considered to be in the penalty area, even if most of the ball is outside.",
            "examples": ["ball barely touching water", "small part in penalty area", "ball on penalty area line", "edge contact counts"]
        },
        {
            "situation": "Ball above penalty area",
            "explanation": "Under Rule 17.1a, a ball is in a penalty area if it is above the edge or any other part of the penalty area, such as when lodged in a tree above water or resting on a bridge over water.",
            "examples": ["ball in tree above water", "ball on bridge over penalty area", "ball stuck above hazard", "vertical penalty area boundaries"]
        },
        {
            "situation": "Ball partly in penalty area and partly in another area",
            "explanation": "Under Rule 17.1a, if part of the ball is in a penalty area and part is in another area of the course, Rule 2.2c applies where the ball is considered in the penalty area.",
            "examples": ["ball straddling penalty area line", "part in water part on bank", "mixed area situations", "refer to Rule 2.2c", "when ball is touching the penalty line, it is consisidered in the penalty area."]
        },
    ]
    },  
    {
        "id": "17.1b",
        "title": "Player May Play Ball as It Lies in Penalty Area or Take Penalty Relief",
        "text": "The player may either: Play the ball as it lies without penalty, under the same Rules that apply to a ball in the general area (which means there are no special Rules limiting how a ball may be played from a penalty area), or Play a ball from outside the penalty area by taking penalty relief under Rule 17.1d or 17.2. Exception – Relief Must Be Taken from Interference by No Play Zone in Penalty Area (see Rule 17.1e).",
        "keywords": ["play as it lies", "without penalty", "general area rules", "no special rules", "penalty relief", "outside penalty area", "no play zone"],
        "examples": [
            "playing ball from water",
            "no penalty to play from penalty area",
            "same rules as general area",
            "taking relief from penalty area"
        ],
        "conditions": [
        {
            "situation": "Can I play my ball from the penalty area without penalty",
            "explanation": "Under Rule 17.1b, you may play the ball as it lies in a penalty area without penalty. The same rules apply as in the general area, meaning there are no special restrictions on how you play from a penalty area.",
            "examples": ["no penalty to play from water", "same rules as fairway", "can ground club in penalty area", "no special restrictions"]
        },
        {
            "situation": "What are my relief options from penalty area",
            "explanation": "Under Rule 17.1b, you may take penalty relief by playing a ball from outside the penalty area under Rule 17.1d (stroke-and-distance, back-on-line, or lateral relief) or Rule 17.2 (after playing from penalty area).",
            "examples": ["stroke and distance relief", "back on line relief", "lateral relief option", "play from outside penalty area"]
        },
        {
            "situation": "Are there special rules for playing from penalty areas",
            "explanation": "Under Rule 17.1b, there are no special rules limiting how a ball may be played from a penalty area. You can ground your club, remove loose impediments, and play normally, just like in the general area.",
            "examples": ["can ground club in penalty area", "can remove leaves and twigs", "no special restrictions", "treat like general area"]
        },
         {
            "situation": "Can I ground the club in a penalty area",
            "explanation": "Under Rule 17.1b, there are no special rules limiting how a ball may be played from a penalty area. You can ground your club, remove loose impediments, and play normally, just like in the general area.",
            "examples": ["ground club in penalty area", "remove leaves and twigs", "no special restrictions", "treat like general area"]
        },
        {
            "situation": "Exception for no play zones in penalty area",
            "explanation": "Under Rule 17.1b exception, if there is a no play zone in the penalty area, you must take relief and cannot play the ball as it lies. See Rule 17.1e for specific procedures.",
            "examples": ["must take relief from no play zone", "cannot play from no play zone", "see Rule 17.1e", "exception to playing as it lies"]
        }
    ]
    },
    {
        "id": "17.1c",
        "title": "Relief for Ball Not Found but in Penalty Area",
        "text": "If a player's ball has not been found and it is known or virtually certain that the ball came to rest in a penalty area: The player may take penalty relief under Rule 17.1d or 17.2. Once the player puts another ball in play to take relief in this way: The original ball is no longer in play and must not be played. This is true even if it is then found on the course before the end of the three-minute search time (see Rule 6.3b). But if it is not known or virtually certain that the ball came to rest in a penalty area and the ball is lost, the player must take stroke-and-distance relief under Rule 18.2.",
        "keywords": ["ball not found", "known or virtually certain", "penalty area", "penalty relief", "original ball no longer in play", "three-minute search", "stroke-and-distance"],
        "examples": [
            "ball lost in water hazard",
            "ball disappeared into penalty area",
            "taking relief when ball not found",
            "cannot play original ball if found later"
        ],
        "conditions": [
        {
            "situation": "Ball not found but known to be in penalty area",
            "explanation": "Under Rule 17.1c, if your ball hasn't been found but it's known or virtually certain it came to rest in a penalty area, you may take penalty relief under Rule 17.1d or 17.2 instead of stroke-and-distance relief.",
            "examples": ["ball clearly went into water", "saw ball enter penalty area", "virtually certain in hazard", "relief options available"]
        },
        {
            "situation": "Original ball found after taking relief",
            "explanation": "Under Rule 17.1c, once you put another ball in play to take relief for a ball known or virtually certain to be in a penalty area, the original ball is no longer in play and must not be played, even if found before the three-minute search time ends.",
            "examples": ["cannot play original if found later", "new ball is now in play", "original ball out of play", "no switching back to original"]
        },
        {
            "situation": "Not certain ball is in penalty area",
            "explanation": "Under Rule 17.1c, if it's not known or virtually certain that the ball came to rest in a penalty area and the ball is lost, you must take stroke-and-distance relief under Rule 18.2 instead of penalty area relief.",
            "examples": ["uncertainty about penalty area", "might be lost elsewhere", "must use stroke and distance", "no penalty area relief available"]
        },
        {
            "situation": "What does known or virtually certain mean",
            "explanation": "Under Rule 17.1c, known or virtually certain means there's conclusive evidence the ball went into the penalty area, such as seeing it go in, hearing a splash, or finding it's the only reasonable place the ball could be.",
            "examples": ["saw ball splash into water", "heard ball hit water", "only possible location", "conclusive evidence required"]
        }
    ]
    },
    {
        "id": "17.1d",
        "title": "Relief for Ball in Penalty Area",
        "text": "If a player's ball is in a penalty area, including when it is known or virtually certain to be in a penalty area even though not found, the player has these relief options, each for one penalty stroke: (1) Stroke-and-Distance Relief, (2) Back-on-the-Line Relief, (3) Lateral Relief (Only for Red Penalty Area).",
        "keywords": ["relief options", "one penalty stroke", "stroke-and-distance", "back-on-the-line", "lateral relief", "red penalty area", "yellow penalty area"],
        "examples": [
            "penalty area relief options",
            "one stroke penalty relief",
            "red vs yellow penalty area options",
            "back on line relief",
            "lateral relief for red stakes"
        ],
        "conditions": [
        {
            "situation": "Stroke-and-distance relief from penalty area",
            "explanation": "Under Rule 17.1d(1), you may play the original ball or another ball from where the previous stroke was made (see Rule 14.6). This option is available for both red and yellow penalty areas with one penalty stroke.",
            "examples": ["play from previous spot", "go back to tee", "replay from fairway", "one stroke penalty"]
        },
        {
            "situation": "Back-on-the-line relief from penalty area",
            "explanation": "Under Rule 17.1d(2), you may drop outside the penalty area, keeping the point where the ball last crossed the penalty area edge between the hole and where you drop, with no limit on how far back. Available for both red and yellow penalty areas.",
            "examples": ["drop on line back from hole", "no limit how far back", "keep crossing point between ball and hole", "both red and yellow areas"]
        },
        {
            "situation": "Back-on-line relief area specifics",
            "explanation": "Under Rule 17.1d(2), when you drop on the back-on-line, the spot where the ball first touches the ground creates a relief area one club-length in any direction, but not nearer the hole than the crossing point and must be in the same area where the ball first touched.",
            "examples": ["one club-length relief area", "not nearer than crossing point", "same area as first touch", "relief area created by drop"]
        },
        {
            "situation": "Lateral relief for red penalty areas only",
            "explanation": "Under Rule 17.1d(3), when the ball last crossed a red penalty area, you may drop within two club-lengths of the crossing point, not nearer the hole, in any area except the same penalty area. This option is only available for red penalty areas.",
            "examples": ["red penalty areas only", "two club-lengths from crossing point", "not nearer to hole", "any area except same penalty area"]
        },
        {
            "situation": "Lateral relief area limitations",
            "explanation": "Under Rule 17.1d(3), for lateral relief the ball must come to rest in the same area of the course that it first touched when dropped in the relief area, if multiple areas are within two club-lengths of the reference point.",
            "examples": ["same area as first touch", "multiple areas within two club-lengths", "area consistency requirement", "where ball first touches matters"]
        },
        {
            "situation": "Which relief options are available for yellow vs red penalty areas",
            "explanation": "Under Rule 17.1d, yellow penalty areas have two relief options: stroke-and-distance and back-on-the-line. Red penalty areas have three options: stroke-and-distance, back-on-the-line, and lateral relief.",
            "examples": ["yellow: two options only", "red: three options available", "lateral relief only for red", "back-on-line for both colors"]
        }
    ]
    },
    {
        "id": "17.1e",
        "title": "Relief Must Be Taken from Interference by No Play Zone in Penalty Area",
        "text": "In each of these situations, the player must not play the ball as it lies: (1) When Ball Is in No Play Zone in Penalty Area, (2) When No Play Zone on Course Interferes with Stance or Swing for Ball in Penalty Area, (3) No Relief When Clearly Unreasonable.",
        "keywords": ["no play zone", "must not play", "penalty area", "interference", "stance", "swing", "clearly unreasonable"],
        "examples": [
            "ball in no play zone",
            "no play zone interfering with stance",
            "mandatory relief from no play zone",
            "environmentally sensitive area"
        ],
        "conditions": [
        {
            "situation": "Ball in no play zone within penalty area",
            "explanation": "Under Rule 17.1e(1), when your ball is in a no play zone in a penalty area, you must not play the ball as it lies and must take penalty relief under Rule 17.1d or 17.2.",
            "examples": ["ball in environmentally sensitive area", "must take penalty relief", "cannot play from no play zone", "mandatory relief required"]
        },
        {
            "situation": "No play zone interferes with stance or swing",
            "explanation": "Under Rule 17.1e(2), if your ball is in a penalty area outside a no play zone, but a no play zone interferes with your stance or swing area, you must either take penalty relief outside the penalty area or take free relief within the penalty area.",
            "examples": ["stance in no play zone", "swing would contact no play zone", "two relief options available", "penalty relief or free relief"]
        },
        {
            "situation": "Free relief within penalty area from no play zone",
            "explanation": "Under Rule 17.1e(2), you may take free relief by dropping within the penalty area at the nearest point of complete relief from the no play zone, within one club-length, in the same penalty area, not nearer the hole.",
            "examples": ["free relief option in penalty area", "nearest point of complete relief", "one club-length relief area", "same penalty area"]
        },
        {
            "situation": "No relief when clearly unreasonable",
            "explanation": "Under Rule 17.1e(3), there is no free relief from no play zone interference when playing would be clearly unreasonable for other reasons (like ball in bush) or when interference exists only because of unreasonable club/stance choice.",
            "examples": ["ball unplayable for other reasons", "unreasonable club selection", "interference from unreasonable stance", "no relief when clearly unreasonable"]
        },
        {
            "situation": "Further relief after taking relief from no play zone",
            "explanation": "Under Rule 17.1e(1), if you still have interference from a no play zone after taking relief under this rule, you must take further relief under Rule 16.1f(2) and cannot play the ball as it lies.",
            "examples": ["continued no play zone interference", "further relief required", "see Rule 16.1f(2)", "cannot play with continued interference"]
        }
    ]
    },
    {
        "id": "17.1 Penalty",
        "title": "Penalty for Playing Ball from Wrong Place in Breach of Rule 17.1",
        "text": "Penalty for Playing Ball from a Wrong Place in Breach of Rule 17.1: General Penalty Under Rule 14.7a.",
        "keywords": ["penalty", "wrong place", "breach", "Rule 17.1", "general penalty", "Rule 14.7a"],
        "examples": [
            "penalty for wrong penalty area relief",
            "playing from incorrect relief area",
            "general penalty for wrong place"
        ],
        "conditions": [
            {
            "situation": "Penalty for taking relief incorrectly",
            "explanation": "Under Rule 17.1, if you take relief from a penalty area incorrectly (wrong relief area, wrong procedure, etc.) and play from the wrong place, you get the general penalty under Rule 14.7a (loss of hole in match play, two strokes in stroke play).",
            "examples": ["incorrect relief procedure", "wrong relief area", "improper penalty area relief", "general penalty applies"]
        }
    ]
    },
    {
        "id": "17.2",
        "title": "Options After Playing Ball from Penalty Area",
        "text": "This Rule covers situations where a player has played a ball from a penalty area and the ball comes to rest in the same or another penalty area, or becomes lost, out of bounds, or unplayable outside the penalty area.",
        "keywords": ["playing from penalty area", "same penalty area", "another penalty area", "lost", "out of bounds", "unplayable", "relief options"],
        "examples": [
            "second shot from penalty area",
            "ball goes from one hazard to another",
            "options after hitting into same penalty area twice"
        ]
    },
    {
        "id": "17.2a",
        "title": "When Ball Played from Penalty Area Comes to Rest in Same or Another Penalty Area",
        "text": "If a ball played from a penalty area comes to rest in the same penalty area or another penalty area, the player may play the ball as it lies (see Rule 17.1b). Or, for one penalty stroke, the player may take relief under normal relief options or the extra relief option of playing from where last stroke made outside a penalty area.",
        "keywords": ["same penalty area", "another penalty area", "play as it lies", "one penalty stroke", "normal relief options", "extra relief option", "last stroke outside"],
        "examples": [
            "ball stays in same water hazard",
            "ball goes from one penalty area to another",
            "playing from where entered penalty area",
            "extra relief option available",
            "ball goes out of bounds after hitting from penalty area"
        ],
        "conditions": [
        {
            "situation": "Ball played from penalty area stays in same or goes to another penalty area",
            "explanation": "Under Rule 17.2a, if your ball played from a penalty area comes to rest in the same penalty area or another penalty area, you may play the ball as it lies without penalty, or take relief for one penalty stroke.",
            "examples": ["ball stays in same water hazard", "ball goes from one hazard to another", "can play as it lies", "one stroke penalty for relief"]
        },
        {
            "situation": "Normal relief options when ball stays in penalty area",
            "explanation": "Under Rule 17.2a(1), you may take stroke-and-distance relief, back-on-the-line relief, or lateral relief (for red penalty area). For back-on-line or lateral relief, use where the ball last crossed the edge of the penalty area where it now lies.",
            "examples": ["stroke and distance available", "back-on-line from new crossing point", "lateral relief for red areas", "reference point is new crossing point"]
        },
        {
            "situation": "Extra relief option - play from last stroke outside penalty area",
            "explanation": "Under Rule 17.2a(2), instead of normal relief options, you may choose to play from where you made the last stroke from outside a penalty area (often where you entered the penalty area originally).",
            "examples": ["go back to where you entered penalty area", "last stroke outside penalty area", "alternative to normal relief", "often more advantageous option"]
        },
        {
            "situation": "Dropping in penalty area then deciding not to play",
            "explanation": "Under Rule 17.2a(1), if you take stroke-and-distance relief by dropping in the penalty area but decide not to play that ball, you may take further relief outside the penalty area for one more penalty stroke (total two strokes).",
            "examples": ["drop in penalty area first", "decide not to play dropped ball", "take relief outside for additional stroke", "total two penalty strokes"]
        },
        {
            "situation": "Reference point for back-on-line and lateral relief",
            "explanation": "Under Rule 17.2a(1), when taking back-on-the-line or lateral relief, the estimated point used is where the original ball last crossed the edge of the penalty area where the ball now lies, not where it originally entered. If the ball does not exit the penalty area then re-cross the edge of the penalty area on the shot taken from the penalty area, the estimated point is where the original ball first crossed the edge of the penalty area.",
            "examples": ["use new crossing point", "where ball last crossed current penalty area", "not original entry point", "current penalty area crossing point"]
        }
    ]
    },
    {
        "id": "17.2b",
        "title": "When Ball Played from Penalty Area Is Lost, Out of Bounds or Unplayable Outside Penalty Area",
        "text": "After playing a ball from a penalty area, a player may sometimes be required or choose to take stroke-and-distance relief because the original ball is either: Out of bounds or lost outside the penalty area (see Rule 18.2), or Unplayable outside the penalty area (see Rule 19.2a). Special relief options are available with penalty strokes.",
        "keywords": ["lost outside", "out of bounds", "unplayable outside", "stroke-and-distance", "required", "choose", "special relief options", "penalty strokes"],
        "examples": [
            "ball out of bounds after penalty area shot",
            "ball lost after leaving penalty area",
            "unplayable ball after penalty area",
            "two stroke penalty relief"
        ],
        "conditions": [
        {
            "situation": "Ball lost, out of bounds, or unplayable after leaving penalty area",
            "explanation": "Under Rule 17.2b, after playing from a penalty area, if your ball becomes lost outside the penalty area, goes out of bounds, or becomes unplayable outside the penalty area, you have special relief options available.",
            "examples": ["ball out of bounds after water shot", "ball lost in woods after penalty area", "unplayable lie after leaving hazard", "special relief options available"]
        },
        {
            "situation": "Dropping in penalty area first, then taking relief outside",
            "explanation": "Under Rule 17.2b, if you take stroke-and-distance relief by dropping in the penalty area first, then decide not to play that ball, you may take further relief outside the penalty area for one more penalty stroke (total two strokes).",
            "examples": ["drop in penalty area first", "then take relief outside", "one more penalty stroke", "total two penalty strokes"]
        },
        {
            "situation": "Direct relief outside penalty area without dropping first",
            "explanation": "Under Rule 17.2b, you may directly take relief outside the penalty area without first dropping a ball in the penalty area, but you still get a total of two penalty strokes.",
            "examples": ["skip dropping in penalty area", "go directly outside", "still two penalty strokes total", "more efficient option"]
        },
        {
            "situation": "Relief options outside penalty area for lost/OB/unplayable",
            "explanation": "Under Rule 17.2b, you may take relief outside the penalty area under Rule 17.1d(2) (back-on-the-line), Rule 17.1d(3) (lateral relief for red penalty area), or Rule 17.2a(2) (from last stroke outside penalty area).",
            "examples": ["back-on-the-line relief outside", "lateral relief for red areas", "from last stroke outside penalty area", "same options as Rule 17.2a"]
        },
        {
            "situation": "Why two penalty strokes for this situation",
            "explanation": "Under Rule 17.2b, you get two penalty strokes total: one stroke for the stroke-and-distance relief (required for lost/OB/unplayable), and one stroke for taking relief outside the penalty area.",
            "examples": ["one stroke for stroke-and-distance", "one stroke for penalty area relief", "total two penalty strokes", "cumulative penalties"]
        },
        {
            "situation": "When stroke-and-distance relief is required vs chosen",
            "explanation": "Under Rule 17.2b, stroke-and-distance relief is required when the ball is lost or out of bounds (Rule 18.2), but is chosen when the ball is unplayable outside the penalty area (Rule 19.2a).",
            "examples": ["required for lost ball", "required for out of bounds", "chosen for unplayable ball", "different reasons same procedure"]
        }
    ]
    },
    {
        "id": "17.2.penalty",
        "title": "Penalty for Playing Ball from Wrong Place in Breach of Rule 17.2",
        "text": "Penalty for Playing Ball from a Wrong Place in Breach of Rule 17.2: General Penalty Under Rule 14.7a.",
        "keywords": ["penalty", "wrong place", "breach", "Rule 17.2", "general penalty", "Rule 14.7a"],
        "examples": [
            "penalty for wrong relief after penalty area",
            "playing from incorrect location",
            "general penalty for wrong place"
        ],
        "conditions": [
        {
            "situation": "Penalty for taking relief incorrectly after penalty area",
            "explanation": "Under Rule 17.2, if you take relief incorrectly after playing from a penalty area (wrong relief area, wrong procedure, etc.) and play from the wrong place, you get the general penalty under Rule 14.7a (loss of hole in match play, two strokes in stroke play).",
            "examples": ["incorrect relief procedure", "wrong relief area", "improper penalty area relief", "general penalty applies"]
        }
    ]
    },
    {
        "id": "17.3",
        "title": "No Relief Under Other Rules for Ball in Penalty Area",
        "text": "When a player's ball is in a penalty area, there is no relief for abnormal course conditions, embedded ball or unplayable ball. The player may only take relief under Rule 17.1 or 17.2, which both involve a penalty stroke.",
        "keywords": ["no relief", "other rules", "penalty area", "abnormal course conditions", "embedded ball", "unplayable ball", "Rule 17.1", "Rule 17.2", "penalty stroke"],
        "examples": [
            "ball in casual water within penalty area",
            "embedded ball in hazard",
            "unplayable lie in water hazard"
        ],
         "conditions": [
        {
            "situation": "Exception for dangerous animal",
            "explanation": "The only exception to Rule 17.3 is when a dangerous animal condition interferes with the play of the ball in a penalty area. In this case, the player may take either free relief in the penalty area or penalty relief outside the penalty area (see Rule 16.2b(2)).",
            "examples": ["dangerous animal situation in penalty area"]
        }
    ]
    },

    # --- Section 18: Stroke-and-Distance Relief; Ball Lost or Out of Bounds; Provisional Ball ---
    {
        "id": "18",
        "title": "Stroke-and-Distance Relief; Ball Lost or Out of Bounds; Provisional Ball",
        "text": "Rule 18 covers taking relief under penalty of stroke and distance. When a ball is lost outside a penalty area or comes to rest out of bounds, the required progression of playing from the teeing area to the hole is broken; the player must resume that progression by playing again from where the previous stroke was made. This Rule also covers how and when a provisional ball may be played to save time when the ball in play might have gone out of bounds or be lost outside a penalty area.",
        "keywords": ["stroke-and-distance", "lost", "out of bounds", "provisional ball", "penalty stroke", "progression", "teeing area", "hole", "save time"],
        "examples": [
            "ball lost in woods",
            "white stakes out of bounds",
            "provisional ball procedure",
            "stroke and distance penalty",
            "playing from previous spot"
    ]
    },
    {
        "id": "18.1",
        "title": "Relief Under Penalty of Stroke and Distance Allowed at Any Time",
        "text": "At any time, a player may take stroke-and-distance relief by adding one penalty stroke and playing the original ball or another ball from where the previous stroke was made (see Rule 14.6). The player always has this stroke-and-distance relief option: No matter where the player's ball is on the course, and even when a Rule requires the player to take relief in a certain way or to play a ball from a certain place.",
        "keywords": ["stroke-and-distance", "relief", "any time", "one penalty stroke", "original ball", "another ball", "previous stroke", "made"],
        "examples": [
            "taking stroke and distance relief",
            "playing three from the tee",
            "optional stroke and distance",
            "always available option",
            "going back to previous spot"
        ],
        "conditions": [
        {
            "situation": "Can I always take stroke-and-distance relief",
            "explanation": "Under Rule 18.1, you may take stroke-and-distance relief at any time by adding one penalty stroke and playing from where the previous stroke was made, no matter where your ball is on the course.",
            "examples": ["always available option", "anywhere on course", "voluntary stroke and distance", "one penalty stroke"]
        },
        {
            "situation": "Stroke-and-distance when other relief required",
            "explanation": "Under Rule 18.1, you always have the stroke-and-distance option even when a Rule requires you to take relief in a certain way or play from a certain place. It's always an alternative.",
            "examples": ["alternative to required relief", "even when rule requires specific relief", "always an option", "overrides other requirements"]
        },
        {
            "situation": "Original ball out of play after stroke-and-distance",
            "explanation": "Under Rule 18.1, once you put another ball in play under stroke-and-distance, the original ball is no longer in play and must not be played, even if found before the three-minute search time ends.",
            "examples": ["original ball out of play", "cannot play original if found", "new ball is in play", "three-minute rule doesn't matter"]
        },
        {
            "situation": "Exceptions when original ball remains in play",
            "explanation": "Under Rule 18.1, the original ball doesn't go out of play when you announce you're playing a provisional ball (Rule 18.3b) or playing a second ball in stroke play under Rules 14.7b or 20.1c(3).",
            "examples": ["provisional ball announcement", "second ball in stroke play", "original ball still in play", "specific exceptions apply"]
        }
    ]
    },
    {
        "id": "18.2",
        "title": "Ball Lost or Out of Bounds: Stroke-and-Distance Relief Must Be Taken",
        "text": "If a ball is lost or out of bounds, the player must take stroke-and-distance relief by adding one penalty stroke and playing the original ball or another ball from where the previous stroke was made (see Rule 14.6).",
        "keywords": ["lost", "out of bounds", "OB", "white stakes", "provisional", "penalty", "stroke-and-distance", "must", "one penalty stroke", "original ball", "another ball", "previous stroke", "three minutes", "search"],
        "examples": [
            "ball lost in woods",
            "white stakes out of bounds",
            "three minute search time",
            "white stake penalty options",
            "search time begins",
            "go back to previous spot"
        ],
         "conditions": [
        {
            "situation": "When is a ball considered lost",
            "explanation": "Under Rule 18.2a(1), a ball is lost if not found in three minutes after you or your caddie begins to search for it. If found but uncertain if it's yours, you get reasonable time to identify it, even after three minutes.",
            "examples": ["three minute search time", "reasonable time to identify", "search time starts when looking begins", "uncertainty about ball identity"]
        },
        {
            "situation": "When is a ball out of bounds",
            "explanation": "Under Rule 18.2a(2), a ball is out of bounds only when all of it is outside the boundary edge of the course. If any part touches or is above the boundary edge or inside the course, it's in bounds.",
            "examples": ["all of ball must be outside", "any part touching boundary is in bounds", "white stakes mark boundary", "can stand out of bounds to play ball in bounds"]
        },
        {
            "situation": "Required procedure for lost or out of bounds ball",
            "explanation": "Under Rule 18.2b, if your ball is lost or out of bounds, you must take stroke-and-distance relief by adding one penalty stroke and playing from where the previous stroke was made.",
            "examples": ["must take stroke and distance", "add one penalty stroke", "play from previous spot", "no other options available"]
        },
        {
            "situation": "Exception when you know what happened to ball",
            "explanation": "Under Rule 18.2b exception, instead of stroke-and-distance, you may substitute another ball under other Rules when it's known or virtually certain that the ball: Came to rest on the course and was moved by an outside influence (see Rule 9.6) or played as a wrong ball by another player (see Rule 6.3c(2)), came to rest on the course in or on a movable obstruction (see Rule 15.2b) or an abnormal course condition (see Rule 16.1e), is in a penalty area (see Rule 17.1c), or was deliberately deflected or stopped by any person (see Rule 11.2c).",
            "examples": ["known or virtually certain", "moved by outside influence", "in movable obstruction", "in abnormal course condition", "deliberately deflected"]
        },
        {
            "situation": "Ball identification after three minutes",
            "explanation": "Under Rule 18.2a(1), if a ball is found within three minutes but you're uncertain if it's yours, you get reasonable time to identify it, including time to get to the ball, even if this extends beyond three minutes.",
            "examples": ["found within three minutes", "reasonable time to identify", "can extend beyond three minutes", "time to reach the ball"]
        },
        {
            "situation": "Standing out of bounds to play ball",
            "explanation": "Under Rule 18.2a(2), you may stand out of bounds to play a ball that is in bounds on the course.",
            "examples": ["stand out of bounds", "play ball in bounds", "stance doesn't determine ball status", "ball position matters not player position"]
        }
    ]
    },
    {
        "id": "18.3",
        "title": "Provisional Ball",
        "text": "If a ball might be lost outside a penalty area or be out of bounds, to save time the player may play another ball provisionally under penalty of stroke and distance (see Rule 14.6). This covers when provisional balls are allowed, how to announce them, and when they become the ball in play or must be abandoned.",
        "keywords": ["provisional ball", "might be lost", "outside penalty area", "out of bounds", "save time", "announce", "ball in play", "abandoned"],
        "examples": [
            "when to play provisional ball",
            "announcing provisional shot",
            "abandoning provisional ball",
            "provisional becomes ball in play",
            "save time procedure"
        ],
        "conditions": [
        {
            "situation": "When can I play a provisional ball",
            "explanation": "Under Rule 18.3a, you may play a provisional ball when your ball might be lost outside a penalty area or be out of bounds, including when the ball might be lost in a penalty area but also might be lost elsewhere or out of bounds.",
            "examples": ["might be lost outside penalty area", "might be out of bounds", "might be lost in penalty area but also elsewhere", "uncertainty about ball location"]
        },
        {
            "situation": "Must announce provisional ball",
            "explanation": "Under Rule 18.3b, before making the stroke, you must announce to someone that you're playing a provisional ball. You must use the word 'provisional' or clearly indicate you're playing provisionally under Rule 18.3.",
            "examples": ["must announce before stroke", "use word provisional", "clearly indicate provisional", "not enough to say playing another ball"]
        },
        {
            "situation": "What if I don't announce provisional properly",
            "explanation": "Under Rule 18.3b, if you don't announce properly (even if you intended to play provisional) and play from where the previous stroke was made, that ball becomes your ball in play under stroke-and-distance.",
            "examples": ["improper announcement", "did not announce provisional", "ball becomes ball in play", "stroke and distance penalty applies", "no provisional status"]
        },
        {
            "situation": "Can I play provisional ball multiple times",
            "explanation": "Under Rule 18.3c(1), you may continue playing the provisional ball without losing its provisional status as long as it's played from the same distance or farther from the hole than where the original ball is estimated to be.",
            "examples": ["continue playing provisional", "same distance or farther from hole", "multiple strokes allowed", "maintains provisional status"]
        },
        {
            "situation": "When does provisional ball become ball in play",
            "explanation": "Under Rule 18.3c(2), the provisional becomes the ball in play when: (1) the original ball is lost anywhere except in penalty area or is out of bounds, or (2) you play the provisional from nearer the hole than where the original is estimated to be.",
            "examples": ["original lost outside penalty area", "original out of bounds", "played nearer than original estimated", "original no longer in play"]
        },
        {
            "situation": "When must I abandon provisional ball",
            "explanation": "Under Rule 18.3c(3), you must abandon the provisional when: (1) the original ball is found on course outside penalty area before three minutes end, or (2) the original is found or known to be in penalty area.",
            "examples": ["original found outside penalty area", "original found in penalty area", "known to be in penalty area", "must play original ball"]
        },
        {
            "situation": "Both balls found in same area - which is which",
            "explanation": "Under Rule 18.3c(2), if you play provisional into same general location and can't identify which is which: if only one found, it's treated as provisional; if both found, you (the player) choose which ball to treat as the provisional and play that.",
            "examples": ["both balls in same area", "cannot identify which is which", "cannot identify which ball is the original and which is the provisional", "one found treated as provisional", "choose which is provisional if both found"]
        },
        {
            "situation": "Can others search for my original ball",
            "explanation": "Under Rule 18.3c(3), you may ask others not to search for the original ball when you prefer to continue with the provisional, but they have no obligation to comply.",
            "examples": ["can ask others not to search", "no obligation to comply", "prefer to play provisional", "cannot stop others from searching"]
        },
        {
            "situation": "Provisional ball for provisional ball",
            "explanation": "Under Rule 18.3a, if a provisional ball itself might be lost outside a penalty area or out of bounds, you may play another provisional ball, which has the same relationship to the first provisional as the first has to the original.",
            "examples": ["provisional for provisional", "same relationship", "second provisional ball", "multiple provisional balls allowed"]
        },
    ]
    },
    {
        "id": "18.2 Penalty",
        "title": "Penalty for Playing Ball from Wrong Place in Breach of Rule 18.2",
        "text": "Penalty for Playing Ball from a Wrong Place in Breach of Rule 18.2: General Penalty Under Rule 14.7a.",
        "keywords": ["penalty", "wrong place", "breach", "Rule 18.2", "general penalty", "Rule 14.7a"],
        "examples": [
            "penalty for wrong stroke and distance procedure",
            "playing from incorrect location",
            "general penalty for wrong place"
        ],
        "conditions": [
        {
            "situation": "Penalty for incorrect stroke-and-distance procedure",
            "explanation": "Under Rule 18.2, if you take stroke-and-distance relief incorrectly (wrong location, wrong procedure, etc.) and play from the wrong place, you get the general penalty under Rule 14.7a (loss of hole in match play, two strokes in stroke play).",
            "examples": ["incorrect stroke and distance procedure", "wrong location for relief", "improper lost ball procedure", "general penalty applies"]
        }
    ]
    },

    # --- Section 19: Unplayable Ball ---
    {
        "id": "19",
        "title": "Unplayable Ball",
        "text": "Rule 19 covers the player's several relief options for an unplayable ball. This allows the player to choose which option to use – normally with one penalty stroke – to get out of a difficult situation anywhere on the course (except in a penalty area).",
        "keywords": ["unplayable ball", "relief options", "player choice", "one penalty stroke", "difficult situation", "anywhere on course", "except penalty area"],
        "examples": [
            "declaring ball unplayable",
            "unplayable ball relief options",
            "ball stuck in tree",
            "ball in thick bushes",
            "unplayable lie options"
        ]
    },
    {
        "id": "19.1",
        "title": "Player May Decide to Take Unplayable Ball Relief Anywhere Except Penalty Area",
        "text": "A player is the only person who may decide to treat their ball as unplayable by taking penalty relief under Rule 19.2 or 19.3. Unplayable ball relief is allowed anywhere on the course, except in a penalty area. If a ball is unplayable in a penalty area, the player's only relief option is to take penalty relief under Rule 17.",
        "keywords": ["player decision", "only person", "unplayable", "penalty relief", "anywhere on course", "except penalty area", "Rule 17"],
        "examples": [
            "player's decision for unplayable",
            "declaring ball unplayable",
            "no unplayable relief in penalty area",
            "only player can decide"
        ],
        "conditions": [
        {
            "situation": "Who can declare a ball unplayable",
            "explanation": "Under Rule 19.1, only the player may decide to treat their ball as unplayable. No one else (caddie, opponent, fellow competitor) can make this decision for the player.",
            "examples": ["only player decides", "caddie cannot declare unplayable", "opponent cannot force unplayable", "player's sole decision"]
        },
        {
            "situation": "Where can I declare my ball unplayable",
            "explanation": "Under Rule 19.1, unplayable ball relief is allowed anywhere on the course, except in a penalty area. This includes the teeing area, general area, bunkers, and putting green.",
            "examples": ["anywhere except penalty area", "including bunkers", "including putting green", "including teeing area"]
        },
        {
            "situation": "Ball unplayable in penalty area",
            "explanation": "Under Rule 19.1, if your ball is unplayable in a penalty area, you cannot use unplayable ball relief. Your only relief option is to take penalty relief under Rule 17 (penalty area relief).",
            "examples": ["no unplayable relief in penalty area", "must use Rule 17", "penalty area relief only", "cannot declare unplayable in water hazard"]
        },
        {
            "situation": "Is there a definition of unplayable",
            "explanation": "Under Rule 19.1, there is no specific definition of what makes a ball unplayable. It is entirely the player's decision based on their assessment of whether they can reasonably play the ball as it lies.",
            "examples": ["player's subjective decision", "no official definition", "player assessment", "reasonable playability judgment"]
        }
    ]
    },
    {
        "id": "19.2",
        "title": "Relief Options for Unplayable Ball in General Area or on Putting Green",
        "text": "A player may take unplayable ball relief using one of the three options in Rule 19.2a, b or c, in each case adding one penalty stroke. The player may take stroke-and-distance relief even if the original ball has not been found and identified. But to take back-on-the-line relief or lateral relief, the player must know the spot of the original ball.",
        "keywords": ["three options", "one penalty stroke", "stroke-and-distance", "back-on-the-line", "lateral relief", "original ball", "spot known"],
        "examples": [
            "unplayable ball relief options",
            "three relief choices",
            "one stroke penalty",
            "must know ball location"
        ],
        "conditions": [
        {
            "situation": "Three relief options for unplayable ball",
            "explanation": "Under Rule 19.2, when your ball is unplayable in the general area or on putting green, you have three relief options: stroke-and-distance, back-on-the-line, or lateral relief, each with one penalty stroke.",
            "examples": ["three options available", "stroke and distance", "back on line", "lateral relief", "one penalty stroke each"]
        },
        {
            "situation": "Stroke-and-distance without finding ball",
            "explanation": "Under Rule 19.2, you may take stroke-and-distance relief for an unplayable ball even if the original ball has not been found and identified, unlike the other relief options.",
            "examples": ["don't need to find ball", "stroke and distance without ball", "can declare unplayable without seeing ball", "unique stroke-and-distance benefit"]
        },
        {
            "situation": "Must know ball spot for back-on-line and lateral relief",
            "explanation": "Under Rule 19.2, to take back-on-the-line relief or lateral relief, you must know the spot of the original ball. These options are not available if the ball location is unknown.",
            "examples": ["must know exact spot", "back-on-line needs ball location", "lateral relief needs ball spot", "no relief if location unknown"]
        }
    ]
    },
        {
        "id": "19.2a",
        "title": "Stroke-and-Distance Relief",
        "text": "The player may play the original ball or another ball from where the previous stroke was made (see Rule 14.6).",
        "keywords": ["stroke-and-distance", "original ball", "another ball", "previous stroke", "Rule 14.6"],
        "examples": [
            "going back to previous spot",
            "stroke and distance unplayable",
            "replay from where last played"
        ],
        "conditions": [
        {
            "situation": "Stroke-and-distance for unplayable ball",
            "explanation": "Under Rule 19.2a, you may take stroke-and-distance relief by playing the original ball or another ball from where the previous stroke was made, following the procedures in Rule 14.6.",
            "examples": ["go back to previous spot", "add one penalty stroke", "replay from last location", "follow Rule 14.6 procedures"]
        }
    ]
    },
    {
        "id": "19.2b",
        "title": "Back-on-the-Line Relief",
        "text": "The player may drop the original ball or another ball (see Rule 14.3) behind the spot of the original ball, keeping the spot of the original ball between the hole and the spot where the ball is dropped (with no limit as to how far back the ball may be dropped). The spot on the line where the ball first touches the ground when dropped creates a relief area that is one club-length in any direction from that point.",
        "keywords": ["back-on-the-line", "drop", "behind", "original ball spot", "between hole", "no limit", "one club-length", "relief area"],
        "examples": [
            "back on line unplayable relief",
            "drop behind ball toward hole",
            "no limit how far back",
            "one club length relief area"
        ],
        "conditions": [
        {
            "situation": "Back-on-the-line relief procedure for unplayable ball",
            "explanation": "Under Rule 19.2b, you may drop behind the spot of the original ball, keeping that spot between the hole and where you drop, with no limit on how far back you may go.",
            "examples": ["drop behind ball", "keep ball between you and hole", "no distance limit", "straight line back"]
        },
        {
            "situation": "Relief area created by back-on-line drop",
            "explanation": "Under Rule 19.2b, the spot where the ball first touches the ground when dropped creates a relief area one club-length in any direction, but not nearer the hole than the original ball spot and in the same area where ball first touched.",
            "examples": ["one club-length from where ball hits", "not nearer than original spot", "same area as first touch", "relief area from drop point"]
        },
        {
            "situation": "Area limitations for back-on-line relief",
            "explanation": "Under Rule 19.2b, the relief area must not be nearer the hole than the original ball spot, may be in any area of the course, but must be in the same area that the ball first touched when dropped.",
            "examples": ["not nearer to hole", "any area of course allowed", "same area as first touch", "area consistency required"]
        }
    ]
    },
    {
        "id": "19.2c",
        "title": "Lateral Relief",
        "text": "The player may drop the original ball or another ball in this lateral relief area (see Rule 14.3), which is two club-lengths from reference point, or the spot of the original ball.",
        "keywords": ["lateral relief", "drop", "reference point", "original ball spot", "above ground", "tree", "directly below", "two club-lengths"],
        "examples": [
            "lateral relief unplayable",
            "two club lengths relief",
            "ball in tree reference point",
            "sideways relief from ball"
        ],
        "conditions": [
        {
            "situation": "Lateral relief reference point",
            "explanation": "Under Rule 19.2c, the reference point is the spot of the original ball. However, when the ball is above the ground (like in a tree), the reference point is the spot directly below the ball on the ground.",
            "examples": ["spot of original ball", "ball in tree use spot below", "ball above ground", "directly below on ground", "where to drop for lateral relief from an unplayable ball"]
        },
        {
            "situation": "Lateral relief area size",
            "explanation": "Under Rule 19.2c, you get a relief area of two club-lengths from the reference point, which is larger than most other relief situations that provide one club-length.",
            "examples": ["two club-lengths", "larger relief area", "measured from reference point", "generous lateral relief"]
        },
        {
            "situation": "Lateral relief area limitations",
            "explanation": "Under Rule 19.2c, the relief area must not be nearer the hole than the reference point, may be in any area of the course, but if multiple areas are within two club-lengths, the ball must come to rest in the same area it first touched when dropped.",
            "examples": ["not nearer to hole", "any area of course", "same area as first touch", "multiple areas consideration"]
        },
        {
            "situation": "Mobility device modification for lateral relief",
            "explanation": "Under Rule 19.2c and Rule 25.4m, for players who use a wheeled mobility device, the lateral relief area is expanded to four club-lengths instead of two.",
            "examples": ["wheeled mobility device", "four club-lengths", "expanded relief area", "accessibility accommodation"]
        },
        {
            "situation": "Penalty for incorrect unplayable ball relief",
            "explanation": "Under Rule 19.2, if you take unplayable ball relief incorrectly (wrong relief area, wrong procedure, etc.) and play from the wrong place, you get the general penalty under Rule 14.7a (loss of hole in match play, two strokes in stroke play).",
            "examples": ["incorrect relief procedure", "wrong relief area", "improper unplayable relief", "general penalty applies"]
        }
    ]
    },
    {
        "id": "19.3",
        "title": "Relief Options for Unplayable Ball in Bunker",
        "text": "When a player's ball is in a bunker, they have normal relief options for one penalty stroke (but must stay in bunker for back-on-line and lateral relief) or an extra relief option to get outside the bunker for two penalty strokes total.",
        "keywords": ["bunker", "normal relief options", "one penalty stroke", "stay in bunker", "extra relief option", "two penalty strokes", "outside bunker"],
        "examples": [
            "unplayable ball in bunker options",
            "staying in bunker vs leaving bunker",
            "two stroke penalty to leave bunker",
            "bunker unplayable relief"
        ],
        "conditions": [
        {
            "situation": "Normal relief options in bunker (one penalty stroke)",
            "explanation": "Under Rule 19.3a, when your ball is unplayable in a bunker, you may take any of the relief options from Rule 19.2 for one penalty stroke, except that for back-on-line and lateral relief, the ball must be dropped in and come to rest in the bunker.",
            "examples": ["all Rule 19.2 options available", "one penalty stroke", "back-on-line and lateral must stay in bunker", "stroke-and-distance can leave bunker"]
        },
        {
            "situation": "Stroke-and-distance from bunker",
            "explanation": "Under Rule 19.3a, stroke-and-distance relief allows you to play from where the previous stroke was made, which may take you outside the bunker if that's where the previous stroke was played.",
            "examples": ["can leave bunker with stroke-and-distance", "go back to previous spot", "may be outside bunker", "one penalty stroke"]
        },
        {
            "situation": "Back-on-line and lateral relief must stay in bunker",
            "explanation": "Under Rule 19.3a, if you choose back-on-the-line relief or lateral relief in a bunker, the ball must be dropped in and come to rest in the bunker. You cannot use these options to get outside the bunker.",
            "examples": ["must stay in bunker", "back-on-line in bunker only", "lateral relief in bunker only", "cannot leave bunker with these options"]
        },
        {
            "situation": "Extra relief option - outside bunker for two strokes",
            "explanation": "Under Rule 19.3b, as an extra option when your ball is unplayable in a bunker, you may take back-on-the-line relief outside the bunker for a total of two penalty strokes.",
            "examples": ["extra option available", "back-on-line outside bunker", "two penalty strokes total", "additional relief choice"]
        },
        {
            "situation": "Why two penalty strokes for bunker relief outside",
            "explanation": "Under Rule 19.3b, taking back-on-the-line relief outside the bunker costs two penalty strokes total because you're getting the significant advantage of escaping the bunker, which is considered a more severe penalty.",
            "examples": ["significant advantage", "escaping bunker penalty", "two strokes for advantage", "severe penalty for bunker escape"]
        },
        {
            "situation": "Mobility device modification in bunker",
            "explanation": "Under Rule 19.3 and Rule 25.4n, for players who use a wheeled mobility device, the lateral relief area in bunkers is expanded to four club-lengths instead of two.",
            "examples": ["wheeled mobility device", "four club-lengths in bunker", "expanded bunker relief", "accessibility in bunkers"]
        }
    ]
    },


    # --- Section 20: Resolving Rules Issues During Round; Rulings by Referee and Committee ---
    {
        "id": "20",
        "title": "Resolving Rules Issues During Round; Rulings by Referee and Committee",
        "text": "Rule 20 covers what players should do when they have questions about the Rules during a round, including the procedures (which differ in match play and stroke play) allowing a player to protect the right to get a ruling at a later time. The Rule also covers the role of referees who are authorized to decide questions of fact and apply the Rules. Rulings from a referee or the Committee are binding on all players.",
        "keywords": ["rules issues", "questions", "during round", "match play", "stroke play", "protect rights", "ruling", "referee", "committee", "binding"],
        "examples": [
            "disagreement about rules during play",
            "requesting official ruling",
            "rules question during round",
            "referee decision authority",
            "committee ruling procedures"
        ]
    },
    {
        "id": "20.1",
        "title": "Resolving Rules Issues During Round",
        "text": "Under Rule 20.1a, players must not unreasonably delay play when seeking help with the Rules during a round. If a referee or the Committee is not available in a reasonable time to help with a Rules issue, the player must decide what to do and play on. The player may protect their rights by asking for a ruling in match play or by playing two balls in stroke play.",
        "keywords": ["avoid delay", "seeking help", "reasonable time", "decide", "play on", "protect rights", "match play", "stroke play", "two balls"],
        "examples": [
            "avoiding delay while seeking ruling",
            "protecting rights when no referee available",
            "playing on when uncertain about rules",
            "requesting ruling procedures"
        ],
        "conditions": [
        {
            "situation": "Must avoid unreasonable delay when seeking rules help",
            "explanation": "Under Rule 20.1a, players must not unreasonably delay play when seeking help with Rules during a round. If a referee or Committee is not available in reasonable time, you must decide what to do and play on.",
            "examples": ["cannot delay play indefinitely", "reasonable time limit", "must keep playing", "decide and move on"]
        },
        {
            "situation": "How to protect rights when no official available",
            "explanation": "Under Rule 20.1a, you may protect your rights by asking for a ruling in match play (Rule 20.1b(2)) or by playing two balls in stroke play (Rule 20.1c(3)) when no referee or Committee is available.",
            "examples": ["request ruling in match play", "play two balls in stroke play", "protect rights for later", "different procedures by format"]
        }
    ]
    },
    {
        "id": "20.1b",
        "title": "Rules Issues in Match Play",
        "text": "During a round, the players in a match may agree how to decide a Rules issue. The agreed outcome is conclusive even if it turns out to have been wrong under the Rules, so long as the players did not agree to ignore any Rule or penalty they knew applied. Players may request rulings before the result of match is final, with specific time limits.",
        "keywords": ["match play", "agree", "decide", "conclusive", "wrong", "ignore rule", "penalty", "request ruling", "time limits", "final"],
        "examples": [
            "agreeing on rules in match play",
            "requesting ruling in match",
            "time limits for ruling requests",
            "match play rules disputes"
        ],
        "conditions": [
        {
            "situation": "Players can agree on rules issues in match play",
            "explanation": "Under Rule 20.1b(1), players in a match may agree how to decide a Rules issue. The agreed outcome is conclusive even if wrong, as long as they didn't agree to ignore a Rule or penalty they knew applied.",
            "examples": ["players can agree on procedure", "agreement is binding", "cannot ignore known penalties", "conclusive even if wrong"]
        },
        {
            "situation": "Referee overrides player agreement",
            "explanation": "Under Rule 20.1b(1), if a referee is assigned to the match, the referee must rule on any issue that comes to their attention in time, and players must follow that ruling instead of their agreement.",
            "examples": ["referee decision overrides agreement", "must follow referee ruling", "referee attention triggers ruling", "no player agreement when referee present"]
        },
        {
            "situation": "Time limits for ruling requests before match is final",
            "explanation": "Under Rule 20.1b(2), ruling requests must be made in time based on when the requestor became aware of facts: before either player starts next hole if aware before either player starts the final hole, or before match result is final if aware during/after final hole is played.",
            "examples": ["before starting next hole", "before match result final", "timing depends on awareness", "strict time limits apply", "cannot wait to request ruling if you become aware of a rule breach"]
        },
        {
            "situation": "Ruling requests about earlier holes",
            "explanation": "Under Rule 20.1b(2), rulings on earlier holes are only given if all three of these conditions apply: opponent breached stroke counting or penalty notification rules, request is based on facts not known earlier, and request is made in time according to Rule 20.1b.",
            "examples": ["wrong stroke count by opponent", "failure to notify penalty", "new facts discovered", "all three conditions required"]
        },
        {
            "situation": "Ruling requests after match is final",
            "explanation": "Under Rule 20.1b(3), after match is final, rulings are only given if based on facts not known before match was final, and opponent breached stroke counting or penalty notification knowing of the breach.",
            "examples": ["facts not known before final", "opponent knew of breach", "no time limit after final", "very limited circumstances"]
        },
        {
            "situation": "No two ball procedure in match play",
            "explanation": "Under Rule 20.1b(4), a player uncertain about procedure in match play cannot play two balls. That procedure only applies in stroke play.",
            "examples": ["no two balls allowed", "match play restriction", "stroke play procedure only", "must choose one procedure"]
        }
    ]
    },
    {
        "id": "20.1c",
        "title": "Rules Issues in Stroke Play",
        "text": "If a referee or the Committee is not available in a reasonable time to help with a Rules issue: The players are encouraged to help each other in applying the Rules, but they have no right to decide a Rules issue by agreement and any such agreement they may reach is not binding. Players should protect other players in the competition and may play two balls when uncertain.",
        "keywords": ["stroke play", "help each other", "no agreement", "not binding", "protect other players", "play two balls", "uncertain"],
        "examples": [
            "stroke play rules disputes",
            "playing two balls when uncertain",
            "protecting other competitors",
            "no binding agreements in stroke play"
        ],
        "conditions": [
        {
            "situation": "No binding agreements in stroke play",
            "explanation": "Under Rule 20.1c(1), players in stroke play have no right to decide Rules issues by agreement, and any agreement is not binding on any player, referee, or Committee. Players should raise issues with Committee before returning scorecard.",
            "examples": ["agreements not binding", "no right to decide by agreement", "raise with committee", "before returning scorecard"]
        },
        {
            "situation": "Duty to protect other players in competition",
            "explanation": "Under Rule 20.1c(2), if you know another player has breached or might have breached Rules and they don't recognize it, you should tell the player, marker, referee, or Committee promptly, no later than before they return their scorecard.",
            "examples": ["tell other player of breach", "notify marker or committee", "promptly after aware", "before scorecard returned", "protect the field"]
        },
        {
            "situation": "Playing two balls when uncertain",
            "explanation": "Under Rule 20.1c(3), when uncertain about procedure while playing a hole, you may complete the hole with two balls without penalty. The player must decide to play two balls before making stroke, choose and announce which ball will count if the Rules allow the procedure used for that ball, and report to Committee before returning scorecard.",
            "examples": ["two balls without penalty", "decide before stroke", "choose which counts", "report to committee"]
        },
        {
            "situation": "Requirements for two ball procedure",
            "explanation": "Under Rule 20.1c(3), you must decide to play two balls after uncertain situation arises and before making stroke, announce which ball will count, and report facts to Committee even if same score with both balls.",
            "examples": ["decide after uncertainty arises", "before making stroke", "announce choice", "report even if same score"]
        },
          {
            "situation": "Consequences for failing to follow two ball procedure",
            "explanation": "Under Rule 20.1c(3), if the player does not choose which ball will count if the Rules allow the procedure used for that ball, the ball played first is treated as the ball chosen by default. If the player made a stroke before deciding the play two balls, Rule 20.1c does not apply at all and the score that counts is the score with the ball played before the player decided to play the second ball, but the player gets no penalty for playing the second ball.",
            "examples": ["decide after uncertainty arises", "before making stroke", "announce choice", "report even if same score"]
        },
        {
            "situation": "Committee decision on two ball score",
            "explanation": "Under Rule 20.1c(4), Committee decides score based on whether Rules allow the procedure used: chosen ball counts if procedure allowed, other ball counts if chosen ball procedure not allowed, unless there is a serious breach, in which case the ball without the serious breach will count. If both balls were played with a serious breach, player is disqualified.",
            "examples": ["committee decides score", "chosen ball if procedure allowed", "other ball if chosen procedure wrong", "serious breach considerations"]
        },
        {
            "situation": "Consequences of failing to protect other players",
            "explanation": "Under Rule 20.1c(2), if you fail to notify others of a Rules breach, the Committee may disqualify you under Rule 1.2a if it decides this was serious misconduct contrary to the spirit of the game.",
            "examples": ["disqualification possible", "serious misconduct", "spirit of game", "duty to notify"]
        }
    ]
    },
       {
        "id": "20.2",
        "title": "Rulings on Issues Under the Rules",
        "text": "This Rule covers the authority and procedures for official rulings by referees and the Committee. It addresses referee authority, Committee final decisions, the use of video evidence with the 'naked eye' standard, correction of wrong rulings and administrative mistakes, disqualification procedures after competitions end, and handling ineligible players. All official rulings are binding and must be followed by players.",
        "keywords": ["referee", "committee", "questions of fact", "apply rules", "must be followed", "final", "rulings", "video evidence", "naked eye standard", "wrong rulings", "administrative mistakes", "disqualification", "competition closed", "ineligible player"],
        "examples": [
            "referee authority and decisions",
            "committee rulings when no referee",
            "final authority on rules",
            "video evidence naked eye standard",
            "correcting wrong rulings",
            "administrative mistakes vs wrong rulings",
            "disqualification after competition ends",
            "ineligible player discovered later"
        ],
        "conditions": [
        {
            "situation": "Referee authority and player obligations",
            "explanation": "Under Rule 20.2a, a referee decides questions of fact and applies Rules. Referee rulings must be followed by players. Players have no right to appeal to Committee, but referee may seek second opinion or refer to Committee.",
            "examples": ["referee decides facts", "must follow referee ruling", "no player appeal right", "referee may seek help"]
        },
        {
            "situation": "Committee rulings are final",
            "explanation": "Under Rule 20.2b, when there's no referee or referee refers to Committee, Committee gives ruling and it's final. If Committee cannot decide, may refer to USGA Rules Committee whose decision is final.",
            "examples": ["committee ruling is final", "no referee means committee decides", "USGA as final authority", "ultimate appeal level"]
        },
        {
            "situation": "Naked eye standard for video evidence",
            "explanation": "Under Rule 20.2c, when Committee uses video evidence, it's limited by 'naked eye' standard. If facts on video couldn't reasonably be seen with naked eye, video evidence is disregarded even if it shows Rules breach.",
            "examples": ["naked eye standard", "video evidence limitations", "disregard if not visible to naked eye", "protect reasonable observation"]
        },
        {
            "situation": "Exception to naked eye standard",
            "explanation": "Under Rule 20.2c, even where video evidence is disregarded under naked eye standard, Rules breach still found if player was otherwise aware of facts establishing breach (like feeling club touch sand in bunker).",
            "examples": ["player awareness matters", "feeling club touch sand", "other evidence of breach", "player knowledge counts"]
        },
        {
            "situation": "Wrong rulings and when they can be corrected",
            "explanation": "Under Rule 20.2d(1), wrong rulings occur when referee/Committee incorrectly applies Rules. If found wrong later, ruling can be corrected if possible under Rules. If it's too late, the wrong ruling stands.",
            "examples": ["wrong penalty applied", "misinterpreting rule", "correct if possible", "stands if too late"]
        },
        {
            "situation": "Administrative mistakes vs wrong rulings",
            "explanation": "Under Rule 20.2d(2), administrative mistakes are procedural errors in competition administration. There is no time limit for correcting these, even after competition closed, and results should be ammended accordingly. Different from wrong rulings.",
            "examples": ["miscalculating tie results", "wrong handicap calculation", "awarding prize to wrong player", "no time limit to correct"]
        },
        {
            "situation": "Disqualification after match is final",
            "explanation": "Under Rule 20.2e(1), in match play there is no time limit on disqualifying a player under Rule 1.2 (serious misconduct) or Rule 1.3b(1) (deliberately failing to apply penalty or agreeing to ignore Rules). This may be done even after the match result is final.",
            "examples": ["serious misconduct after match", "agreed to ignore known penalty", "deliberately failed to apply penalty", "no time limit for disqualification in match play"]
        },
        {
            "situation": "Disqualification after stroke play competition closed",
            "explanation": "Under Rule 20.2e(2), in stroke play, normally penalties can't be added after competition closed, but player must be disqualified under Rule 1.2 (serious misconduct), or if they returned lower score than taken, knew of disqualification breach before closing, or agreed to ignore known Rules.",
            "examples": ["lower score than taken", "knew of disqualification breach", "agreed to ignore rules", "serious misconduct after closed"]
        },
        {
            "situation": "Ineligible player corrections",
            "explanation": "Under Rule 20.2f, no time limit for correcting results when player found ineligible per Terms of Competition. Player treated as never entered, not disqualified, even after competition closed.",
            "examples": ["ineligible player discovered", "treated as never entered", "not disqualification", "no time limit"]
        }
    ]
    },
    {
        "id": "20.3",
        "title": "Situations Not Covered by the Rules",
        "text": "Any situation not covered by the Rules should be decided by the Committee, considering all the circumstances, and treating the situation in a way that is reasonable, fair and consistent with how similar situations are treated under the Rules.",
        "keywords": ["not covered", "committee decides", "circumstances", "reasonable", "fair", "consistent", "similar situations"],
        "examples": [
            "unusual situation not in rules",
            "committee decision for rare occurrence",
            "handling unprecedented circumstances",
            "fair and reasonable decisions"
        ],
        "conditions": [
        {
            "situation": "Committee authority for uncovered situations",
            "explanation": "Under Rule 20.3, any situation not covered by Rules should be decided by Committee considering all circumstances and treating situation reasonably, fairly, and consistently with how similar situations are treated under Rules.",
            "examples": ["committee decides uncovered situations", "consider all circumstances", "reasonable and fair treatment", "consistency with existing rules"]
        },
        {
            "situation": "Principles for deciding uncovered situations",
            "explanation": "Under Rule 20.3, Committee should decide based on: considering all circumstances, being reasonable and fair, and being consistent with how similar situations are treated under the Rules.",
            "examples": ["all circumstances matter", "reasonable approach required", "fair treatment", "consistent with existing precedent"]
        }
    ]
    },

    # --- Section 21: Other Forms of Play ---
    {
        "id": "21.1",
        "title": "Stableford",
        "text": "Stableford is a form of stroke play where points are awarded on each hole based on the player's score in relation to the hole's fixed score (usually par). The winner is the player who scores the highest number of points over the total round.",
        "keywords": ["stableford", "stroke play", "points", "awarded", "relation", "fixed score", "par", "highest", "total", "round"],
        "examples": [
            "stableford scoring system",
            "calculating stableford points",
            "winner determination in stableford"
        ]
    },
    {
        "id": "21.2a",
        "title": "Maximum Score",
        "text": "Maximum Score is a form of stroke play where a player's or side's score for a hole is capped at a maximum set by the Committee, such as double par, a fixed number or net double bogey. A player who does not complete a hole (often referred to as 'picking up') does not get a penalty.",
        "keywords": ["maximum score", "stroke play", "capped", "committee", "double par", "fixed number", "net double bogey", "complete", "picking up", "penalty"],
        "examples": [
            "double par maximum score format",
            "picking up ball when maximum reached",
            "net double bogey cap",
            "maximum score competition format"
        ],
        "conditions": [
        {
            "situation": "What is Maximum Score format",
            "explanation": "Under Rule 21.2a, Maximum Score is a stroke play format where each hole score is capped at a maximum set by the Committee, such as two times par, a fixed number, or net double bogey.",
            "examples": ["double par maximum", "fixed number like 8", "net double bogey cap", "committee determines maximum"]
        },
        {
            "situation": "Which rules apply in Maximum Score",
            "explanation": "Under Rule 21.2a, the Rules for stroke play in Rules 1-20 apply in Maximum Score, as modified by the specific Rules in Rule 21.2.",
            "examples": ["stroke play rules apply", "Rules 1-20 applicable", "modified by Rule 21.2", "same basic stroke play framework"]
        },
        {
            "situation": "Adaptations for different competition types",
            "explanation": "Under Rule 21.2a, Maximum Score is written for scratch individual play but can be adapted for handicap competitions, partner competitions (with Rules 22-23), and team competitions (with Rule 24).",
            "examples": ["scratch or handicap competitions", "individual or partner play", "team competition adaptation", "flexible format applications"]
        }
    ]
    },
    {
        "id": "21.2b",
        "title": "Scoring in Maximum Score",
        "text": "A player's score for a hole is based on the player's number of strokes (including strokes made and penalty strokes), except that the player will get only the maximum score even if the actual score exceeds the maximum. A player who does not hole out under the Rules for any reason gets the maximum score for the hole.",
        "keywords": ["scoring", "number of strokes", "penalty strokes", "maximum score", "actual score exceeds", "hole out", "any reason"],
        "examples": [
            "scoring when exceeding maximum",
            "not holing out gets maximum",
            "penalty strokes count toward maximum",
            "picking up ball scoring"
        ],
        "conditions": [
        {
            "situation": "How scoring works when under the maximum",
            "explanation": "Under Rule 21.2b(1), a player's score for a hole is based on strokes made plus penalty strokes, as long as the total doesn't exceed the maximum set by the Committee.",
            "examples": ["actual strokes plus penalties", "normal scoring if under maximum", "count all strokes and penalties", "cap at committee maximum"]
        },
        {
            "situation": "What happens when score exceeds maximum",
            "explanation": "Under Rule 21.2b(1), if a player's actual score (strokes plus penalties) exceeds the maximum, they only get the maximum score for that hole, not their actual higher score.",
            "examples": ["capped at maximum", "actual score doesn't matter if higher", "protection from very high scores", "maximum is the worst score possible"]
        },
        {
            "situation": "Scoring when not holing out",
            "explanation": "Under Rule 21.2b(1), a player who does not hole out under the Rules for any reason gets the maximum score for the hole. Players are encouraged to stop playing when reaching the maximum to help pace of play.",
            "examples": ["picking up gets maximum", "any reason for not holing out", "pace of play benefit", "stop when reaching maximum"]
        },
        {
            "situation": "When hole is completed",
            "explanation": "Under Rule 21.2b(1), the hole is completed when the player holes out, chooses not to hole out, or when their score has reached the maximum.",
            "examples": ["holes out completes hole", "chooses not to hole out", "reaching maximum completes hole", "three ways to complete"]
        },
        {
            "situation": "Scorecard entry when holing out under maximum",
            "explanation": "Under Rule 21.2b(2), if you hole out with a score lower than the maximum, the scorecard must show the actual score. If same as or higher than maximum, show either no score or any score at/above maximum.",
            "examples": ["actual score if under maximum", "no score or maximum if at/above", "scorecard flexibility for high scores", "committee adjusts scores"]
        },
        {
            "situation": "Scorecard entry when not holing out",
            "explanation": "Under Rule 21.2b(2), if you don't hole out under the Rules, the scorecard must show either no score or any score at or above the maximum. The Committee adjusts to the actual maximum.",
            "examples": ["no score when picking up", "any high score acceptable", "committee makes adjustment", "flexible scorecard entry"]
        },
        {
            "situation": "Committee responsibilities for scoring",
            "explanation": "Under Rule 21.2b(2), the Committee is responsible for adjusting scores to the maximum for holes showing no score or scores above maximum, and for applying handicap strokes in handicap competitions.",
            "examples": ["committee adjusts scores", "maximum score application", "handicap stroke application", "administrative responsibility"]
        }
    ]
    },
    {
        "id": "21.2c",
        "title": "Penalties in Maximum Score",
        "text": "All penalties that apply in stroke play apply in Maximum Score, except that a player who breaches any of five specific Rules is not disqualified but gets the maximum score for the hole where the breach happened. If the player breaches any other Rule with a penalty of disqualification, the player is disqualified.",
        "keywords": ["penalties", "stroke play apply", "five specific rules", "not disqualified", "maximum score", "breach happened", "other rule", "disqualified"],
        "examples": [
            "penalties converted to maximum score",
            "specific rules that don't disqualify",
            "other disqualification rules still apply",
            "hole-specific penalty application"
        ],
        "conditions": [
        {
            "situation": "General penalty application in Maximum Score",
            "explanation": "Under Rule 21.2c, all penalties that apply in stroke play apply in Maximum Score, except for five specific Rules where disqualification is converted to maximum score for the hole.",
            "examples": ["stroke play penalties apply", "five specific exceptions", "disqualification converted", "hole-specific application"]
        },
        {
            "situation": "Five rules that give maximum score instead of disqualification",
            "explanation": "Under Rule 21.2c, these five Rules give maximum score for the hole instead of disqualification: failure to hole out (Rule 3.3c), playing from outside teeing area (Rule 6.1b(2)), playing wrong ball (Rule 6.3c), serious breach wrong place (Rule 14.7b), wrong order in foursomes (Rule 22.3).",
            "examples": ["failure to hole out", "wrong teeing area", "wrong ball", "serious breach wrong place", "wrong order foursomes"]
        },
        {
            "situation": "Other disqualification rules still apply",
            "explanation": "Under Rule 21.2c, if you breach any other Rule with a penalty of disqualification (not one of the five specific Rules), you are still disqualified from the competition.",
            "examples": ["other disqualification rules unchanged", "still disqualified for other breaches", "five rules are exceptions only", "serious misconduct still disqualifies"]
        },
        {
            "situation": "Score cannot exceed maximum after penalties",
            "explanation": "Under Rule 21.2c, after applying any penalty strokes, the player's score for a hole cannot exceed the maximum score set by the Committee.",
            "examples": ["penalties applied first", "then capped at maximum", "maximum is absolute ceiling", "committee sets limit"]
        }
    ]
    },
    {
        "id": "21.2d",
        "title": "Exception to Rule 11.2 in Maximum Score",
        "text": "Rule 11.2 does not apply in this situation: If a player's ball in motion needs to be holed to score one lower than the maximum score on the hole and any person deliberately deflects or stops the ball at a time when there is no reasonable chance it can be holed, there is no penalty to that person and the player gets the maximum score on the hole.",
        "keywords": ["exception", "Rule 11.2", "ball in motion", "holed", "one lower", "maximum score", "deliberately deflects", "stops", "no reasonable chance", "no penalty"],
        "examples": [
            "deliberate deflection exception",
            "ball needed to avoid maximum",
            "no penalty for deflection",
            "gets maximum score anyway"
        ],
        "conditions": [
        {
            "situation": "Exception to deliberate deflection penalty",
            "explanation": "Under Rule 21.2d, if your ball in motion needs to be holed to score one lower than the maximum and someone deliberately deflects/stops it when there's no reasonable chance it can be holed, there's no penalty and you get the maximum score.",
            "examples": ["ball needed to avoid maximum", "deliberate deflection with no chance", "no penalty to deflector", "player gets maximum anyway"]
        },
        {
            "situation": "When this exception applies",
            "explanation": "Under Rule 21.2d, this exception only applies when the ball in motion must be holed to score one less than maximum, and there's no reasonable chance the ball can be holed when deflected/stopped.",
            "examples": ["must need hole to avoid maximum", "no reasonable chance to hole", "specific circumstances required", "limited exception scope"]
        }
    ]
    },
    {
        "id": "21.2e",
        "title": "When Round Ends in Maximum Score",
        "text": "A player's round ends when the player: Holes out on their final hole (including correction of a mistake, such as under Rule 6.1 or 14.7b), or Chooses not to hole out on the final hole or already will get the maximum score on the hole.",
        "keywords": ["round ends", "holes out", "final hole", "correction", "mistake", "chooses not", "hole out", "maximum score"],
        "examples": [
            "round completion in maximum score",
            "choosing not to finish final hole",
            "correction of mistakes on final hole",
            "reaching maximum on final hole"
        ],
        "conditions": [
        {
            "situation": "Round ends when holing out on final hole",
            "explanation": "Under Rule 21.2e, your round ends when you hole out on the final hole, including when you correct a mistake under Rules like 6.1 or 14.7b.",
            "examples": ["hole out on final hole", "correction of mistakes", "rule 6.1 or 14.7b corrections", "normal completion"]
        },
        {
            "situation": "Round ends when choosing not to hole out on final hole",
            "explanation": "Under Rule 21.2e, your round ends when you choose not to hole out on the final hole or when you already will get the maximum score on that hole.",
            "examples": ["choose not to hole out", "already at maximum score", "picking up on final hole", "early completion allowed"]
        },
    ]
    },
    {
        "id": "21.3",
        "title": "Par/Bogey",
        "text": "Par/Bogey is a form of stroke play using match play scoring where a player or side plays against a fixed target score for each hole. The player who wins more holes than they lose against the fixed score is the winner.",
        "keywords": ["par/bogey", "match play", "scoring", "fixed target", "each hole", "wins", "loses", "fixed score", "winner"],
        "examples": [
            "par/bogey competition format",
            "scoring in bogey competition",
            "winning in par competition"
        ],
         "conditions": [
        {
            "situation": "The game is won by the player or side with the highest total of holes won versus lost",
            "explanation": "Under Rule 21.3, a game of Par/Bogey is won by the player or side with the highest total of holes won versus lost (that is, adding up the holes won and deducting the holes lost.",
            "examples": ["scoring in Par/Bogey", "how to win in Par/Bogey", "Par/Bogey players compete against entire field", "Par/Bogey completion"]
        },
        {
            "situation": "How is a hole won or lost in Par/Bogey",
            "explanation": "Under Rule 21.3b(1), scoring is in match play format where a player or side wins, loses, or halves each hole: if the player's score is lower than the fixed score, the player wins the hole, if the player's score is the same as the fixed score, the hole is tied or halved, and if the player's score is higher or no score is returned, the player loses the hole.",
            "examples": ["scoring in Par/Bogey", "Par/Bogey holes won and lost"]
        },
         {
            "situation": "A player that does not hole out under the Rules for any reason loses the hole",
            "explanation": "Under Rule 21.3b(1), a player that does not hole out, for instance picks up or score his higher than the target, loses the hole.",
            "examples": ["picks up", "already at maximum score", "doesn't hole out"]
        },
         {
            "situation": "Filling out the scorecard in Par/Bogey",
            "explanation": "Under Rule 21.3b(2), to meet the requirements of Rule 3.3b, a player must enter a score on the scorecard when the hole is won or tied. If the hole is not completed or lost, the scorecard must show either no score or any score that results in the hole being lost.",
            "examples": ["picks up", "already at maximum score", "doesn't hole out"]
        },
        {
            "situation": "Some penalties that would otherwise result in a stroke play disqualification only result in a lost hole in Par/Bogey",
            "explanation": "Under Rule 21.3c, if a player breaches a Rule with a penalty of disqualification, the player is disqualified except breaches of these five rules, which lead to a loss of hole and not disqualification: Failure to hole out under Rule 3.3c, Failure to correct mistake of playing from outside the teeing area in starting a hole, Failure to corret mistake of playing the wrong ball, Failure to correct mistake of playing from a wrong place when there is a serious breach, and Failure to correct mistake of making a stroke in the wrong order.",
            "examples": ["picks up", "already at maximum score", "doesn't hole out"]
        },
        {
            "situation": "Any player deliberately deflects or stops a player's ball in motion ",
            "explanation": "Under Rule 21.3d, If a player’s ball in motion needs to be holed to tie the hole and any person deliberately deflects or stops the ball at a time when there is no reasonable chance it can be holed, there is no penalty to that person and the player loses the hole.",
            "examples": ["picks up", "already at maximum score", "doesn't hole out"]
        },
    ]
    },
    {
        "id": "21.4",
        "title": "Three-Ball Match Play",
        "text": "In Three-Ball Match Play, each of three players plays an individual match against the other two players at the same time, with each player playing one ball. Each player is playing two separate matches.",
        "keywords": ["three-ball", "match play", "individual match", "other two", "same time", "one ball", "two separate", "matches"],
        "examples": [
            "three-ball match rules",
            "scoring in three-ball format",
            "managing two matches simultaneously",
            "three players one ball each"
    ]
    },
    {
        "id": "21.4a",
        "title": "Overview of Three-Ball Match Play",
        "text": "Three-Ball Match Play is a form of match play where: Each of three players plays an individual match against the other two players at the same time, and Each player plays one ball that is used in both of their matches. The Rules for match play in Rules 1-20 apply to all three individual matches, except that these specific Rules apply in two situations where applying the Rules in one match might conflict with applying them in another match.",
        "keywords": ["overview", "three players", "individual match", "other two players", "same time", "one ball", "both matches", "rules 1-20 apply", "specific rules", "conflict"],
        "examples": [
            "three-ball match format overview",
            "one ball for both matches",
            "match play rules apply",
            "conflict resolution rules"
        ],
        "conditions": [
        {
            "situation": "Basic structure of three-ball match play",
            "explanation": "Under Rule 21.4a, Three-Ball Match Play involves three players where each player plays an individual match against the other two players simultaneously, using one ball for both of their matches.",
            "examples": ["three players total", "each plays two matches", "simultaneously played", "one ball per player"]
        },
        {
            "situation": "How matches work in three-ball format",
            "explanation": "Under Rule 21.4a, each player is essentially playing two separate matches at the same time - one against each of the other two players - but using the same ball for both matches.",
            "examples": ["Player A vs Player B", "Player A vs Player C", "same ball for both A's matches", "two separate match results"]
        },
        {
            "situation": "Which rules apply in three-ball match play",
            "explanation": "Under Rule 21.4a, the Rules for match play in Rules 1-20 apply to all three individual matches, except that specific Rules in 21.4 apply when applying Rules in one match might conflict with another match.",
            "examples": ["match play rules apply", "Rules 1-20 applicable", "specific rules for conflicts", "conflict resolution needed"]
        },
        {
            "situation": "Why special rules are needed",
            "explanation": "Under Rule 21.4a, special Rules are needed for situations where applying the Rules in one match might conflict with applying them in another match, since each player is simultaneously involved in two matches.",
            "examples": ["potential rule conflicts", "same action affects two matches", "need consistent application", "simultaneous match complications"]
        }
    ]
    },
      {
        "id": "21.4b",
        "title": "Playing Out of Turn",
        "text": "If a player plays out of turn in any match, the opponent who should have played first may cancel the stroke under Rule 6.4a(2): If the player played out of turn in both matches, each opponent may choose whether to cancel the stroke in their match with the player. If a player's stroke is cancelled only in one match, the player must continue play with the original ball in the other match and complete the hole by playing a separate ball in each match.",
        "keywords": ["playing out of turn", "opponent", "cancel stroke", "Rule 6.4a(2)", "both matches", "choose", "cancelled only one match", "original ball", "separate ball", "each match"],
        "examples": [
            "playing out of turn in three-ball",
            "cancelling stroke in one match only",
            "playing separate balls after cancellation",
            "opponent choice to cancel"
        ],
        "conditions": [
        {
            "situation": "Basic out of turn procedure in three-ball",
            "explanation": "Under Rule 21.4b, if a player plays out of turn in any match, the opponent who should have played first may cancel the stroke under Rule 6.4a(2), just like in regular match play.",
            "examples": ["same as regular match play", "opponent may cancel", "Rule 6.4a(2) applies", "optional cancellation"]
        },
        {
            "situation": "Out of turn affecting both matches",
            "explanation": "Under Rule 21.4b, if a player plays out of turn in both matches (against both opponents), each opponent may independently choose whether to cancel the stroke in their individual match with that player.",
            "examples": ["affects both matches", "each opponent chooses independently", "one may cancel, other may not", "separate decisions"]
        },
        {
            "situation": "When stroke is cancelled in only one match",
            "explanation": "Under Rule 21.4b, if a player's stroke is cancelled in only one match but not the other, the player must continue with the original ball in the match where the stroke was not cancelled and play a separate ball in the match where it was cancelled.",
            "examples": ["stroke cancelled in one match only", "continue with original ball in other match", "play separate ball where cancelled", "two different balls required"]
        },
        {
            "situation": "Completing hole with separate balls",
            "explanation": "Under Rule 21.4b, when a stroke is cancelled in only one match, the player must complete the hole by playing a separate ball in each match - the original ball continues in one match, and a new ball starts from the proper position in the other match.",
            "examples": ["separate ball for each match", "original ball continues", "new ball from proper position", "complete hole with two balls"]
        },
        {
            "situation": "Independent opponent decisions",
            "explanation": "Under Rule 21.4b, when a player plays out of turn affecting both matches, each opponent makes an independent decision about cancelling the stroke in their match - they don't have to make the same decision.",
            "examples": ["independent decisions", "Opponent A may cancel", "Opponent B may not cancel", "no requirement to agree"]
        }
    ]
    },  
    {
        "id": "21.4c",
        "title": "Ball or Ball-Marker Lifted or Moved by One Opponent",
        "text": "If an opponent gets one penalty stroke for lifting a player's ball or ball-marker or causing the ball or ball-marker to move under Rule 9.5b or 9.7b, that penalty applies only in the match with that player. The opponent gets no penalty in their match with the other player.",
        "keywords": ["opponent", "one penalty stroke", "lifting", "ball", "ball-marker", "causing", "move", "Rule 9.5b", "Rule 9.7b", "penalty applies", "only in match", "no penalty", "other player"],
        "examples": [
            "opponent moves ball penalty",
            "penalty only in one match",
            "no penalty in other match",
            "ball-marker lifting penalty"
        ],
        "conditions": [
        {
            "situation": "Penalty for opponent moving ball or ball-marker",
            "explanation": "Under Rule 21.4c, if an opponent gets a one penalty stroke for lifting a player's ball or ball-marker or causing it to move under Rules 9.5b or 9.7b, this penalty applies only in the match between that opponent and the affected player.",
            "examples": ["opponent lifts ball", "opponent causes ball to move", "one penalty stroke", "only in their specific match"]
        },
        {
            "situation": "No penalty in other match",
            "explanation": "Under Rule 21.4c, when an opponent incurs a penalty for moving another player's ball or ball-marker, that opponent gets no penalty in their match with the third player, even though the same action occurred.",
            "examples": ["no penalty in other match", "same action different consequences", "penalty isolated to one match", "third player unaffected"]
        },
        {
            "situation": "Match-specific penalty application",
            "explanation": "Under Rule 21.4c, penalties for moving another player's ball or ball-marker are applied only in the specific match between the player whose ball was moved and the opponent who moved it, not across all matches.",
            "examples": ["penalty specific to one match", "doesn't affect other match", "isolated consequence", "match-by-match application"]
        },
        {
            "situation": "Rules 9.5b and 9.7b application",
            "explanation": "Under Rule 21.4c, this rule specifically applies to penalties under Rules 9.5b (opponent lifting or moving player's ball) and 9.7b (opponent lifting or moving ball-marker), with the penalty applying only in the relevant match.",
            "examples": ["Rules 9.5b and 9.7b", "opponent lifting ball", "opponent moving ball-marker", "specific rule violations"]
        }
    ]
    },
    {
        "id": "21.5",
        "title": "Other Forms of Playing Golf",
        "text": "Other forms of play such as scramble, greensomes and best-ball are not specifically covered by the Rules of Golf. The Committee should decide how the Rules apply in these cases.",
        "keywords": ["other forms", "scramble", "greensomes", "best-ball", "committee", "decide", "rules", "apply", "cases"],
        "examples": [
            "rules for scramble format",
            "greensomes competition regulations",
            "best-ball tournament rules"
        ]
    },

    # --- Section 22-24: Team Competitions ---
    {
        "id": "22",
        "title": "Foursomes (Also Known as Alternate Shot)",
        "text": "Rule 22 covers Foursomes (played either in match play or stroke play), where two partners compete together as a side by alternating in making strokes at a single ball. The Rules for this form of play are essentially the same as for individual play, except for requiring the partners to alternate in teeing off to start a hole and to play out each hole with alternate shots.",
        "keywords": ["foursomes", "alternate shot", "partners", "side", "alternating", "single ball", "match play", "stroke play", "teeing off", "alternate shots"],
        "examples": [
            "alternate shot format rules",
            "taking turns in foursomes",
            "penalties in foursomes",
            "partner team competition"
    ]
    },
    {
        "id": "22.1",
        "title": "Overview of Foursomes",
        "text": "Foursomes (also known as Alternate Shot) is a form of play involving partners (in either match play or stroke play) where two partners compete as a side by playing one ball in alternating order on each hole. Rules 1-20 apply to this form of play (with the side playing one ball being treated in the same way as the individual player is treated), as modified by these specific Rules.",
        "keywords": ["overview", "alternate shot", "partners", "match play", "stroke play", "side", "one ball", "alternating order", "rules 1-20 apply", "specific rules"],
        "examples": [
            "foursomes format overview",
            "alternate shot explanation",
            "partner team play",
            "one ball per side"
        ],
        "conditions": [
        {
            "situation": "Basic structure of foursomes",
            "explanation": "Under Rule 22.1, Foursomes is a form of play where two partners compete as a side by playing one ball in alternating order on each hole, available in both match play and stroke play.",
            "examples": ["two partners as one side", "one ball per side", "alternating order", "match play or stroke play"]
        },
        {
            "situation": "Which rules apply in foursomes",
            "explanation": "Under Rule 22.1, Rules 1-20 apply to foursomes with the side playing one ball treated the same as an individual player, as modified by the specific Rules in Rule 22.",
            "examples": ["Rules 1-20 apply", "side treated as individual", "modified by Rule 22", "same basic framework"]
        },
        {
            "situation": "Threesomes variation",
            "explanation": "Under Rule 22.1, a variation called Threesomes is a form of match play where an individual player competes against a side of two partners who play alternating shots under these specific Rules.",
            "examples": ["one player vs two partners", "match play format", "alternating shots for partners", "individual vs side"]
        }
    ]
    },
    {
        "id": "22.2",
        "title": "Either Partner May Act for Side",
        "text": "As both partners compete as one side playing only one ball: Either partner may take any allowed action for the side before the stroke is made, such as to mark the spot of the ball and lift, replace, drop and place the ball, no matter which partner's turn it is to play next for the side. Any action taken or breach of the Rules by either partner or either caddie applies to the side.",
        "keywords": ["either partner", "act for side", "one side", "one ball", "allowed action", "before stroke", "mark", "lift", "replace", "drop", "place", "breach applies to side"],
        "examples": [
            "either partner can mark ball",
            "partner actions for the side",
            "ball handling by either partner",
            "team responsibility for actions"
        ],
        "conditions": [
        {
            "situation": "Either partner may take actions for the side",
            "explanation": "Under Rule 22.2, either partner may take any allowed action for the side before a stroke is made, such as marking, lifting, replacing, dropping, or placing the ball, regardless of whose turn it is to play next.",
            "examples": ["either partner can mark ball", "either can lift and replace", "either can drop ball", "regardless of turn to play"]
        },
        {
            "situation": "Partner and caddie assistance rules",
            "explanation": "Under Rule 22.2, a partner and their caddie may help the other partner in any way that the other partner's caddie is allowed to help (like giving advice), but must not give help that a caddie is not allowed to give.",
            "examples": ["partner can give advice", "same as caddie assistance rules", "cannot exceed caddie limitations", "help within allowed boundaries"]
        },
        {
            "situation": "Actions and breaches apply to the side",
            "explanation": "Under Rule 22.2, any action taken or breach of the Rules by either partner or either caddie applies to the side as a whole, not just to the individual who took the action.",
            "examples": ["breach by one affects side", "penalty applies to side", "team responsibility", "collective consequences"]
        },
        {
            "situation": "Scorecard certification in stroke play",
            "explanation": "Under Rule 22.2, in stroke play, only one of the partners needs to certify the side's hole scores on the scorecard, not both partners.",
            "examples": ["one partner certifies scorecard", "not both partners required", "side responsibility", "simplified certification"]
        }
    ]
    },
    {
        "id": "22.3",
        "title": "Side Must Alternate in Making Strokes",
        "text": "On each hole, the partners must make each stroke for the side in alternating order: Partners must alternate the order in which they play first from the teeing area of each hole. After the side's first stroke from the teeing area of a hole, the partners must alternate strokes for the rest of the hole. Any penalty strokes for the side do not affect the partners' alternating order of play.",
        "keywords": ["alternate", "making strokes", "each hole", "alternating order", "teeing area", "first stroke", "rest of hole", "penalty strokes", "do not affect", "order of play"],
        "examples": [
            "alternating strokes in foursomes",
            "taking turns on each shot",
            "penalty strokes don't change order",
            "alternating tee shots"
        ],
        "conditions": [
        {
            "situation": "Basic alternating stroke requirement",
            "explanation": "Under Rule 22.3, on each hole, partners must make each stroke for the side in alternating order throughout the entire hole.",
            "examples": ["alternate every stroke", "take turns hitting", "consistent alternating pattern", "throughout entire hole"]
        },
        {
            "situation": "Alternating tee shots between holes",
            "explanation": "Under Rule 22.3, partners must alternate the order in which they play first from the teeing area of each hole, so if Partner A tees off on hole 1, Partner B tees off on hole 2.",
            "examples": ["alternate who tees off", "different partner each hole", "switch tee responsibilities", "hole-by-hole alternation"]
        },
        {
            "situation": "Alternating after first stroke on hole",
            "explanation": "Under Rule 22.3, after the side's first stroke from the teeing area, the partners must alternate strokes for the rest of that hole.",
            "examples": ["after tee shot alternate", "second shot by other partner", "continue alternating", "rest of hole pattern"]
        },
        {
            "situation": "Penalty strokes don't affect alternating order",
            "explanation": "Under Rule 22.3, penalty strokes for the side do not affect the partners' alternating order of play - the same partner who would have played next still plays next.",
            "examples": ["penalty doesn't change turn", "same partner plays after penalty", "alternating order maintained", "penalties don't disrupt pattern"]
        },
        {
            "situation": "Cancelled or replayed strokes",
            "explanation": "Under Rule 22.3, if a stroke is cancelled, replayed, or doesn't count under any Rule (except wrong order), the same partner who made that stroke must make the next stroke for the side.",
            "examples": ["same partner replays cancelled stroke", "stroke doesn't count", "same partner continues", "exception for wrong order"]
        },
        {
            "situation": "Provisional ball procedure",
            "explanation": "Under Rule 22.3, if the side decides to play a provisional ball, it must be played by the partner whose turn it is to play the side's next stroke.",
            "examples": ["provisional by partner whose turn", "normal alternating order", "turn determines provisional player", "follow alternating pattern"]
        },
        {
            "situation": "Penalty for wrong order in stroke play",
            "explanation": "Under Rule 22.3, in stroke play, if strokes are made in wrong order, the side gets general penalty and must correct: right partner makes stroke from where first wrong stroke was made, wrong strokes don't count, disqualified if not corrected.",
            "examples": ["general penalty for wrong order", "must correct mistake", "right partner from correct spot", "disqualification if not corrected"]
        }
    ]
    },
    {
        "id": "22.4",
        "title": "Starting the Round",
        "text": "The side may choose which partner will play from the first teeing area in starting the round, unless the Terms of the Competition say which partner must play first. Rule 5.3a applies differently to each partner based on who will play first for the side.",
        "keywords": ["starting round", "choose partner", "first teeing area", "terms of competition", "Rule 5.3a", "differently", "play first"],
        "examples": [
            "choosing who tees off first",
            "starting time requirements",
            "partner presence requirements",
            "beginning foursomes round"
        ],
        "conditions": [
        {
            "situation": "Choosing which partner plays first",
            "explanation": "Under Rule 22.4a, the side may choose which partner will play from the first teeing area to start the round, unless the Terms of the Competition specify which partner must play first.",
            "examples": ["side chooses first player", "either partner can start", "unless competition specifies", "team decision"]
        },
        {
            "situation": "When round starts for the side",
            "explanation": "Under Rule 22.4a, the side's round starts when the chosen partner makes a stroke to start the side's first hole.",
            "examples": ["round starts with first stroke", "chosen partner makes first stroke", "side's round beginning", "first hole commencement"]
        },
        {
            "situation": "Starting time requirements for partner playing first",
            "explanation": "Under Rule 22.4b, the partner who will play first must be ready to play at the starting time and starting point, and must start at (not before) that time.",
            "examples": ["first partner ready at start time", "at starting point", "start at designated time", "not before start time"]
        },
        {
            "situation": "Starting time requirements for partner playing second",
            "explanation": "Under Rule 22.4b, the partner who will play second must be present at the starting time either at the starting point or on the hole near where the ball from the teeing area is expected to come to rest.",
            "examples": ["second partner at start time", "at starting point or near expected ball location", "presence requirement", "flexibility in location"]
        },
        {
            "situation": "Consequences of partner absence",
            "explanation": "Under Rule 22.4b, if either partner is not present as required, the side is in breach of Rule 5.3a.",
            "examples": ["breach if either partner absent", "both partners must be present", "Rule 5.3a violation", "side responsibility"]
        }
    ]
    },
    {
        "id": "22.5",
        "title": "Partners May Share Clubs",
        "text": "Rule 4.1b(2) is modified to allow partners to share clubs, so long as the total number of clubs they have together is not more than 14.",
        "keywords": ["partners", "share clubs", "Rule 4.1b(2)", "modified", "total number", "together", "not more than 14"],
        "examples": [
            "sharing clubs between partners",
            "14 club limit for the side",
            "combined club count",
            "partner equipment sharing"
        ],
        "conditions": [
        {
            "situation": "Partners may share clubs",
            "explanation": "Under Rule 22.5, partners are allowed to share clubs with each other, which is a modification of Rule 4.1b(2) that normally prohibits sharing clubs.",
            "examples": ["partners can share clubs", "modification of normal rule", "sharing allowed in foursomes", "equipment sharing permitted"]
        },
        {
            "situation": "14 club limit applies to the side",
            "explanation": "Under Rule 22.5, while partners may share clubs, the total number of clubs they have together as a side must not be more than 14.",
            "examples": ["14 club maximum for side", "combined total", "not 14 each", "side limit not individual limit"]
        },
        {
            "situation": "Practical implications of club sharing",
            "explanation": "Under Rule 22.5, partners could carry different clubs and share them as needed, as long as their combined total doesn't exceed 14 clubs for the side.",
            "examples": ["different clubs for each partner", "share as needed during round", "strategic club distribution", "combined equipment strategy"]
        }
    ]
    },
    {
        "id": "22.6",
        "title": "Restriction on Player Standing Behind Partner When Stroke Made",
        "text": "In addition to the limitations in Rule 10.2b(4), a player must not stand on or close to an extension of the line of play behind the ball while their partner is making a stroke to gain information for the side's next stroke. Penalty for Breach of Rule 22.6: General Penalty.",
        "keywords": ["restriction", "standing behind", "partner", "stroke made", "Rule 10.2b(4)", "extension", "line of play", "behind ball", "gain information", "next stroke", "general penalty"],
        "examples": [
            "cannot stand behind partner during stroke",
            "line of play positioning restriction",
            "gaining information penalty",
            "partner positioning rules"
        ],
        "conditions": [
        {
            "situation": "Restriction on standing behind partner",
            "explanation": "Under Rule 22.6, in addition to normal Rule 10.2b(4) limitations, a player must not stand on or close to an extension of the line of play behind the ball while their partner is making a stroke.",
            "examples": ["cannot stand behind partner", "line of play extension", "behind the ball", "additional restriction"]
        },
        {
            "situation": "Purpose of restriction - gaining information",
            "explanation": "Under Rule 22.6, the restriction prevents a player from standing behind their partner's stroke to gain information for the side's next stroke.",
            "examples": ["prevent gaining information", "information for next stroke", "unfair advantage prevention", "strategic positioning restriction"]
        },
        {
            "situation": "Penalty for violation",
            "explanation": "Under Rule 22.6, the penalty for breaching this restriction is the general penalty (loss of hole in match play, two strokes in stroke play).",
            "examples": ["general penalty applies", "loss of hole in match play", "two strokes in stroke play", "significant penalty"]
        },
        {
            "situation": "Relationship to Rule 10.2b(4)",
            "explanation": "Under Rule 22.6, this restriction is in addition to the limitations already in Rule 10.2b(4), creating an extra layer of positioning restrictions for foursomes.",
            "examples": ["additional to Rule 10.2b(4)", "extra restrictions", "foursomes-specific rule", "enhanced positioning limitations"]
        }
    ]   
    },
    {
        "id": "23",
        "title": "Four-Ball",
        "text": "Rule 23 covers Four-Ball (played either in match play or stroke play), where partners compete as a side with each playing a separate ball. The side's score for a hole is the lower score of the partners on that hole.",
        "keywords": ["four-ball", "partners", "side", "separate ball", "match play", "stroke play", "lower score", "hole"],
        "examples": [
            "four-ball format rules",
            "best ball of partners",
            "lower score counts",
            "partner team play"
    ]
    },
    {
        "id": "23.1",
        "title": "Overview of Four-Ball",
        "text": "Four-Ball is a form of play (in either match play or stroke play) involving partners where: Two partners compete together as a side, with each player playing their own ball, and a side's score for a hole is the lower score of the two partners on that hole. Rules 1-20 apply to this form of play, as modified by these specific Rules.",
        "keywords": ["overview", "partners", "side", "own ball", "lower score", "two partners", "rules 1-20 apply", "specific rules"],
        "examples": [
            "four-ball format overview",
            "each player plays own ball",
            "best ball scoring",
            "partner competition"
        ],
        "conditions": [
        {
            "situation": "Basic structure of four-ball",
            "explanation": "Under Rule 23.1, Four-Ball is a form of play where two partners compete as a side, with each player playing their own ball, and the side's score for each hole is the lower score of the two partners.",
            "examples": ["two partners as side", "each plays own ball", "lower score counts", "best ball format"]
        },
        {
            "situation": "Which rules apply in four-ball",
            "explanation": "Under Rule 23.1, Rules 1-20 apply to four-ball play, as modified by the specific Rules in Rule 23.",
            "examples": ["Rules 1-20 apply", "modified by Rule 23", "individual play rules", "partnership modifications"]
        },
        {
            "situation": "Best-Ball variation",
            "explanation": "Under Rule 23.1, a variation called Best-Ball is match play where an individual competes against a side of two or three partners, with each partner playing their own ball under these Rules.",
            "examples": ["individual vs partners", "two or three partners", "match play format", "each plays own ball"]
        }
    ]
    },
    {
        "id": "23.2",
        "title": "Scoring in Four-Ball",
        "text": "The side's score for a hole depends on how many partners complete the hole: if both partners hole out, the lower score counts; if only one partner holes out, that score counts; if neither partner holes out, the side has no score (loses hole in match play, disqualified in stroke play unless corrected).",
        "keywords": ["scoring", "both partners", "hole out", "lower score", "one partner", "neither partner", "no score", "loses hole", "disqualified"],
        "examples": [
            "four-ball scoring rules",
            "when both partners finish",
            "when only one partner finishes",
            "neither partner finishes penalty"
        ],
        "conditions": [
        {
            "situation": "Scoring when both partners hole out",
            "explanation": "Under Rule 23.2a, when both partners hole out or otherwise complete the hole under the Rules, the lower score is the side's score for the hole.",
            "examples": ["both complete hole", "lower score counts", "best ball scoring", "side gets better score"]
        },
        {
            "situation": "Scoring when only one partner holes out",
            "explanation": "Under Rule 23.2a, when only one partner holes out or otherwise completes the hole under the Rules, that partner's score is the side's score. The other partner does not need to hole out.",
            "examples": ["one partner completes", "that score counts", "other partner can pick up", "no need to finish"]
        },
        {
            "situation": "Consequences when neither partner holes out",
            "explanation": "Under Rule 23.2a, when neither partner holes out or completes the hole under the Rules, the side has no score: loses the hole in match play (unless opponent conceded/lost), or is disqualified in stroke play unless corrected under Rule 3.3c.",
            "examples": ["neither completes hole", "loses hole in match play", "disqualified in stroke play", "must correct under Rule 3.3c"]
        },
        {
            "situation": "Scorecard requirements in stroke play",
            "explanation": "Under Rule 23.2b(1), the side's gross scores must be entered on a single scorecard, with at least one partner's score per hole, each score clearly identified by individual partner, and only one partner needs to certify.",
            "examples": ["single scorecard", "at least one score per hole", "clearly identify partner", "one partner certifies"]
        },
        {
            "situation": "Committee responsibilities for scoring",
            "explanation": "Under Rule 23.2b(2), the Committee decides which score counts: if only one entered, that counts; if both entered and different, lowest counts; if both same, Committee may count either but will use the other if chosen score is wrong.",
            "examples": ["committee decides counting score", "one score entered", "different scores - lowest counts", "same scores - either may count"]
        },
        {
            "situation": "Exception to Rule 11.2 in four-ball",
            "explanation": "Under Rule 23.2c, Rule 11.2 doesn't apply when partner has completed hole and player's ball needs to be holed to lower side's score by one stroke - if deliberately deflected with no reasonable chance to hole, no penalty and ball doesn't count.",
            "examples": ["partner already completed", "ball needed to improve by one", "deliberate deflection", "no penalty if no chance"]
        }
    ]
    },
    {
        "id": "23.3",
        "title": "When Round Starts and Ends; When Hole Is Completed",
        "text": "A side's round starts when one partner makes a stroke to start their first hole. The round ends when the match is decided (match play) or when the side completes the final hole (stroke play). A hole is completed when the required partners have holed out or the result is decided.",
        "keywords": ["round starts", "one partner", "stroke", "first hole", "round ends", "match decided", "final hole", "hole completed", "result decided"],
        "examples": [
            "when four-ball round starts",
            "completing final hole",
            "hole completion rules",
            "match ending procedures"
        ],
        "conditions": [
        {
            "situation": "When side's round starts",
            "explanation": "Under Rule 23.3a, a side's round starts when one of the partners makes a stroke to start their first hole.",
            "examples": ["one partner starts", "first stroke begins round", "either partner can start", "side's round commencement"]
        },
        {
            "situation": "When round ends in match play",
            "explanation": "Under Rule 23.3b, in match play, the side's round ends when either side has won the match or the match is tied after the final hole when Terms of Competition allow ties.",
            "examples": ["either side wins", "match decided", "tied after final hole", "terms allow ties"]
        },
        {
            "situation": "When round ends in stroke play",
            "explanation": "Under Rule 23.3b, in stroke play, the round ends when the side completes the final hole, either by both partners holing out (including corrections) or by one partner holing out and the other choosing not to.",
            "examples": ["both hole out final hole", "one holes out other chooses not to", "including corrections", "side completes final hole"]
        },
        {
            "situation": "Hole completion in match play",
            "explanation": "Under Rule 23.3c(1), in match play, a side completes a hole when: both partners hole out/conceded, one holes out/conceded and other chooses not to or has score that can't count, or result is decided.",
            "examples": ["both hole out or conceded", "one completes other can't count", "result already decided", "multiple completion scenarios"]
        },
        {
            "situation": "Hole completion in stroke play",
            "explanation": "Under Rule 23.3c(2), in stroke play, a side completes a hole when one partner has holed out and the other has holed out, chooses not to do so, or is disqualified for the hole.",
            "examples": ["one partner holes out", "other holes out chooses not to or disqualified", "completion requirements", "stroke play specific"]
        }
    ]
    },
    {
        "id": "23.4",
        "title": "One or Both Partners May Represent the Side",
        "text": "The side may be represented by one partner during all or any part of a round. It is not necessary for both partners to be present or, if present, for both to play on each hole. If a partner arrives late, they may start play only between holes, not during a hole.",
        "keywords": ["one partner", "represent side", "all or any part", "not necessary", "both present", "both play", "arrives late", "between holes", "not during hole"],
        "examples": [
            "one partner can play alone",
            "late arriving partner rules",
            "when partner can join",
            "partnership flexibility"
        ],
        "conditions": [
        {
            "situation": "Side representation flexibility",
            "explanation": "Under Rule 23.4, the side may be represented by one partner during all or any part of a round. It's not necessary for both partners to be present or, if present, for both to play on each hole.",
            "examples": ["one partner can represent", "during any part of round", "both don't need to be present", "both don't need to play each hole"]
        },
        {
            "situation": "Late arriving partner in match play",
            "explanation": "Under Rule 23.4, in match play, if a partner arrives after any player in the match has started a hole, that partner is not allowed to play until the next hole.",
            "examples": ["arrive after hole started", "not allowed until next hole", "any player in match", "match play restriction"]
        },
        {
            "situation": "Late arriving partner in stroke play",
            "explanation": "Under Rule 23.4, in stroke play, if a partner arrives after the other partner has started a hole, the arriving partner is not allowed to play until the next hole.",
            "examples": ["arrive after other partner started", "not allowed until next hole", "stroke play rule", "partner-specific timing"]
        },
        {
            "situation": "Actions allowed by arriving partner not playing",
            "explanation": "Under Rule 23.4, an arriving partner who is not allowed to play on a hole may still give advice or help to the other partner and take other actions for the other partner on that hole.",
            "examples": ["can give advice", "can help other partner", "can take actions for partner", "assistance still allowed"]
        },
        {
            "situation": "Penalty for playing when not allowed",
            "explanation": "Under Rule 23.4, the penalty for making a stroke when not allowed to play a hole is the general penalty.",
            "examples": ["general penalty", "stroke when not allowed", "timing violation", "loss of hole or two strokes"]
        }
    ]
    },
    {
        "id": "23.5",
        "title": "Player's Actions Affecting Partner's Play",
        "text": "A player may take any action concerning the partner's ball that the partner is allowed to take before making a stroke, such as marking, lifting, replacing, dropping and placing the ball. Any action taken by the player concerning the partner's ball is treated as having been taken by the partner.",
        "keywords": ["player actions", "partner's ball", "partner allowed", "before stroke", "marking", "lifting", "replacing", "dropping", "placing", "treated as partner"],
        "examples": [
            "marking partner's ball",
            "helping with partner's equipment",
            "actions treated as partner's",
            "partner responsibility for actions"
        ],
        "conditions": [
        {
            "situation": "Actions player may take for partner",
            "explanation": "Under Rule 23.5a, a player may take any action concerning the partner's ball that the partner is allowed to take before making a stroke, such as marking, lifting, replacing, dropping, and placing the ball.",
            "examples": ["mark partner's ball", "lift replace drop place", "any action partner could take", "before making stroke"]
        },
        {
            "situation": "Help and advice limitations",
            "explanation": "Under Rule 23.5a, a player and caddie may help the partner in any way the partner's caddie is allowed to help (like advice), but must not give help that a partner's caddie is not allowed to give, as defined in Rule 10.2.",
            "examples": ["same as caddie help rules", "can give advice", "cannot exceed caddie limitations", "follow existing help rules", "cannot stand behind partner's ball or behind the hole when partner is making a putt"]
        },
        {
            "situation": "Restriction on leaving ball to help others",
            "explanation": "Under Rule 23.5a, in stroke play, partners must not agree to leave a ball in place on the putting green to help either of them or any other player.",
            "examples": ["cannot leave ball to help", "putting green restriction", "stroke play only", "no agreement to help"]
        },
        {
            "situation": "Partner responsibility for player's actions",
            "explanation": "Under Rule 23.5b, any action taken by the player concerning the partner's ball or equipment is treated as having been taken by the partner, and if it would breach a Rule, the partner gets the penalty.",
            "examples": ["action treated as partner's", "partner gets penalty", "player breaches rule", "partner responsible"]
        },
        {
            "situation": "Examples of partner responsibility",
            "explanation": "Under Rule 23.5b, examples include when player improves conditions for partner's stroke, accidentally causes partner's ball to move, or fails to mark partner's ball before lifting.",
            "examples": ["improving conditions", "causing ball to move", "failing to mark", "partner gets penalty"]
        },
        {
            "situation": "When actions affect both players",
            "explanation": "Under Rule 23.5b, if player's or caddie's actions affect both the player's own ball and partner's ball, see Rule 23.9a(2) for when both partners get penalties.",
            "examples": ["actions affect both balls", "both partners may get penalty", "see Rule 23.9a(2)", "dual impact situations"]
        }
    ]
    },
    {
        "id": "23.6",
        "title": "Side's Order of Play",
        "text": "Partners may play in the order the side considers best. This means that when it is a player's turn to play under Rule 6.4a (match play) or 6.4b (stroke play), either the player or their partner may play next. Exception: A player must not continue play after their next stroke has been conceded if this would help their partner.",
        "keywords": ["partners", "order", "side considers best", "player's turn", "either player", "partner", "play next", "exception", "stroke conceded", "help partner"],
        "examples": [
            "flexible playing order",
            "strategic order choice",
            "continuing after concession",
            "helping partner restriction"
        ],
        "conditions": [
        {
            "situation": "Flexible order of play",
            "explanation": "Under Rule 23.6, partners may play in the order the side considers best, meaning when it's a player's turn under Rules 6.4a or 6.4b, either the player or their partner may play next.",
            "examples": ["side chooses order", "strategic flexibility", "either player can go", "best order for side"]
        },
        {
            "situation": "Normal turn-taking modified",
            "explanation": "Under Rule 23.6, the normal individual turn-taking rules are modified to allow either partner to play when it would normally be one specific player's turn.",
            "examples": ["normal rules modified", "either partner option", "strategic advantage", "team decision"]
        },
        {
            "situation": "Exception for continuing after concession",
            "explanation": "Under Rule 23.6, a player must not continue play of a hole after their next stroke has been conceded if this would help their partner. If they do, their score stands without penalty but partner's score cannot count.",
            "examples": ["cannot continue after concession", "would help partner", "score stands no penalty", "partner score doesn't count"]
        }
    ]
    },
    {
        "id": "23.7",
        "title": "Partners May Share Clubs",
        "text": "Rule 4.1b(2) is modified to allow partners to share clubs, so long as the total number of clubs they have together is not more than 14.",
        "keywords": ["partners", "share clubs", "Rule 4.1b(2)", "modified", "total number", "together", "not more than 14"],
        "examples": [
            "sharing clubs between partners",
            "14 club limit for side",
            "combined club count",
            "equipment sharing rules"
        ],
        "conditions": [
        {
            "situation": "Partners may share clubs",
            "explanation": "Under Rule 23.7, partners are allowed to share clubs with each other, which is a modification of Rule 4.1b(2) that normally prohibits sharing clubs.",
            "examples": ["partners can share", "modification of normal rule", "sharing allowed", "equipment flexibility"]
        },
        {
            "situation": "14 club limit applies to side",
            "explanation": "Under Rule 23.7, while partners may share clubs, the total number of clubs they have together as a side must not be more than 14.",
            "examples": ["14 club maximum for side", "combined total", "not 14 each", "side limit not individual"]
        },
        {
            "situation": "A player uses a parner's club, but they each have 14 clubs",
            "explanation": "If a player uses a partner's club, and the total number of clubs they have together exceeds 14, then Rule 4.1b applies.",
            "examples": ["14 club maximum for side", "combined total", "each player has 14 clubs", "sharing clubs", "side limit not individual"]
        }
    ]
    },
    {
        "id": "23.8",
        "title": "Restriction on Player Standing Behind Partner When Stroke Made",
        "text": "In addition to the limitations in Rule 10.2b(4), a player must not stand on or close to an extension of the line of play behind the ball while their partner is making a stroke to gain information for their (the player's) next stroke. Penalty for Breach of Rule 23.8: General Penalty.",
        "keywords": ["restriction", "standing behind", "partner", "stroke made", "Rule 10.2b(4)", "extension", "line of play", "gain information", "next stroke", "general penalty"],
        "examples": [
            "cannot stand behind partner",
            "line of play positioning",
            "gaining information penalty",
            "partner positioning rules"
        ],
        "conditions": [
        {
            "situation": "Restriction on standing behind partner",
            "explanation": "Under Rule 23.8, in addition to Rule 10.2b(4) limitations, a player must not stand on or close to an extension of the line of play behind the ball while their partner is making a stroke.",
            "examples": ["cannot stand behind partner", "cannnot watch partner's putt from behind the ball", "line of play extension", "additional to Rule 10.2b(4)", "positioning restriction"]
        },
        {
            "situation": "Purpose - gaining information",
            "explanation": "Under Rule 23.8, the restriction prevents a player from standing behind their partner's stroke to gain information for the player's own next stroke.",
            "examples": ["prevent gaining information", "for player's next stroke", "unfair advantage", "information gathering restriction"]
        },
        {
            "situation": "Penalty for violation",
            "explanation": "Under Rule 23.8, the penalty for breaching this restriction is the general penalty.",
            "examples": ["general penalty", "loss of hole or two strokes", "significant penalty", "positioning violation"]
        }
    ]
    },
    {
        "id": "23.9",
        "title": "When Penalty Applies to One Partner Only or Applies to Both Partners",
        "text": "When a player gets a penalty for breach of a Rule, the penalty may apply either to that player alone or to both partners (the side). This depends on the penalty and the form of play. Most penalties apply only to the individual player, but some apply to both partners or result in side disqualification.",
        "keywords": ["penalty applies", "one partner", "both partners", "side", "depends on", "penalty", "form of play", "individual player", "side disqualification"],
        "examples": [
            "individual vs side penalties",
            "when both partners penalized",
            "disqualification rules",
            "penalty application rules"
        ],
        "conditions": [
        {
            "situation": "Normal penalty application - individual only",
            "explanation": "Under Rule 23.9a(1), when a player gets a penalty other than disqualification, it normally applies only to that player, not the partner. Penalty strokes are added only to the player's score, and in match play, a player with general penalty has no score that can count but doesn't affect the partner.",
            "examples": ["penalty to individual only", "penalty strokes to player only", "partner unaffected", "normal rule application"]
        },
        {
            "situation": "Penalty applies to both partners - club limit breach",
            "explanation": "Under Rule 23.9a(2), when a player breaches Rule 4.1b (14 club limit), in match play the side gets the penalty (match score adjustment), and in stroke play the partner also gets the same penalty.",
            "examples": ["14 club limit breach", "match score adjustment", "partner gets same penalty", "side penalty"]
        },
        {
            "situation": "Penalty applies to both partners - helps partner's play",
            "explanation": "Under Rule 23.9a(2), when a player's breach helps the partner's play, in either match play or stroke play, the partner also gets the same penalty as the player.",
            "examples": ["breach helps partner", "partner gets same penalty", "both match and stroke play", "assistance penalty"]
        },
        {
            "situation": "Penalty applies to both partners - hurts opponent in match play",
            "explanation": "Under Rule 23.9a(2), in match play, when a player's breach hurts opponent's play, the partner also gets the same penalty as the player.",
            "examples": ["breach hurts opponent", "match play only", "partner gets same penalty", "opponent impact"]
        },
        {
            "situation": "Exception for wrong ball",
            "explanation": "Under Rule 23.9a(2), a player who makes a stroke at a wrong ball is not treated as helping partner's play or hurting opponent's play. Only the player gets the general penalty for Rule 6.3c breach, regardless of whose ball it was.",
            "examples": ["wrong ball exception", "only player penalized", "not helping or hurting", "regardless of ball ownership"]
        },
        {
            "situation": "Side disqualification - one partner breach",
            "explanation": "Under Rule 23.9b(1), a side is disqualified if either partner gets disqualification under specific Rules including conduct, equipment, play rules, and format-specific Rules.",
            "examples": ["either partner disqualified", "specific rules listed", "conduct equipment play", "side disqualification"]
        },
        {
            "situation": "Side disqualification - both partners breach",
            "explanation": "Under Rule 23.9b(2), a side is disqualified if both partners get disqualification under Rules like starting/ending, groups, play suspension, or in stroke play if both get hole-specific disqualifications on same hole.",
            "examples": ["both partners disqualified", "specific rules require both", "same hole in stroke play", "dual breach requirement"]
        },
        {
            "situation": "Individual hole disqualification",
            "explanation": "Under Rule 23.9b(3), in other disqualification situations, the player is not disqualified but their score on the breach hole cannot count for the side. If both partners breach such Rules on same hole in match play, side loses the hole.",
            "examples": ["hole-specific disqualification", "score doesn't count", "both breach same hole", "side loses hole"]
        }
    ]
    },
    {
        "id": "24",
        "title": "Team Competitions",
        "text": "Rule 24 covers team competitions (played in either match play or stroke play), where multiple players or sides compete as a team with the results of their rounds or matches combined to produce an overall team score.",
        "keywords": ["team competitions", "multiple players", "sides", "compete", "team", "rounds", "matches", "combined", "overall team score"],
        "examples": [
            "team match play competitions",
            "team stroke play events",
            "combining individual scores",
            "multi-player team formats"
    ]
    },
    {
        "id": "24.1",
        "title": "Overview of Team Competitions",
        "text": "A 'team' is a group of players who play as individuals or as sides to compete against other teams. Their play in the team event may also be part of another competition (such as individual stroke play) that takes place at the same time. Rules 1-23 apply in a team competition, as modified by these specific Rules.",
        "keywords": ["overview", "team", "group of players", "individuals", "sides", "compete", "other teams", "another competition", "same time", "rules 1-23 apply", "specific rules"],
        "examples": [
            "team competition structure",
            "simultaneous individual competition",
            "players vs sides format",
            "dual competition events"
        ],
        "conditions": [
        {
            "situation": "Definition of a team",
            "explanation": "Under Rule 24.1, a 'team' is a group of players who play as individuals or as sides to compete against other teams.",
            "examples": ["group of players", "individuals or sides", "compete against other teams", "team structure"]
        },
        {
            "situation": "Simultaneous competitions",
            "explanation": "Under Rule 24.1, player's play in the team event may also be part of another competition (such as individual stroke play) that takes place at the same time.",
            "examples": ["team event plus individual", "simultaneous competitions", "dual scoring", "same rounds count twice"]
        },
        {
            "situation": "Which rules apply in team competitions",
            "explanation": "Under Rule 24.1, Rules 1-23 apply in team competitions, as modified by the specific Rules in Rule 24.",
            "examples": ["Rules 1-23 apply", "modified by Rule 24", "individual/partnership rules", "team modifications"]
        }
    ]
    },
    {
        "id": "24.2",
        "title": "Terms of Team Competition",
        "text": "The Committee decides the form of play, how a team's overall score is to be calculated and other Terms of the Competition, such as: In match play, the number of points awarded for winning or tying a match. In stroke play, the number of scores to count in each team's total score. Whether the competition may end in a tie and, if not, how the tie will be decided.",
        "keywords": ["committee decides", "form of play", "overall score", "calculated", "terms of competition", "match play", "points awarded", "stroke play", "scores to count", "tie", "tie decided"],
        "examples": [
            "committee sets team format",
            "point systems in team match play",
            "counting scores in team stroke play",
            "tie-breaking procedures"
        ],
        "conditions": [
        {
            "situation": "Committee authority over team format",
            "explanation": "Under Rule 24.2, the Committee decides the form of play, how a team's overall score is calculated, and other Terms of the Competition for team events.",
            "examples": ["committee decides format", "overall score calculation", "terms of competition", "administrative control"]
        },
        {
            "situation": "Match play team scoring",
            "explanation": "Under Rule 24.2, in match play team competitions, the Committee decides the number of points awarded for winning or tying a match.",
            "examples": ["points for winning match", "points for tying match", "committee sets point values", "match play scoring system"]
        },
        {
            "situation": "Stroke play team scoring",
            "explanation": "Under Rule 24.2, in stroke play team competitions, the Committee decides the number of scores to count in each team's total score.",
            "examples": ["how many scores count", "team total calculation", "best scores selection", "committee determines counting method"]
        },
        {
            "situation": "Tie procedures",
            "explanation": "Under Rule 24.2, the Committee decides whether the competition may end in a tie and, if not, how ties will be decided.",
            "examples": ["ties allowed or not", "tie-breaking methods", "playoff procedures", "committee sets tie rules"]
        }
    ]
    },
    {
        "id": "24.3",
        "title": "Team Captain",
        "text": "Each team may name a team captain to lead the team and make decisions for it, such as which players on the team will play in which rounds or matches, in what order they will play and who will play together as partners. The team captain may be a player in the competition.",
        "keywords": ["team captain", "lead team", "make decisions", "which players", "rounds", "matches", "order", "play together", "partners", "player in competition"],
        "examples": [
            "captain making lineup decisions",
            "captain as playing member",
            "team leadership role",
            "strategic team decisions"
        ],
        "conditions": [
        {
            "situation": "Team captain role and authority",
            "explanation": "Under Rule 24.3, each team may name a team captain to lead the team and make decisions such as which players play in which rounds or matches, playing order, and partnership selections.",
            "examples": ["lead the team", "make lineup decisions", "playing order", "partnership selections"]
        },
        {
            "situation": "Captain decision-making responsibilities",
            "explanation": "Under Rule 24.3, the team captain makes strategic decisions about which players will play in specific rounds or matches, the order they will play, and who will play together as partners.",
            "examples": ["which players play", "specific rounds or matches", "playing order decisions", "partner pairings"]
        },
        {
            "situation": "Captain as competing player",
            "explanation": "Under Rule 24.3, the team captain may be a player in the competition, combining leadership responsibilities with playing duties.",
            "examples": ["captain can play", "dual role", "playing captain", "leadership while competing"]
        }
    ]
    },
    {
        "id": "24.4",
        "title": "Advice Allowed in Team Competition",
        "text": "The Committee may adopt a Local Rule allowing each team to name one person (an 'advice giver') who may give advice and other help to players on the team during a round. Team members cannot give advice to each other except when playing as partners, but special Local Rules may modify this restriction.",
        "keywords": ["advice allowed", "committee", "local rule", "advice giver", "give advice", "help", "team members", "except partners", "local rules", "modify restriction"],
        "examples": [
            "team advice giver rules",
            "advice between team members",
            "captain giving advice",
            "local rule modifications"
        ],
        "conditions": [
        {
            "situation": "Committee may allow advice giver",
            "explanation": "Under Rule 24.4a, the Committee may adopt a Local Rule allowing each team to name one person (an 'advice giver') who may give advice and other help as allowed in Rule 10.2b to players on the team during a round.",
            "examples": ["committee local rule", "one advice giver", "give advice and help", "Rule 10.2b assistance"]
        },
        {
            "situation": "Who can be advice giver",
            "explanation": "Under Rule 24.4a, the advice giver may be the team captain, a team coach, or other person (including a team member playing in the competition), but must be identified to the Committee before giving advice.",
            "examples": ["team captain", "team coach", "other person", "playing team member", "must be identified"]
        },
        {
            "situation": "Advice giver flexibility",
            "explanation": "Under Rule 24.4a, the Committee may allow a team's advice giver to change during a round or during the competition, providing flexibility in advice-giving arrangements.",
            "examples": ["advice giver can change", "during round or competition", "committee allows changes", "flexible arrangements"]
        },
        {
            "situation": "Restriction on playing advice giver",
            "explanation": "Under Rule 24.4b, if a team's advice giver is a player on the team, they are not allowed to act in that role while playing a round in the competition. While playing, they are treated like any other team member for advice restrictions.",
            "examples": ["cannot give advice while playing", "treated like other players", "advice restrictions apply", "dual role limitation"]
        },
        {
            "situation": "No advice between team members except partners",
            "explanation": "Under Rule 24.4c, except when playing together as partners on a side, a player must not ask for or give advice to a team member playing on the course, whether in the same group or another group.",
            "examples": ["no advice except partners", "same group or different group", "cannot ask or give", "team member restriction"]
        },
        {
            "situation": "Local rule for same group advice",
            "explanation": "Under Rule 24.4c, in stroke play team competitions where a player's score counts only as part of the team score, the Committee may adopt a Local Rule allowing team members in the same group to give each other advice even if not partners.",
            "examples": ["stroke play team only", "score counts for team only", "same group advice", "local rule modification"]
        },
        {
            "situation": "Penalty for advice violations",
            "explanation": "Under Rule 24.4, the penalty for breaching advice rules in team competition is the general penalty under Rule 10.2.",
            "examples": ["general penalty", "Rule 10.2 penalty", "advice violation", "loss of hole or two strokes"]
        }
    ]
    },

    # --- Section 25: Modifications for Players with Disabilities ---
    {
        "id": "25",
        "title": "Modifications for Players with Disabilities",
        "text": "Rule 25 provides modifications to certain Rules of Golf to allow players with specific disabilities to play fairly with players who have no disabilities, the same disability or a different type of disability.",
        "keywords": ["modifications", "players with disabilities", "specific disabilities", "play fairly", "no disabilities", "same disability", "different type"],
        "examples": [
            "disability accommodations in golf",
            "modified rules for disabled players",
            "fair play across disability types",
            "accessibility modifications"
        ]
    },
    {
        "id": "25.1",
        "title": "Overview",
        "text": "Rule 25 applies to all competitions, including all forms of play. It is a player's category of disability and eligibility that determine whether they can use the specific modified Rules in Rule 25. Rule 25 modifies certain Rules for players who are blind, amputees, use assistive mobility devices, and have intellectual disabilities.",
        "keywords": ["overview", "all competitions", "forms of play", "category of disability", "eligibility", "blind", "amputees", "assistive mobility devices", "intellectual disabilities"],
        "examples": [
            "disability categories covered",
            "eligibility requirements",
            "competition applicability",
            "modified rules overview"
        ],
        "conditions": [
        {
            "situation": "Rule 25 application scope",
            "explanation": "Under Rule 25.1, Rule 25 applies to all competitions, including all forms of play. A player's category of disability and eligibility determine whether they can use the specific modified Rules.",
            "examples": ["all competitions", "all forms of play", "disability category determines eligibility", "specific modifications available"]
        },
        {
            "situation": "Covered disability categories",
            "explanation": "Under Rule 25.1, Rule 25 modifies certain Rules for players who are blind (including certain vision impairments), amputees (limb deficiencies and limb loss), those who use assistive mobility devices, and those with intellectual disabilities.",
            "examples": ["blind and vision impaired", "amputees and limb deficiencies", "assistive mobility device users", "intellectual disabilities"]
        },
        {
            "situation": "Non-covered disability types",
            "explanation": "Under Rule 25.1, many other disability types (neurological conditions, orthopaedic conditions, short stature, deaf players) are not covered in Rule 25 as no requirement for Rules modification has been identified to date.",
            "examples": ["neurological conditions", "orthopaedic conditions", "short stature", "deaf players", "no modification needed"]
        },
        {
            "situation": "Equipment Rules application",
            "explanation": "Under Rule 25.1, the Equipment Rules apply without modification, except as provided in Section 7 of the Equipment Rules. For equipment use for medical reasons, see Rule 4.3b.",
            "examples": ["Equipment Rules apply", "Section 7 exceptions", "medical equipment use", "Rule 4.3b reference"]
        }
    ]
    },
    {
        "id": "25.2",
        "title": "Modifications for Players Who Are Blind",
        "text": "Rule 25.2 allows a player who is blind (which includes certain levels of visual impairment) to be assisted by both an aide and a caddie at the same time, allows help with aiming, gives the player a limited exception to the prohibitions on touching sand in a bunker with a club and allows help with lifting, dropping, placing and replacing a ball.",
        "keywords": ["blind", "visual impairment", "aide", "caddie", "same time", "help with aiming", "touching sand", "bunker", "lifting", "dropping", "placing", "replacing"],
        "examples": [
            "aide assistance for blind players",
            "aiming help for blind players",
            "bunker sand touching exception",
            "ball handling assistance"
        ],
        "conditions": [
        {
            "situation": "Help from an aide",
            "explanation": "Under Rule 25.2a, a player who is blind may get help from an aide in taking a stance, with aiming before the stroke, and by asking for and getting advice. An aide has the same status as a caddie with specific exceptions.",
            "examples": ["taking stance help", "aiming assistance", "advice from aide", "caddie-like status"]
        },
        {
            "situation": "One aide limitation",
            "explanation": "Under Rule 25.2b, a player who is blind may have only one aide at a time. Having more than one aide results in general penalty for each hole where that breach happened.",
            "examples": ["only one aide", "general penalty for multiple aides", "each hole penalty", "same as caddie rule"]
        },
        {
            "situation": "Object setting for aiming assistance",
            "explanation": "Under Rule 25.2c, Rule 10.2b(3) is modified so there's no penalty if player, caddie, or aide sets an object down to help with aiming or taking stance (like a club showing aim direction), but object must be removed before stroke.",
            "examples": ["club set for aiming", "object for stance help", "must remove before stroke", "no penalty exception"]
        },
        {
            "situation": "Positioning behind ball exception",
            "explanation": "Under Rule 25.2d, Rule 10.2b(4) is modified so there's no penalty if aide or caddie is positioned on or close to extension of line of play behind ball, as long as they don't help in making the stroke.",
            "examples": ["behind ball positioning", "no penalty exception", "cannot help with stroke", "aide or caddie allowed"]
        },
        {
            "situation": "Aide and caddie simultaneously",
            "explanation": "Under Rule 25.2e, the aide may also serve as caddie but isn't required to. Player may have both aide and caddie, but aide must not carry/handle clubs except when guiding, helping stance/aiming, or courtesy help.",
            "examples": ["aide as caddie optional", "both aide and caddie allowed", "limited club handling", "guiding and stance help only"]
        },
        {
            "situation": "Bunker sand touching exception",
            "explanation": "Under Rule 25.2f, before making stroke in bunker, blind player may touch sand with club in area right in front of or behind ball and in backswing, without penalty, but must not improve lie more than light grounding would.",
            "examples": ["touch sand in front/behind ball", "backswing touching allowed", "cannot improve lie", "light grounding standard"]
        },
        {
            "situation": "Ball lifting on putting green",
            "explanation": "Under Rule 25.2g, when ball lies on putting green, Rule 14.1b is modified so player's aide, in addition to caddie, may lift ball without player's authorization.",
            "examples": ["aide can lift on green", "no authorization needed", "in addition to caddie", "putting green only"]
        },
        {
            "situation": "General authorization for ball handling",
            "explanation": "Under Rule 25.2h, all Rules requiring player to drop, place, or replace ball are modified so player may give general authorization to any other person to drop, place, and replace their ball without limitation.",
            "examples": ["general authorization allowed", "any other person", "drop place replace", "without limitation"]
        }
    ]
    },
    {
        "id": "25.3",
        "title": "Modifications for Players Who Are Amputees",
        "text": "Rule 25.3 allows a player who is an amputee (which means both those with limb deficiencies and those who have lost a limb) to use a prosthetic device and make a stroke while anchoring the club, and allows help with dropping, placing and replacing a ball.",
        "keywords": ["amputees", "limb deficiencies", "lost limb", "prosthetic device", "anchoring club", "dropping", "placing", "replacing"],
        "examples": [
            "prosthetic device use",
            "anchoring club for amputees",
            "ball handling assistance",
            "limb deficiency accommodations"
        ],
        "conditions": [
        {
            "situation": "Prosthetic device status",
            "explanation": "Under Rule 25.3a, use of artificial arm or leg is not a breach of Rule 4.3 provided player has medical reason and Committee decides it gives no unfair advantage. Player still subject to Rule 4.3a prohibitions on abnormal equipment use.",
            "examples": ["artificial arm or leg allowed", "medical reason required", "committee approval", "no unfair advantage"]
        },
        {
            "situation": "Anchoring exception for amputees",
            "explanation": "Under Rule 25.3b, if amputee player is unable to hold and swing majority of clubs without anchoring due to limb deficiencies or loss, they may make stroke while anchoring club without Rule 10.1b penalty.",
            "examples": ["unable to hold without anchoring", "limb deficiencies or loss", "anchoring allowed", "no Rule 10.1b penalty"]
        },
        {
            "situation": "General authorization for ball handling",
            "explanation": "Under Rule 25.3c, all Rules requiring player to drop, place, or replace ball are modified so amputee player may give general authorization to any other person to drop, place, and replace their ball without limitation.",
            "examples": ["general authorization allowed", "any other person", "drop place replace", "without limitation"]
        },
        {
            "situation": "Modified definition of replace",
            "explanation": "Under Rule 25.3d, for amputee players, the definition of replace (and Rule 14.2b(2)) is modified to allow replacing ball either by hand or using other equipment (such as rolling ball with club).",
            "examples": ["replace by hand or equipment", "rolling with club", "modified definition", "equipment assistance"]
        }
    ]
    },
    {
        "id": "25.4",
        "title": "Modifications for Players Who Use Assistive Mobility Devices",
        "text": "Rule 25.4 allows a player who uses an assistive mobility device to be assisted by both an aide and a caddie at the same time, explains how a player may use an assistive mobility device (such as a wheelchair or other wheeled mobility device or a cane or a crutch) to help in taking a stance and making a stroke, and modifies certain relief procedures.",
        "keywords": ["assistive mobility devices", "aide", "caddie", "wheelchair", "wheeled mobility device", "cane", "crutch", "stance", "stroke", "relief procedures"],
        "examples": [
            "wheelchair golf accommodations",
            "cane and crutch use",
            "mobility device stance modifications",
            "expanded relief areas"
        ],
        "conditions": [
        {
            "situation": "Help from aide or other person",
            "explanation": "Under Rule 25.4a, player using assistive mobility device may get help from aide or any other person (including another player) with: lifting ball on putting green, dropping/placing/replacing ball, and positioning player or device before stroke.",
            "examples": ["aide or other person help", "lifting on green", "ball handling", "positioning assistance"]
        },
        {
            "situation": "Advice from aide",
            "explanation": "Under Rule 25.4b, player may ask for and get advice from aide same way as from caddie under Rule 10.2a. Aide has same status as caddie with specific exceptions. Player may get advice from both aide and caddie simultaneously.",
            "examples": ["advice from aide", "same as caddie status", "both aide and caddie", "Rule 10.2a applies"]
        },
        {
            "situation": "One aide limitation",
            "explanation": "Under Rule 25.4c, player using assistive mobility device may have only one aide at a time. Multiple aides result in general penalty for each hole where breach happened.",
            "examples": ["only one aide", "general penalty for multiple", "each hole penalty", "same as caddie rule"]
        },
        {
            "situation": "Modified definition of stance",
            "explanation": "Under Rule 25.4d, definition of stance is modified to mean 'position of player's feet and body, and position of assistive mobility device if used, in preparing for or making stroke' for various Rules applications.",
            "examples": ["includes device position", "feet body and device", "preparing or making stroke", "various Rules applications"]
        },
        {
            "situation": "Modified definition of replace",
            "explanation": "Under Rule 25.4e, definition of replace (and Rule 14.2b(2)) is expanded to allow replacing ball either by hand or using other equipment (such as rolling ball with club).",
            "examples": ["replace by hand or equipment", "rolling with club", "expanded definition", "equipment assistance"]
        },
        {
            "situation": "Equipment use standards",
            "explanation": "Under Rule 25.4f, Rule 4.3 applies to assistive mobility devices: player may use devices if allowed under Rule 4.3b standards, but still subject to Rule 4.3a prohibitions on abnormal equipment use.",
            "examples": ["Rule 4.3 applies", "allowed under 4.3b", "prohibited abnormal use", "equipment standards"]
        },
        {
            "situation": "Digging in with device for stance",
            "explanation": "Under Rule 25.4g, Rule 8.1b(5) is modified so 'reasonable digging in with feet' includes reasonable digging with device and reasonable actions to position device and avoid slipping, but not building stance to prevent slipping.",
            "examples": ["digging with device", "positioning to avoid slipping", "cannot build stance", "reasonable actions only"]
        },
        {
            "situation": "Anchoring exception for device users",
            "explanation": "Under Rule 25.4h, if player unable to hold and swing majority of clubs without anchoring due to assistive mobility device use, they may make stroke while anchoring club without Rule 10.1b penalty.",
            "examples": ["unable to hold without anchoring", "due to device use", "anchoring allowed", "no Rule 10.1b penalty"]
        },
        {
            "situation": "Standing across line modification",
            "explanation": "Under Rule 25.4i, Rule 10.1c is modified so player must also not make stroke with any part of assistive mobility device deliberately placed on each side of or touching line of play or extension behind ball.",
            "examples": ["device cannot straddle line", "deliberately placed", "line of play or extension", "same restriction as body"]
        },
        {
            "situation": "Aide as caddie with device users",
            "explanation": "Under Rule 25.4j, aide may serve as caddie but not required. Player may have both, but aide must not carry/handle clubs except for stance/lineup help or courtesy, without modifying Rule 10.2b(3).",
            "examples": ["aide as caddie optional", "both allowed", "limited club handling", "stance and lineup help only"]
        },
        {
            "situation": "Ball accidentally hitting device on green",
            "explanation": "Under Rule 25.4k, Rule 11.1b(2) is modified so if player's ball in motion from putting green accidentally hits assistive mobility device, ball must be played as it lies.",
            "examples": ["accidentally hits device", "from putting green", "play as it lies", "no penalty"]
        },
        {
            "situation": "Testing sand conditions with device",
            "explanation": "Under Rule 25.4l, Rule 12.2b(1) applies to using device to deliberately test sand conditions (prohibited), but player may touch sand with device for any other purpose without penalty.",
            "examples": ["deliberate testing prohibited", "other purposes allowed", "touch sand with device", "intent matters"]
        },
        {
            "situation": "Expanded relief area for wheeled devices",
            "explanation": "Under Rule 25.4m, when player with wheeled mobility device takes lateral relief for ball in red penalty area or unplayable ball, relief area is expanded from two club-lengths to four club-lengths.",
            "examples": ["wheeled device only", "red penalty area relief", "unplayable ball relief", "four club-lengths instead of two"]
        },
        {
            "situation": "Bunker relief modification for wheeled devices",
            "explanation": "Under Rule 25.4n, when player with wheeled mobility device takes relief for unplayable ball in bunker, Rule 19.3b is modified to allow back-on-line relief outside bunker for one penalty stroke.",
            "examples": ["wheeled device only", "unplayable in bunker", "back-on-line outside bunker", "one penalty stroke"]
        }
    ]
    },
    {
        "id": "25.5",
        "title": "Modifications for Players With Intellectual Disabilities",
        "text": "Rule 25.5 allows a player with intellectual disability to be assisted by both an aide and a caddie at the same time, and clarifies the role of a supervisor, who is not assigned to a specific player and is not allowed to give advice.",
        "keywords": ["intellectual disabilities", "aide", "caddie", "same time", "supervisor", "not assigned", "specific player", "not allowed", "advice"],
        "examples": [
            "aide assistance for intellectual disabilities",
            "supervisor vs aide roles",
            "advice restrictions",
            "individualized help needs"
        ],
        "conditions": [
        {
            "situation": "Help from aide or supervisor",
            "explanation": "Under Rule 25.5a, Committee may provide aide (helps individual player with play and Rules, has caddie status with restrictions) or supervisor (helps any player with intellectual disability as needed, is outside influence, cannot give advice).",
            "examples": ["aide helps individual", "supervisor helps any player", "aide has caddie status", "supervisor is outside influence"]
        },
        {
            "situation": "Aide vs supervisor distinction",
            "explanation": "Under Rule 25.5a, aide is assigned to individual player and may give advice like caddie, while supervisor is not assigned to specific player, helps any player as needed, and cannot give advice.",
            "examples": ["aide assigned to individual", "aide gives advice", "supervisor not assigned", "supervisor no advice"]
        },
        {
            "situation": "One aide limitation",
            "explanation": "Under Rule 25.5b, player with intellectual disability may have only one aide at a time. Multiple aides result in general penalty for each hole where breach happened.",
            "examples": ["only one aide", "general penalty for multiple", "each hole penalty", "same as caddie rule"]
        },
        {
            "situation": "Aide as caddie modification",
            "explanation": "Under Rule 25.5c, aide may serve as caddie but not required. Player may have both, but aide must not carry/handle clubs except for stance/lineup help (if Committee authorized) or courtesy, without modifying Rule 10.2b(3).",
            "examples": ["aide as caddie optional", "both allowed", "committee authorization for stance help", "limited club handling"]
        },
        {
            "situation": "Ball lifting on putting green",
            "explanation": "Under Rule 25.5d, when ball lies on putting green, Rule 14.1b is modified so player's aide, in addition to caddie, may lift ball without player's authorization.",
            "examples": ["aide can lift on green", "no authorization needed", "in addition to caddie", "putting green only"]
        },
        {
            "situation": "Combined intellectual and physical disabilities",
            "explanation": "Under Rule 25.5e, for players with both intellectual and physical disabilities, Committee should use combination of Rule 25 provisions to address both types of disabilities.",
            "examples": ["both disability types", "combine Rule 25 provisions", "address both types", "committee recommendation"]
        }
    ]
    },
    {
    "id": "25.6",
    "title": "General Provisions for All Categories of Disability",
    "text": "General provisions apply to all disability categories regarding unreasonable delay and dropping procedures. Committees should use discretion in applying time standards and accept reasonable efforts considering physical limitations.",
    "keywords": ["general provisions", "all categories", "unreasonable delay", "dropping procedures", "committee discretion", "time standards", "reasonable efforts", "physical limitations"],
    "examples": [
        "flexible time standards",
        "reasonable delay interpretation",
        "dropping accommodations",
        "committee discretion"
    ],
    "conditions": [
        {
            "situation": "Unreasonable delay considerations",
            "explanation": "Under Rule 25.6a, in applying Rule 5.6a to players with disabilities, Committee should use discretion setting reasonable standards considering course difficulty, weather conditions, competition nature, and extent of disabilities.",
            "examples": ["committee discretion", "course difficulty factor", "weather impact", "disability extent considered"]
        },
        {
            "situation": "Relaxed delay interpretation",
            "explanation": "Under Rule 25.6a, taking various factors into account, it may be appropriate for Committees to use more relaxed interpretation of what constitutes unreasonable delay for players with disabilities.",
            "examples": ["more relaxed interpretation", "various factors considered", "appropriate accommodation", "disability-specific standards"]
        },
        {
            "situation": "Dropping accommodation",
            "explanation": "Under Rule 25.6b, in applying Rule 14.3b, because physical limitations may make it difficult to know if ball dropped from knee height, Committee should accept player's reasonable judgment and all reasonable efforts considering limitations.",
            "examples": ["difficult to know knee height", "accept reasonable judgment", "reasonable efforts", "physical limitations considered"]
        }
    ]
    }
]
