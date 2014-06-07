import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector


def addTemplate(core):
	mobileTemplate = MobileTemplate()	
	mobileTemplate.setCreatureName('piket_plains_walker')
	mobileTemplate.setLevel(61)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)

	mobileTemplate.setMinSpawnDistance(5)
	mobileTemplate.setMaxSpawnDistance(10)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Herbivore Meat")
	mobileTemplate.setMeatAmount(35)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setBoneAmount(25)	
	mobileTemplate.setBoneType("Avian Bone")
	mobileTemplate.setHideAmount(30)
	mobileTemplate.setSocialGroup("piket")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(False)	

	templates = Vector()
	templates.add('object/mobile/shared_piket_plains_walker.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', WeaponType.UNARMED, 1.0, 6, 'kinetic')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('piket_plains_walker', mobileTemplate)
	return