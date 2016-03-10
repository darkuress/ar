import maya.cmds as cmds
def armAlignPatch():
	L_o_R = ['L_', 'R_']
	for LR in L_o_R:
		###making locators
		tempLoc = cmds.xform('%sShoulder' %LR, q = True, t = True, ws = True)
		print tempLoc
		cmds.createNode('transform', n = '%sArmalign_Loc_GRP' %LR)
		cmds.spaceLocator(n = '%sArmalign_Loc' %LR)
		cmds.select('%sArmalign_Loc_GRP' %LR, tgl = True)
		cmds.parent()
		cmds.move(tempLoc[0], tempLoc[1], tempLoc[2])
		cmds.select('%sScapula_CTRL' %LR, r = True)
		cmds.select('%sArmalign_Loc_GRP' %LR, tgl = True)
		cmds.parentConstraint(mo = True, weight = 1)
		
		#####unparent shoulder joint and parent constrain from scapula
		cmds.createNode('transform', n = '%sShoulder_GRP' %LR)
		cmds.move(tempLoc[0], tempLoc[1], tempLoc[2])
		cmds.select('%sShoulder' %LR, r = True)
		cmds.select('%sShoulder_GRP' %LR, tgl = True)
		cmds.parent()
		cmds.select('%sScapula' %LR, r = True)
		cmds.select('%sShoulder_GRP' %LR, tgl = True)
		cmds.parentConstraint(mo = True, weight = 1)
		
		####Constrains
		cmds.select('%sShoulder_FK_CTRL_GRP' %LR, r = True)
		cmds.parent(w= True)
		cmds.select('%sArmalign_Loc' %LR, r = True)
		cmds.select('%sShoulder_FK_CTRL_GRP' %LR, tgl = True)
		cmds.pointConstraint(mo = True, weight = 1)
		cmds.orientConstraint(mo = True, weight = 1)
		
		######add attr
		cmds.addAttr('%sShoulder_FK_CTRL' %LR, ln = 'WorldAlign', at = 'long', min = 0, max = 1)
		cmds.setAttr('%sShoulder_FK_CTRL.WorldAlign' %LR, 1, e = True, keyable = True)
		cmds.connectAttr('%sShoulder_FK_CTRL.WorldAlign' %LR, '%sShoulder_FK_CTRL_GRP_orientConstraint1.%sArmalign_LocW0' %(LR,LR))
	cmds.createNode('transform', n = 'Shoulder_GRP')
	cmds.select('L_Armalign_Loc_GRP', r = True)
	cmds.select('R_Armalign_Loc_GRP', tgl = True)
	cmds.select('L_Shoulder_GRP', tgl = True)
	cmds.select('R_Shoulder_GRP', tgl = True)
	cmds.select('L_Shoulder_FK_CTRL_GRP', tgl = True)
	cmds.select('R_Shoulder_FK_CTRL_GRP', tgl = True)
	cmds.select('Shoulder_GRP', tgl = True)
	cmds.parent()
	cmds.select('Shoulder_GRP', r = True)
	cmds.select('Puck', tgl = True)
	cmds.parent()
