import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from resources.datatables import FactionStatus
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('rebel_crewman')
	mobileTemplate.setLevel(22)
	mobileTemplate.setDifficulty(Difficulty.NORMAL)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setSocialGroup("rebel")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(FactionStatus.Combatant)
	
	
	templates = Vector()
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_female_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_female_02.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_01.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_02.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_03.iff')
	templates.add('object/mobile/shared_dressed_rebel_crewman_human_male_04.iff')				
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/ranged/carbine/shared_carbine_e5.iff', WeaponType.CARBINE, 1.0, 15, 'energy')
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('rangedShot')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('rebel_crewman', mobileTemplate)
	return