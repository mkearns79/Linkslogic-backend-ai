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
            'title': 'Penalty Areas - Holes 13, 15, 16, 17, 18',
            'text': 'Special relief options for penalty areas on holes 15, 16, 17, and 18. Players have additional dropping zone options beyond standard penalty area relief.',
            'keywords': ['penalty area', 'bridge on 13', 'dropping zone', 'red penalty area', 'water hazard', 'holes 13 15 16 17 18', 'extra relief', 'bridge', 'cart bridge', 'footbridge', 'creek', 'pond', 'integral object', 'hole 13'],
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
                    'examples': ['Ball in water on 16th', 'Ball in water on number 16']
                },
                {
                    'situation': 'Hole 17 penalty area relief options',
                    'explanation': 'When ball is in penalty area on hole 17, player has relief options for one penalty stroke: (1) Standard relief under Rule 17.1, or (2) If ball is in the pond or creek area to the LEFT of the footbridge (west side, when viewed from the tee), drop in designated dropping zone near the footbridge. The dropping zone is NOT available for balls in the creek or penalty area to the RIGHT of the footbridge (east side).',
                    'examples': ['Ball in pond west of footbridge - dropping zone available', 'Ball in creek left of bridge - dropping zone available', 'Ball in creek right of bridge - NO dropping zone, standard relief only', 'Dropping zone only for main pond area left/west side of footbridge']
                },
                {
                    'situation': 'Ball on bridge over penalty area',
                    'explanation': 'When ball comes to rest on one of the bridges on holes 16, 17, and 18 that crosses over the penalty area, player gets NO RELIEF from the bridge. The ball is considered to be above the penalty area in accordance with Rule 17.1(a), and the bridge is an integral object of the penalty area. Player must play the ball as it lies or proceed under penalty area relief options.',
                    'examples': ['Ball on bridge between 17th and 18th', 'Ball on bridge on 16', 'Ball on bridge on 17', 'Ball resting on bridge over water', 'Bridge over penalty area - no free relief', 'Must play from bridge or take penalty relief', 'No free relief from bridge']
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
            'keywords': ['penalty area', 'red penalty area', 'left side', 'holes 2 3 4', 'unmaintained area', 'fescue on 3', 'stakes', 'painted lines'],
            'examples': [
                'Ball rolls left into rough area on hole 2 - red penalty area relief available',
                'Ball in unmaintained area or fescue on left side of hole 3',
                'Ball in fescue area left of fairway on hole 4'
            ],
            'conditions': [
                {
                    'situation': 'Left side penalty area boundary',
                    'explanation': 'The entire left side of holes 2, 3, and 4 is designated as a red penalty area',
                    'examples': ['Left rough area on hole 2', 'Left side fescue on hole 3', 'fescue on 3', 'Left unmaintained area on hole 4']
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
            'text': 'Specific cart paths and roads are designated as integral objects from which free relief is not allowed. The unpaved road behind 12th green and sections of cart path behind the 17th green marked by green stakes are integral objects. Balls resting on or against these cart paths get NO RELIEF and must play it as it lies or take an unplayable ball penalty.',
            'keywords': ['cart path', 'integral object', 'no relief', 'unpaved road', 'green stakes', 'holes 12 17', 'cart path behind green', 'path behind green','path behind twelfth green', 'road behind twelvth green', 'path behind seventeenth green', 'path behind 12th green', 'road behind 12th green', 'path behind 17th green', 'path behind 12 green', 'road behind 12 green', 'path behind 17 green', 'cart path behind', 'no free relief','cart path integral', 'path integral object'],
            'examples': [
                'Ball on cart path behind 17th green - no free relief available',
                'Ball on road behind 12th green - no free relief available',
                'Ball on maintenance road elsewhere - free relief under Rule 16.1',
                'Ball on path marked with green stakes - must play as lies'
            ],
            'conditions': [
                {
                    'situation': 'No relief areas - certain paths are integral objects',
                    'explanation': 'No free relief is available from: unpaved road behind 12th green, cart path sections behind 14th green marked by green stakes, cart path sections behind 17th green marked by green stakes',
                    'examples': ['Unpaved road behind 12th green', 'path behind 12th green', 'Cart path behind 17th green with green stakes']
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
            'text': 'The fenced trees in the penalty area on hole 3 are Temporary Immovable Obstructions (TIO). Because they are designated as "TEMPORARY", free relief may be taken if the TIO interferes with the lie of the ball, stance, or swing, or if the TIO lies directly in the line of sight between the ball and hole. All other immovable obstructions on the course follow relief procedures under Official Rule 16.1',
            'keywords': ['fenced trees', 'temporary immovable obstruction', 'TIO', 'hole 3', 'penalty area', 'line of sight', 'free relief'],
            'examples': [
                'Ball in penalty area but fenced tree blocks swing - free relief available',
                'Any other PERMANENT immovable obstructions on the course - free relief if interference with lie of the ball, stance, or swing path only, no free relief from line of sight',
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
            'title': 'Purple Line',
            'text': 'The walls around the Purple Line are boundary objects from which free relief is not available. A ball coming to rest on or beyond the Purple Line construction area is out of bounds.',
            'keywords': ['purple line', 'the purple line', 'purple', 'construction fence', 'purple line fence', 'boundary fence', 'out of bounds', 'no relief', 'green fence', 'mesh', 'mesh fence', 'construction mesh', 'green mesh', 'behind green', 'behind 1st green', 'behind first green', 'behind 14th green', 'to the right of #2', 'construction area', 'fence behind green', 'temporary fence'],
            'examples': [
                'Ball lands in construction area - out of bounds, proceed under stroke and distance',
                'Ball against purple line fence - no free relief available, play as lies or unplayable',
                'Ball against tunnel angled support walls - immovable obstruction'
            ],
            'conditions': [
                {
                    'situation': 'Construction fence as boundary',
                    'explanation': 'The fence around the Purple Line construction area is considered a boundary fence from which free relief is not available',
                    'examples': ['Purple construction fence', 'Temporary boundary fencing', 'No obstruction relief available']
                },
                {
                    'situation': 'Out of bounds determination',
                    'explanation': 'A ball coming to rest in or beyond the Purple Line construction area is out of bounds, even if it comes to rest on another part of the course that is in bounds for other holes',
                    'examples': ['Ball in construction zone', 'Ball beyond purple line markers', 'Out of bounds even if on course']
                },
                {
                    'situation': 'Tunnels are out of bounds',
                    'explanation': 'A ball that enters the tunnels under the Purple Line at holes 1, 2, 14, 15 is out of bounds, unless it bounces back into play on the same side as it entered',
                    'examples': ['Ball in tunnel', 'Ball went into tunnel', 'Ball at rest in tunnel', 'Ball went through the tunnel']
                },
                                {
                    'situation': 'Angled support walls',
                    'explanation': 'The angled support walls at tunnel entrances are immovable obstructions',
                    'examples': ['Ball against support wall', 'tunnel support wall interfering with swing', 'angled tunnel wall intereferes with swing', 'free relief from angled support walls']
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
                'Ball near bird house post - free relief available under Rule 16.1 - free relief if interference with lie of ball, stance, or swing path. No free relief from line of sight',
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
                },
                {
                    'situation': 'Line of sight relief',
                    'explanation': 'When an immovable obstruction, like a bird house, intereferes with the players line of sight, no free relief is allowed',
                    'examples': ['Must play it as it lies', 'May take an unplayable ball with penalty']
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
        },

        {
            'id': 'CCC-14',
            'title': 'Preferred Lies (Lift, Clean, and Place)',
            'text': 'When the Committee has declared preferred lies in effect (Model Local Rule E-3), a ball lying in a part of the general area cut to fairway height or less may be lifted, cleaned, and placed without penalty. The player must mark the spot before lifting, and must place the ball within one club-length of the original spot, not nearer the hole, and in the general area. This applies to any ball at rest in an area cut to fairway height or less, including after a ball has been dropped under another Rule (such as penalty area relief into a dropping zone).',
            'keywords': ['preferred lies', 'lift clean place', 'winter rules', 'Model Local Rule E-3', 'clean ball', 'place ball', 'general area', 'fairway height', 'closely mown', 'dropping zone', 'mark ball', 'seasonal rule', 'wet conditions', 'mud ball'],
            'examples': [
                'Preferred lies in effect - may lift, clean, and place ball on fairway',
                'Ball dropped in dropping zone cut to fairway height - may then lift, clean, and place under preferred lies',
                'Ball in fairway with mud - lift, clean, and place within one club-length',
                'Ball in rough - preferred lies does NOT apply, rough is not cut to fairway height'
            ],
            'conditions': [
                {
                    'situation': 'When preferred lies applies',
                    'explanation': 'Preferred lies applies whenever the Committee has put the local rule in effect, typically during wet or winter conditions. It allows any ball at rest in a part of the general area cut to fairway height or less to be lifted, cleaned, and placed within one club-length, not nearer the hole, and must remain in the general area. It does NOT apply to balls in the rough or other areas not cut to fairway height.',
                    'examples': ['Ball on fairway during winter rules', 'Ball on fringe cut to fairway height', 'Ball on fairway-cut path between holes', 'Ball in rough - NOT eligible for preferred lies']
                },
                {
                    'situation': 'Procedure for preferred lies',
                    'explanation': 'Player must: (1) Mark the spot of the ball before lifting, (2) Lift and clean the ball, (3) Place the ball within one club-length of the original spot, not nearer the hole, in the general area. The ball must be placed, not dropped. If the placed ball does not stay at rest on the spot, follow Rule 14.2e.',
                    'examples': ['Mark with tee or coin before lifting', 'Clean mud off ball', 'Place within one club-length not nearer hole', 'Ball must stay at rest where placed']
                },
                {
                    'situation': 'Preferred lies after dropping in a dropping zone',
                    'explanation': 'After a player drops a ball in a dropping zone located in the general area that is cut to fairway height or less (such as after taking penalty area relief), the ball is now at rest in an eligible area. Since preferred lies applies to ANY ball at rest in the general area cut to fairway height or less, the player IS allowed to then invoke preferred lies to lift, clean, and place the ball. The penalty relief procedure and preferred lies are two independent rules that can both apply sequentially. If the dropping zone is in the rough or an area not cut to fairway height, preferred lies would NOT apply.',
                    'examples': ['Drop in dropping zone on fairway-cut area on hole 16, then lift clean and place - ALLOWED', 'Drop in dropping zone on hole 17 on closely mown area, then lift clean and place - ALLOWED', 'Dropping zone in rough area - preferred lies NOT available after drop', 'Penalty area relief drop on fairway followed by preferred lies - both apply']
                },
                {
                    'situation': 'Where preferred lies does NOT apply',
                    'explanation': 'Preferred lies only applies to areas of the general area cut to fairway height or less. It does NOT apply to: the rough, bunkers, penalty areas, putting greens (which already have lift/clean/replace under Rule 13.1b), or the teeing area. A ball sitting in the rough even a few inches from the fairway is not eligible.',
                    'examples': ['Ball in rough - no preferred lies', 'Ball in bunker - no preferred lies', 'Ball in penalty area - no preferred lies', 'Ball just off fairway in first cut of rough - no preferred lies', 'Ball on green - use Rule 13.1b instead']
                },
                {
                    'situation': 'Penalty for incorrect procedure',
                    'explanation': 'If a player places the ball in a wrong place or fails to mark before lifting, the player gets one penalty stroke under Rule 14.2. If the player drops instead of places, the ball is not in play and must be corrected.',
                    'examples': ['Forgetting to mark spot - one penalty stroke', 'Placing ball nearer the hole - wrong place penalty', 'Dropping instead of placing - must correct']
                }
            ]
        },

        {
            'id': 'CCC-15',
            'title': 'Bridges on the Course',
            'text': 'Rules for balls on or near bridges at Columbia Country Club.',
            'keywords': ['bridge', 'footbridge', 'cart bridge', 'ball on bridge', 'under bridge', 'bridge relief', 'support beam', 'bridge over creek', 'bridge over water', 'bridge over penalty area', 'hole 2', 'hole 3', 'hole 13', 'hole 14', 'hole 16', 'hole 17', 'hole 18'],
            'examples': [
                'Ball on bridge - no free relief on most holes',
                'Ball on bridge on hole 13 - may get free relief depending on position',
                'Ball under bridge against support beam - free relief',
                'Ball on footbridge on 17 - in penalty area'
            ],
            'conditions': [
                {
                    'situation': 'Bridges entirely over penalty areas (holes 2, 3, 14, 16, 17, 18)',
                    'explanation': 'The following bridges are entirely within penalty areas: both bridges on hole 2, both bridges on hole 3, the bridge on hole 14, the footbridge on hole 16, the footbridge on hole 17, and the cart bridge on hole 18. A ball on any of these bridges is treated as being in the penalty area under Rule 17.1a. No free relief is available from the bridge. The player must play the ball as it lies or take penalty area relief under Rule 17.1d for one penalty stroke.',
                    'examples': ['Ball on bridge on 2', 'Ball on bridge on 3', 'Ball on bridge on 14', 'Ball on footbridge on 16', 'Ball on footbridge on 17', 'Ball on cart bridge on 18']
                },
                {
                    'situation': 'Bridge on hole 13 - ball ON the bridge',
                    'explanation': 'The footbridge on hole 13 crosses a creek (penalty area) as well as a general area. Only the portion of the bridge directly over the penalty area is treated as being in the penalty area under Rule 17.1a. If your ball is on a part of the bridge NOT directly over the penalty area, the bridge is an immovable obstruction and you get free relief under Rule 16.1. Per USGA Clarification 16.1/4, the nearest point of complete relief is on the ground directly beneath where the ball lies on the bridge (vertical distance is disregarded). Drop within one club-length of that point, not nearer the hole. If your ball is on the portion directly over the creek, you must play it as it lies or take penalty area relief under Rule 17.1d for one penalty stroke.',
                    'examples': ['Ball on bridge on 13', 'Ball on bridge over creek on hole 13', 'Relief from bridge on 13th', 'Free drop from 13 bridge']
                },
                {
                    'situation': 'Ball UNDER any bridge or near support structures',
                    'explanation': 'If your ball is on the ground under or near any bridge and the bridge or its supporting structures (beams, columns, railings) interfere with your stance or swing, the bridge is an immovable obstruction and you are entitled to free relief under Rule 16.1. Find the nearest point of complete relief not nearer the hole and drop within one club-length. This applies on any hole because the ball is on the ground, not above the penalty area.',
                    'examples': ['Ball under bridge against support beam', 'Bridge column in swing path', 'Ball under bridge on 13 near beam', 'Support beam interfering with stance', 'Ball against bridge support on 17']
                },
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
        'fenced_trees': ['CCC-5'],
        'preferred_lies': ['CCC-14'],
        'lift_clean_and_place': ['CCC-14'],
        'bridge': ['CCC-15']
    },
    
    'hole_specific_rules': {
        '2': ['CCC-3', 'CCC-15']
        '3': ['CCC-3', 'CCC-5', 'CCC-15'],
        '4': ['CCC-3'],
        '6': ['CCC-9'],
        '9': ['CCC-7', 'CCC-8'],
        '10': ['CCC-7', 'CCC-8'],
        '12': ['CCC-4'],
        '13': ['CCC-9'],
        '14': ['CCC-4', 'CCC-15'],
        '15': ['CCC-2', 'CCC-4'],
        '16': ['CCC-2', 'CCC-14', 'CCC-15'],
        '17': ['CCC-2', 'CCC-4', 'CCC-14', 'CCC-15'],
        '18': ['CCC-2', 'CCC-9', 'CCC-15']
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
