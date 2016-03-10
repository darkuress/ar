armSet = [('shoulder', [5,10,2]), ('elbow', [8,10,0]), ('wrist', [11, 10, 2])]
handSet = ['palm']
fingerSet = ['thumb', 'index', 'middle', 'ring', 'pinky']

spineJoints = ['Root', 'Spine1', 'Spine2', 'Spine3', 'Spine4', 'NeckBase', 'Head', 'Jaw', 'JawAim']
legJoints = ['Root', 'Pelvis', 'L_Hip', 'L_Knee', 'L_Ankle', 'L_Ball', 'L_Toe']
legJointsR = ['R_Hip', 'R_Knee', 'R_Ankle', 'R_Ball', 'R_Toe']
armJoints = ['Spine4', 'L_Scapula', 'L_Shoulder', 'L_Elbow', 'L_Wrist']
armJointsR = ['Spine4','R_Scapula', 'R_Shoulder', 'R_Elbow', 'R_Wrist']
handJoints = ['Palm']
fingerJoints = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
tailJoints = ['Tail0', 'Tail1', 'Tail2', 'Tail3' 'Tail4', 'Tail5' 'Tail6']

#locator info, {'name' : 'translate', 'scale', 'lock attr info'}
placeLocs = { #Root Spine
              'Root_Adjust_CTRL'        : [[0, 12, 0],    1,   'tx'],
              'Spine1_Adjust_CTRL'      : [[0, 13, -0.5], 0.7, 'tx'],
              'Spine2_Adjust_CTRL'      : [[0, 15, -0.7], 0.7, 'tx'],
              'Spine3_Adjust_CTRL'      : [[0, 17, -0.7], 0.7, 'tx'],
              'Spine4_Adjust_CTRL'      : [[0, 19, -0.3], 0.7, 'tx'],
              #Neck, Head, Jaw
              'NeckBase_Adjust_CTRL'    : [[0, 21, -0.4], 0.7, 'tx'],
              'Head_Adjust_CTRL'        : [[0, 22, 0]   , 0.7, 'tx'],
              'Jaw_Adjust_CTRL'         : [[0, 22, 2]   , 0.7, 'tx'],
              'JawAim_Adjust_CTRL'      : [[0, 21, 3]   , 0.7, 'tx'],
              #Legs
              'Pelvis_Adjust_CTRL'      : [[0, 12, 0]   , 1,   'tx'],
              'L_Hip_Adjust_CTRL'         : [[2, 12, -1]  , 1,   'tx'],
              'L_Knee_Adjust_CTRL'      : [[2, 7, -0.2] , 1,   ''  ],
              'L_Ankle_Adjust_CTRL'     : [[2, 2, -0.3] , 1,   ''  ],
              'L_Ball_Adjust_CTRL'      : [[2, 0, 2]    , 1,   ''  ],
              'L_Toe_Adjust_CTRL'       : [[2, 0, 3]    , 1,   ''  ],
              'L_Heel_PivotPosition'    : [[2, 0, -1]   , 0.7, ''  ],
              'L_SideIn_PivotPosition'  : [[1.5, 0, 0]  , 0.7, ''  ],
              'L_SideOut_PivotPosition' : [[2.5, 0, 0]  , 0.7, ''  ],
              #Arms
              'L_Scapula_Adjust_CTRL'   : [[2, 18, -1]  , 1,   ''  ],
              'L_Shoulder_Adjust_CTRL'  : [[3, 20, -0.3], 1,   ''  ],
              'L_Elbow_Adjust_CTRL'     : [[6, 20, -1.5], 1,   ''  ],
              'L_Wrist_Adjust_CTRL'     : [[9, 20, -0.3], 1,   ''  ],
              #palm
              #'L_Palm_Adjust_CTRL'     : [[9.7, 20, -0.3],1,   ''  ]
            }


