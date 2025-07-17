# Restructured columbia_cc_local_rules_db.py to match official rules format

COLUMBIA_CC_LOCAL_RULES = {
    'club_info': {
        'club_id': 'columbia_cc',
        'club_name': 'Columbia Country Club',
        'rules_date': '2023-04-11',
        'location': 'Chevy Chase, MD',
        'contact': 'your_contact@columbiacc.org'
    },
    
    'local_rules': [  # ← Changed to LIST like official rules
        {
            'id': 'CCC-1',
            'title': 'Ball Lost or Out of Bounds (Alternative Relief)',
            'text': 'When a player\'s ball has not been found or is known or virtually certain to be out of bounds, the player may proceed as follows rather than proceeding under stroke and distance. For two penalty strokes, the player may take relief by dropping the original ball or another ball in a relief area using two estimated reference points.',
            'keywords': ['lost ball', 'out of bounds', 'stroke and distance', 'relief', 'two penalty strokes', 'reference points', 'fairway', 'dropping'],
            'examples': [
                'Ball goes over fence and out of bounds - use alternative relief instead of returning to tee',
                'Ball lost in rough - estimate where it came to rest and take relief',
                'Ball crosses boundary line - use reference point system for relief'
            ],
            'conditions': [  # ← Standardized LIST format
                {
                    'situation': 'When ball has not been found',
                    'explanation': 'Ball has not been found within three-minute search time and player chooses alternative to stroke and distance relief',
                    'examples': ['Ball lost in woods', 'Ball lost in tall grass', 'Ball lost in water but not in penalty area']
                },
                {
                    'situation': 'When ball is known or virtually certain to be out of bounds',
                    'explanation': 'Ball is known or virtually certain to be out of bounds and player chooses alternative relief',
                    'examples': ['Ball seen going over fence', 'Ball clearly beyond boundary markers', 'Ball on road outside course']
                },
                {
                    'situation': 'Relief procedure with reference points',
                    'explanation': 'Player uses two reference points: (1) Ball Reference Point - where ball estimated to come to rest or last crossed boundary, (2) Fairway Reference Point - nearest fairway point to ball reference point but not nearer hole',
                    'examples': ['Drop between lines from hole through each reference point', 'Within two club-lengths of lines', 'Must be in general area and not nearer hole']
                },
                {
                    'situation': 'When this local rule cannot be used',
                    'explanation': 'Player may not use this option when ball is known or virtually certain to be in penalty area, or when player has already played provisional ball under stroke and distance',
                    'examples': ['Ball in water hazard', 'Ball in penalty area', 'Provisional ball already played']
                }
            ]
        },
        
        {
            'id': 'CCC-2',
            'title': 'Penalty Areas - Holes 15, 16, 17, 18',
            'text': 'Special relief options for penalty areas on holes 15, 16, 17, and 18. Players have additional dropping zone options beyond standard penalty area relief.',
            'keywords': ['penalty area', 'dropping zone', 'red penalty area', 'water hazard', 'holes 15 16 17 18', 'extra relief'],
            'examples': [
                'Ball in water on 16th - can use dropping zone instead of going back',
                'Ball in pond on 17th west of bridge - dropping zone available',
                'Ball in creek on 17th right of the bridge - dropping zone NOT available, standard relief only',
                'Ball in penalty area on 15th - treat as red penalty area'
            ],
            'conditions': [
                {
                    'situation': 'Hole 15 penalty area relief',
                    'explanation': 'When ball is in penalty area on hole 15, player must proceed under Rule 17.1 and may consider the penalty area to be a red penalty area',
                    'examples': ['Ball in water on 15th', 'Ball in penalty area on 15th']
                },
                {
                    'situation': 'Hole 16 penalty area relief options',
                    'explanation': 'When ball is in penalty area on hole 16, player has two relief options for one penalty stroke: (1) Standard relief under Rule 17.1, or (2) Drop in designated dropping zone near 16th green',
                    'examples': ['Ball in water on 16th', 'Use dropping zone for better angle to pin']
                },
                {
                    'situation': 'Hole 17 penalty area relief options',
                    'explanation': 'When ball is in penalty area on hole 17, player has relief options for one penalty stroke: (1) Standard relief under Rule 17.1, or (2) If ball is in pond area west of footbridge, drop in designated dropping zone near the foot bridge',
                    'examples': ['Ball in pond west of footbridge', 'Dropping zone only for main pond area']
                },
                {
                    'situation': 'Hole 18 penalty area relief',
                    'explanation': 'When ball is in penalty area on hole 18, player must proceed under Rule 17.1 and may consider the penalty area to be a red penalty area',
                    'examples': ['Ball in water on 18th', 'Ball in penalty area on 18th']
                },
                {
                    'situation': 'Artificial walls in penalty areas',
                    'explanation': 'Artificial walls inside penalty areas of holes 15, 16, 17, and 18 are integral objects from which free relief is not allowed',
                    'examples': ['Stone wall in water hazard', 'Retaining wall in penalty area']
                }
            ]
        },
        
        {
            'id': 'CCC-3',
            'title': 'Penalty Areas - Holes 2, 3, 4',
            'text': 'The entire left side of holes 2, 3, and 4 is a red penalty area. In the absence of painted lines and/or stakes, the edge of the penalty area is defined as the edge of the unmaintained area. Players may play their ball as it lies or take penalty relief under Rule 17.1d.',
            'keywords': ['penalty area', 'red penalty area', 'left side', 'holes 2 3 4', 'unmaintained area', 'stakes', 'painted lines'],
            'examples': [
                'Ball rolls left into rough area on hole 2 - red penalty area relief available',
                'Ball in unmaintained area on left side of hole 3',
                'Ball in scrub area left of fairway on hole 4'
            ],
            'conditions': [
                {
                    'situation': 'Left side penalty area boundary',
                    'explanation': 'The entire left side of holes 2, 3, and 4 is designated as a red penalty area',
                    'examples': ['Left rough area on hole 2', 'Left side vegetation on hole 3', 'Left unmaintained area on hole 4']
                },
                {
                    'situation': 'Boundary definition when no markings',
                    'explanation': 'In the absence of painted lines and/or stakes, the edge of the penalty area is defined as the edge of the unmaintained area',
                    'examples': ['Where maintained grass ends', 'Edge of rough vegetation', 'Transition to scrub area']
                },
                {
                    'situation': 'Relief options',
                    'explanation': 'Players may play their ball as it lies in the penalty area or take penalty relief under Rule 17.1d for one penalty stroke',
                    'examples': ['Play from penalty area as lies', 'Take one penalty stroke relief']
                }
            ]
        },

        {
            'id': 'CCC-4',
            'title': 'Integral Objects - Cart Paths and Roads',
            'text': 'Specific cart paths and roads are designated as integral objects from which free relief is not allowed. The unpaved road behind 12th green and sections of cart path behind 14th and 17th greens marked by green stakes are integral objects. Balls resting on or against these cart paths get NO RELIEF and must play it as it lies or take an unplayable ball penalty.',
            'keywords': ['cart path', 'integral object', 'no relief', 'unpaved road', 'green stakes', 'holes 12 14 17', 'cart path behind green', 'path behind green','path behind twelfth green', 'road behind twelvth green', 'path behind fourteenth green', 'path behind seventeenth green', 'path behind 12th green', 'road behind 12th green', 'path behind 14th green', 'path behind 17th green', 'path behind 12 green', 'road behind 12 green', 'path behind 14 green', 'path behind 17 green', 'cart path behind', 'no free relief','cart path integral', 'path integral object'],
            'examples': [
                'Ball on cart path behind 14th green - no free relief available',
                'Ball on road behind 12th green - no free relief available',
                'Ball on maintenance road elsewhere - free relief under Rule 16.1',
                'Ball on path marked with green stakes - must play as lies'
            ],
            'conditions': [
                {
                    'situation': 'No relief areas - certain paths are integral objects',
                    'explanation': 'No free relief is available from: unpaved road behind 12th green, cart path sections behind 14th green marked by green stakes, cart path sections behind 17th green marked by green stakes',
                    'examples': ['Unpaved road behind 12th green', 'path behind 12th green', 'Cart path behind 14th green with green stakes', 'Cart path behind 17th green with green stakes']
                },
                {
                    'situation': 'Stone wall at 15th tee',
                    'explanation': 'The low stone wall adjacent to cart path at 15th tee is part of the immovable obstruction, but the portion adjacent to integral object cart path is also integral object',
                    'examples': ['Stone wall next to cart path at 15th tee']
                },
                {
                    'situation': 'Other roads and paths - free relief available',
                    'explanation': 'All other roads and paths on course, even if not artificially surfaced, are treated as immovable obstructions from which free relief is allowed under Rule 16.1',
                    'examples': ['Maintenance roads', 'Other cart paths', 'Unpaved paths not marked as integral']
                }
            ]
        },
        
        {
            'id': 'CCC-5',
            'title': 'Fenced Young Trees - Hole 3',
            'text': 'The fenced trees in the penalty area on hole 3 are Temporary Immovable Obstructions (TIO). Free relief may be taken if the TIO interferes with the lie of the ball, stance, or swing, or if the TIO lies directly in the line of sight between the ball and hole.',
            'keywords': ['fenced trees', 'temporary immovable obstruction', 'TIO', 'hole 3', 'penalty area', 'line of sight', 'free relief'],
            'examples': [
                'Ball in penalty area but fenced tree blocks swing - free relief available',
                'Fenced tree blocks line of sight to hole - free relief for line of sight',
                'Ball near fenced tree affecting stance - free relief available'
            ],
            'conditions': [
                {
                    'situation': 'Interference types qualifying for relief',
                    'explanation': 'Free relief available when TIO interferes with: lie of ball, intended stance, area of intended swing, or lies directly in line of sight between ball and hole',
                    'examples': ['Tree cage blocks swing', 'Fence interferes with stance', 'Tree blocks view of hole']
                },
                {
                    'situation': 'Relief procedure within penalty area',
                    'explanation': 'Take free relief by dropping ball within penalty area at nearest point of complete relief (both physical and line of sight), within one club-length, not nearer hole',
                    'examples': ['Drop within penalty area only', 'Complete relief from obstruction', 'Must not be closer to hole']
                },
                {
                    'situation': 'Alternative penalty relief',
                    'explanation': 'Player may also choose to take penalty relief under Rule 17.1d instead of the free TIO relief',
                    'examples': ['Exit penalty area with one penalty stroke', 'Standard penalty area relief options']
                }
            ]
        },
        
        {
            'id': 'CCC-6',
            'title': 'Purple Line and Construction Fence',
            'text': 'The fence around the Purple Line construction area is considered a boundary fence from which free relief is not available. Mesh attached to the fence is part of the fence and considered immovable. A ball coming to rest on or beyond the Purple Line construction area is out of bounds.',
            'keywords': ['purple line', 'construction fence', 'purple line fence', 'boundary fence', 'out of bounds', 'no relief', 'green fence', 'mesh', 'mesh fence', 'construction mesh', 'green mesh', 'behind green', 'behind 1st green', 'behind first green', 'behind 14th green', 'to the right of #2', 'construction area', 'fence behind green', 'temporary fence'],
            'examples': [
                'Ball lands in construction area - out of bounds, proceed under stroke and distance',
                'Ball against purple line fence - no free relief available, play as lies or unplayable',
                'Ball hits mesh on construction fence - no relief from boundary fence'
            ],
            'conditions': [
                {
                    'situation': 'Construction fence as boundary',
                    'explanation': 'The fence around the Purple Line construction area is considered a boundary fence from which free relief is not available',
                    'examples': ['Purple construction fence', 'Temporary boundary fencing', 'No obstruction relief available']
                },
                {
                    'situation': 'Mesh as part of fence',
                    'explanation': 'Mesh attached to the construction fence is part of the fence and is considered immovable - no free relief available',
                    'examples': ['Orange mesh on fence', 'Construction netting', 'Protective screening']
                },
                {
                    'situation': 'Out of bounds determination',
                    'explanation': 'A ball coming to rest in or beyond the Purple Line construction area is out of bounds, even if it comes to rest on another part of the course that is in bounds for other holes',
                    'examples': ['Ball in construction zone', 'Ball beyond purple line markers', 'Out of bounds even if on course']
                },
                {
                    'situation': 'No free relief options',
                    'explanation': 'Ball against or near purple line fence: no free relief available, must play as lies or declare unplayable ball under Rule 19',
                    'examples': ['Ball against construction fence', 'Swing impeded by boundary fence', 'Declare unplayable if needed']
                }
            ]
        },
        {
            'id': 'CCC-7',
            'title': 'Maintenance Facility',
            'text': 'The golf course maintenance facility near holes 9 and 10, including all buildings, storage tanks, sheds, paved areas, gravel surfaced areas, and retention ponds is treated as a single immovable obstruction. Free relief is allowed under Rule 16.1.',
            'keywords': ['maintenance facility', 'maintenance barn', 'immovable obstruction', 'buildings', 'storage tanks', 'sheds', 'paved areas', 'gravel', 'retention ponds', 'holes 9 10', 'free relief'],
            'examples': [
                'Ball near maintenance building - free relief available under Rule 16.1',
                'Ball on maintenance facility roof - free relief from immovable obstruction',
                'Ball interfered by maintenance equipment storage - free relief available'
            ],
            'conditions': [
                {
                    'situation': 'Maintenance facility components',
                    'explanation': 'The maintenance facility includes all buildings, storage tanks, sheds, paved areas, gravel surfaced areas, and retention ponds, all treated as one single immovable obstruction',
                    'examples': ['Main maintenance building', 'Equipment storage sheds', 'Paved maintenance roads', 'Gravel storage areas', 'Retention ponds']
                },
                {
                    'situation': 'Free relief procedure',
                    'explanation': 'When ball is interfered by maintenance facility, player may take free relief under Rule 16.1 by dropping within one club-length of nearest point of complete relief, not nearer hole',
                    'examples': ['Ball behind maintenance building', 'Ball on maintenance facility roof', 'Ball near equipment storage']
                },
                {
                    'situation': 'No penalty for relief',
                    'explanation': 'Relief from maintenance facility is free relief with no penalty stroke, as facility is treated as immovable obstruction',
                    'examples': ['Free drop from building interference', 'No penalty for obstruction relief']
                }
            ]
        },

          {
            'id': 'CCC-8',
            'title': 'Turf Nursery',
            'text': 'The turf nursery adjacent to the maintenance area is a No Play Zone that is to be treated as Ground Under Repair. The No Play Zone is defined as the closely mown area of the turf nursery. Free relief must be taken from interference by the no play zone under Rule 16.1f.',
            'keywords': ['turf nursery', 'no play zone', 'ground under repair', 'mandatory relief', 'closely mown area', 'maintenance area'],
            'examples': [
                'Ball in turf nursery area - must take free relief, cannot play as it lies',
                'Ball near nursery affecting swing - free relief available',
                'Mandatory relief from no play zone'
            ],
            'conditions': [
                {
                    'situation': 'No play zone definition',
                    'explanation': 'The turf nursery adjacent to maintenance area is No Play Zone treated as Ground Under Repair, defined as closely mown area of turf nursery',
                    'examples': ['Closely mown nursery area', 'Designated growing area', 'Restricted maintenance zone']
                },
                {
                    'situation': 'Mandatory relief requirement',
                    'explanation': 'Free relief must be taken from interference by no play zone under Rule 16.1f - player cannot choose to play ball as it lies',
                    'examples': ['Must take relief', 'No option to play as lies', 'Compulsory free relief']
                },
                {
                    'situation': 'Relief procedure',
                    'explanation': 'Take free relief under Rule 16.1f by dropping at nearest point of complete relief, within one club-length, not nearer hole',
                    'examples': ['Drop outside nursery area', 'Complete relief from no play zone', 'Free relief procedure']
                }
            ]
        },
        
        {
            'id': 'CCC-9',
            'title': 'Decorative Planting Areas',
            'text': 'Decorative planting areas, including mulched beds and plants, are part of the General Area with no free relief. Walls and bulkheads around decorative areas are immovable obstructions providing free relief under Rule 16.1.',
            'keywords': ['decorative planting', 'mulched beds', 'general area', 'no relief', 'walls', 'bulkheads', 'immovable obstruction', 'gazebo', 'restroom'],
            'examples': [
                'Ball in mulched bed - no relief, play as it lies',
                'Ball interfered by retaining wall - free relief available',
                'Ball near decorative area wall - obstruction relief under Rule 16.1'
            ],
            'conditions': [
                {
                    'situation': 'Decorative areas as general area',
                    'explanation': 'Decorative planting areas, including mulched beds and plants rooted in them, are part of General Area - free relief is not allowed',
                    'examples': ['Mulched flower beds', 'Planted shrub areas', 'Landscaped garden beds']
                },
                {
                    'situation': 'Walls and bulkheads as obstructions',
                    'explanation': 'Walls and bulkheads around decorative planting areas are immovable obstructions - free relief available under Rule 16.1',
                    'examples': ['Stone retaining walls', 'Concrete bulkheads', 'Decorative barriers']
                },
                {
                    'situation': 'Special exception areas',
                    'explanation': 'Decorative planting areas completely surrounded by cart paths at 6th tee, 13th tee, around restroom at 13th tee, and around gazebo on 18th are part of adjacent immovable obstructions',
                    'examples': ['Landscaping at 6th tee', 'Plants around 13th restroom', 'Gazebo landscaping on 18th']
                },
                {
                    'situation': 'Relief reference point considerations',
                    'explanation': 'When taking relief from wall or bulkhead around decorative planting area, the reference point may not necessarily be outside the decorative planting area',
                    'examples': ['Relief point may be in planting area', 'Nearest relief point determination']
                }
            ]
        },
        
        {
            'id': 'CCC-10',
            'title': 'Immovable Obstructions Close to Putting Greens',
            'text': 'Enhanced relief options when ball and immovable obstructions are close to putting green in area cut to fairway height or less, and obstruction is on line of play. Additional relief available under Rule 16.1b for line of play interference.',
            'keywords': ['immovable obstruction', 'putting green', 'line of play', 'fairway height', 'enhanced relief', 'close to green'],
            'examples': [
                'Ball 30 yards from green, sprinkler head on line to hole - enhanced relief available',
                'Choosing unreasonable line over trees to avoid bunker - no relief',
                'Ball and obstruction both near green - extra relief options'
            ],
            'conditions': [
                {
                    'situation': 'Standard obstruction relief always available',
                    'explanation': 'Relief from interference by immovable obstruction may always be taken under Rule 16.1',
                    'examples': ['Standard obstruction relief', 'Physical interference relief', 'Basic Rule 16.1 relief']
                },
                {
                    'situation': 'Enhanced relief conditions',
                    'explanation': 'Extra relief options available when: ball and obstruction in area cut to fairway height or less, both close to putting green, and obstruction is on line of play',
                    'examples': ['Ball in fairway near green', 'Obstruction between ball and hole', 'Both within two club-lengths of green']
                },
                {
                    'situation': 'Distance requirements for enhanced relief',
                    'explanation': 'Enhanced relief available when obstruction is: on line of play, within two club-lengths of putting green, and within two club-lengths of ball',
                    'examples': ['Sprinkler head on line to hole', 'Cart path between ball and green', 'Yardage marker blocking line']
                },
                {
                    'situation': 'Clearly unreasonable line exception',
                    'explanation': 'No relief under this local rule if player chooses line of play that is clearly unreasonable under the circumstances',
                    'examples': ['Unreasonable club selection', 'Clearly impossible shot line', 'Avoiding normal course features']
                }
            ]
        },
        
        {
            'id': 'CCC-11',
            'title': 'Aeration Holes',
            'text': 'If a player\'s ball lies in or touches an aeration hole, free relief is available under Rule 16.1b in general area or Rule 16.1d on putting green. Interference does not exist if aeration hole only interferes with stance or line of play on putting green.',
            'keywords': ['aeration holes', 'temporary condition', 'stance', 'line of play', 'putting green', 'general area', 'free relief'],
            'examples': [
                'Ball in aeration hole in fairway - free relief available',
                'Ball beside aeration hole but only affects stance - no relief',
                'Ball on green with aeration hole on line of putt - no relief'
            ],
            'conditions': [
                {
                    'situation': 'Ball in general area - aeration hole relief',
                    'explanation': 'When ball lies in or touches aeration hole in general area, player may take free relief under Rule 16.1b. If ball comes to rest in another aeration hole, player may take relief again',
                    'examples': ['Ball in aeration hole in fairway', 'Ball in aeration hole in rough', 'Multiple aeration holes']
                },
                {
                    'situation': 'Ball on putting green - aeration hole relief',
                    'explanation': 'When ball lies in or touches aeration hole on putting green, player may take free relief under Rule 16.1d',
                    'examples': ['Ball in aeration hole on green', 'Ball touching aeration hole on green']
                },
                {
                    'situation': 'No interference situations',
                    'explanation': 'Interference does not exist if aeration hole only interferes with player\'s stance, or on putting green, only interferes with player\'s line of play',
                    'examples': ['Aeration hole only affects stance', 'Aeration hole on line of putt', 'No physical ball interference']
                }
            ]
        },

        {
            'id': 'CCC-12',
            'title': 'Bird Houses',
            'text': 'Bird houses and their posts are immovable obstructions. Free relief is allowed under Rule 16.1.',
            'keywords': ['bird houses', 'posts', 'immovable obstruction', 'free relief'],
            'examples': [
                'Ball near bird house post - free relief available',
                'Bird house interfering with swing - obstruction relief under Rule 16.1'
            ],
            'conditions': [
                {
                    'situation': 'Bird houses as immovable obstructions',
                    'explanation': 'Bird houses and their supporting posts are classified as immovable obstructions',
                    'examples': ['Wooden bird houses', 'Metal bird house posts', 'Nesting boxes']
                },
                {
                    'situation': 'Free relief procedure',
                    'explanation': 'When bird house or post interferes with lie, stance, or swing, free relief is available under Rule 16.1',
                    'examples': ['Drop at nearest point of relief', 'One club-length relief area', 'No penalty for relief']
                }
            ]
        },
        
        {
            'id': 'CCC-13',
            'title': 'Sod Seams',
            'text': 'If a player\'s ball lies in or touches a seam of cut turf, or seam interferes with area of intended swing, free relief available under Rule 16.1b (general area) or Rule 16.1d (putting green). All seams in area treated as same seam.',
            'keywords': ['sod seams', 'cut turf', 'seam interference', 'temporary condition', 'same seam treatment'],
            'examples': [
                'Ball in sod seam affecting swing - free relief available',
                'After relief, ball still affected by different seam - must place under Rule 14.3c(2)',
                'Seam only affects stance - no relief available'
            ],
            'conditions': [
                {
                    'situation': 'Sod seam interference types',
                    'explanation': 'Relief available when: ball lies in seam, ball touches seam, or seam interferes with area of intended swing',
                    'examples': ['Ball sitting in seam line', 'Ball touching seam edge', 'Seam blocks swing path']
                },
                {
                    'situation': 'No interference situations',
                    'explanation': 'Interference does not exist if seam only interferes with player\'s stance',
                    'examples': ['Seam only affects foot placement', 'Stance interference only']
                },
                {
                    'situation': 'Relief procedures by area',
                    'explanation': 'Ball in general area: relief under Rule 16.1b. Ball on putting green: relief under Rule 16.1d',
                    'examples': ['Drop relief in general area', 'Place relief on putting green']
                },
                {
                    'situation': 'Multiple seam treatment',
                    'explanation': 'All seams within area of cut turf treated as same seam. If interference after dropping, must proceed under Rule 14.3c(2) even when ball still within one club-length of reference point',
                    'examples': ['Connected seam lines', 'Secondary relief procedure', 'Place ball if drop fails']
                }
            ]
        }
    ],
    
    # Keep existing search optimization data but update references
    'search_keywords': {
        'lost_ball': ['CCC-1'],
        'out_of_bounds': ['CCC-1', 'CCC-6'],
        'penalty_area': ['CCC-2', 'CCC-3', 'CCC-5'],
        'water_hazard': ['CCC-2', 'CCC-3'],
        'dropping_zone': ['CCC-2'],
        'cart_path': ['CCC-4', 'CCC-9'],
        'obstruction': ['CCC-4', 'CCC-5', 'CCC-7', 'CCC-9', 'CCC-10', 'CCC-12'],
        'construction': ['CCC-6'],
        'purple_line': ['CCC-6'],
        'fence': ['CCC-6'],
        'maintenance': ['CCC-7', 'CCC-8'],
        'aeration': ['CCC-11'],
        'sod_seams': ['CCC-13'],
        'decorative': ['CCC-9'],
        'bird_house': ['CCC-12'],
        'turf_nursery': ['CCC-8'],
        'fenced_trees': ['CCC-5']
    },
    
    'hole_specific_rules': {
       '2': ['CCC-3'],
        '3': ['CCC-3', 'CCC-5'],
        '4': ['CCC-3'],
        '6': ['CCC-9'],
        '9': ['CCC-7', 'CCC-8'],
        '10': ['CCC-7', 'CCC-8'],
        '12': ['CCC-4'],
        '13': ['CCC-9'],
        '14': ['CCC-4'],
        '15': ['CCC-2', 'CCC-4'],
        '16': ['CCC-2'],
        '17': ['CCC-2', 'CCC-4'],
        '18': ['CCC-2', 'CCC-9']
    }
}

