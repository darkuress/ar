import maya.cmds as cmds
#color blue : 6
#      red  : 12
#      yellow : 17

def colorPatch():
	centerCnt = ['Head_CTRL', 'NeckBase_CTRL', 'Jaw_CTRL', 'Spine3_CTRL', 'Spine2_CTRL', 'Spine1_CTRL', 'Pelvis_CTRL']
	left = ['L_FK_Knee_CTRL', 'L_FK_Hip_CTRL', 'L_FK_Ankle_CTRL', 'L_FK_Ball_CTRL', 'L_Scapula_CTRL', 'L_Shoulder_FK_CTRL', 'L_Elbow_FK_CTRL', 'L_Wrist_FK_CTRL', 'L_PalmFinger_CTRL', 'L_Arm_Extra_CTRL', 'L_Leg_Extra_CTRL', 'L_Leg_CTRL', 'L_Polevector', 'L_Arm_Polevector', 'L_Arm_IK_CTRL']
	right = ['R_FK_Knee_CTRL', 'R_FK_Hip_CTRL', 'R_FK_Ankle_CTRL', 'R_FK_Ball_CTRL', 'R_Scapula_CTRL', 'R_Shoulder_FK_CTRL', 'R_Elbow_FK_CTRL', 'R_Wrist_FK_CTRL', 'R_PalmFinger_CTRL', 'R_Arm_Extra_CTRL', 'R_Leg_Extra_CTRL', 'R_Leg_CTRL', 'R_Polevector', 'R_Arm_Polevector', 'R_Arm_IK_CTRL']
	root = ['Root_CTRL']

	for c in centerCnt:
		shapeNode = cmds.listRelatives(c)[0]
		cmds.setAttr(shapeNode + '.overrideEnabled', 1)
		cmds.setAttr(shapeNode + '.overrideColor', 17)
	for l in left:
		shapeNode = cmds.listRelatives(l)[0]
		cmds.setAttr(shapeNode + '.overrideEnabled', 1)
		cmds.setAttr(shapeNode + '.overrideColor', 6)
	for r in right:
		shapeNode = cmds.listRelatives(r)[0]
		cmds.setAttr(shapeNode + '.overrideEnabled', 1)
		cmds.setAttr(shapeNode + '.overrideColor', 12)
	for r in root:
		shapeNode = cmds.listRelatives(r)[0]
		cmds.setAttr(shapeNode + '.overrideEnabled', 1)
		cmds.setAttr(shapeNode + '.overrideColor', 9)   