# Update helper functions to work with new structure
def get_local_rules_for_hole(hole_number):
    """Get all local rules that apply to a specific hole."""
    hole_str = str(hole_number)
    rules = []
    
    # Get hole-specific rules
    if hole_str in COLUMBIA_CC_LOCAL_RULES['hole_specific_rules']:
        rule_ids = COLUMBIA_CC_LOCAL_RULES['hole_specific_rules'][hole_str]
        for rule_id in rule_ids:
            # Find rule in the list
            for rule in COLUMBIA_CC_LOCAL_RULES['local_rules']:
                if rule['id'] == rule_id:
                    rules.append(rule)
                    break
    
    # Add rules that apply to all holes (if any)
    for rule in COLUMBIA_CC_LOCAL_RULES['local_rules']:
        if rule.get('holes') == 'all':
            rules.append(rule)
    
    return rules

def search_local_rules(query_keywords):
    """Search local rules by keywords."""
    matching_rules = []
    
    for keyword in query_keywords:
        keyword_lower = keyword.lower()
        if keyword_lower in COLUMBIA_CC_LOCAL_RULES['search_keywords']:
            rule_ids = COLUMBIA_CC_LOCAL_RULES['search_keywords'][keyword_lower]
            for rule_id in rule_ids:
                # Find rule in the list
                for rule in COLUMBIA_CC_LOCAL_RULES['local_rules']:
                    if rule['id'] == rule_id and rule not in matching_rules:
                        matching_rules.append(rule)
                        break
    
    return matching_rules

def get_rule_precedence():
    """Return rule precedence for hybrid search system."""
    return COLUMBIA_CC_LOCAL_RULES['rule_precedence']
