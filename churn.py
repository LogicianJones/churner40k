from random import randint #for randRecursiveWalk

listSkills = {
  "common lore":["Adeptus Arbites", "Adeptus Astra Telepathica", "Adeptus Mechanicus", "Administratum", "Ecclesiarchy", "Imperial Creed", "Imperial Guard", "Imperial Navy", "Imperium", "Jericho Reach", "Koronus Expanse", "Screaming Vortex", "Tech", "War"],
  "forbidden lore":["Adeptus Mechanicus", "Adeptus Astartes", "Codex Astartes", "Archeotech", "Daemonology", "Heresy", "The Horus Heresy and Long War", "The Inquisition", "Mutants", "Navigators", "Pirates", "Psykers", "The Warp", "Xenos"],
  "linguistics":["High Gothic", "Low Gothic"],
  "scholastic lore":["Astromancy", "Beasts", "Bureaucracy", "Chymistry", "Cryptology", "Heraldry", "Imperial Warrants", "Imperial Creed", "Judgement", "Legend", "Navis Nobilite", "Numerology", "Occulty", "Philosophy", "Tactica Imperialis"],
  "trade":["Archaeologist", "Armourer", "Astrographer", "Chymist", "Cryptographer", "Explorator", "Linguist", "Remembrancer", "Scrimshawer"],
}

class node():
  def __init__(self):
    self.name = ""
    self.changes = []
    self.next = []
  def __init__(self, name):
    self.name = name
    self.changes = []
    self.next = []
  #need to add check for duplicates
  def insertSelect(options, string):
    for entry in options:
      node = node(string + entry)
      for nextNode in next:
        node.next.append(nextNode)
      self.next.append(node)
  def addLinearChoiceLayer(choices):
    if len(self.next) == 0:
      for choice in choices:
        self.next.append(choice)
    else:
      for nextNode in self.next:
        nextNode.addLinearChoiceLayer(choices)

class sheet():
  def __init__(self):

    self.cname = ""
    self.pname = ""
    self.archetype = ""
    self.rank = ""
    self.warband = ""
    self.pride = ""
    self.disgrace = ""
    self.motivation = ""
    self.description = ""

    self.characteristics = {
      "ws":0,
      "bs":0,
      "s":0,
      "t":0,
      "ag":0,
      "int":0,
      "per":0,
      "wp":0,
      "fel":0,
      "inf":0
    }

    self.skills = {
      "acrobatics":("ag", 0),
      "atheltics":("s", 0),
      "awareness":("per", 0),
      "charm":("fel", 0),
      "command":("fel", 0),
      "commerce":("int", 0),
      #commonlore, int, list skill
      "deceive":("fel", 0),
      "dodge":("ag", 0),
      #forbiddenlore, int, list skill
      "inquiry":("fel", 0),
      "intimidate":("wp", 0),
      #linguistics, int, list skill
      "logic":("int", 0),
      "medicae":("int", 0),
      "navigation (surface)":("int", 0),
      "navigation (stellar)":("int", 0),
      "navigation (warp)":("int", 0),
      "operate (aeronautica)":("ag", 0),
      "operate (surface)":("ag", 0),
      "operate (voidship)":("ag", 0),
      "parry":("ws", 0),
      "psyniscience":("per", 0),
      #scholastic lore, int, list skill
      "scrutiny":("per", 0),
      "security":("int", 0),
      "sleight of hand":("ag", 0),
      "stealth":("ag", 0),
      "tech-use":("int", 0),
      "tracking":("int", 0),
      #trade, int, list skill
    }

    self.listSkills = {
      "common lore":("int", []),
      "forbidden lore":("int", []),
      "linguistics":("int", []),
      "scholastic lore":("int", []),
      "trade":("int", []),
    }

    self.talents = []
    self.traits = []
    self.abilities = []
    self.powers = []
    self.gear = []

    self.wounds = 0
    self.corruption = 0
    self.mutations = []

    self.xpTotal = 0
    self.xpSpent = 0
    self.advancements = []

    self.alignments = {
      "khorne":0,
      "slaanesh":0,
      "nurgle":0,
      "tzeentch":0,
      "unaligned":0,
    }
    self.currentAlignment = "unaligned"

def initializeTest2():
  #human or spacemarine
  start = node("start")

  #bolter or boltpistol
  spaceMarine = node("spaceMarine")

  #champion, chosen, forsaken, or sorcerer
  spaceMarine_legionBolter = node("spaceMarine_legionBolter")
  spaceMarine_legionBoltPistol = node("spaceMarine_legionBoltPistol")
  list1 = [spaceMarine_legionBolter, spaceMarine_legionBoltPistol]
  spaceMarine.addLinearChoiceLayer(*list1)

  human = node("human")
  start.next.extend([spaceMarine, human])
  
  return start

def initializeTest():
  #human or spacemarine
  start = node("start")

  #bolter of bolt pistol
  spaceMarine = node("spaceMarine")
  
  #champion or chosen or forsaken or sorcerer
  spaceMarine_legionBolter = node("spaceMarine_legionBolter")
  spaceMarine_legionBoltPistol = node("spaceMarine_legionBoltPistol")

  #charm or deceive
  champion = node("champion")

  #intimidate or scrutiny  
  champion_charm = node("champion_charm")
  champion_deceive = node("champion_deceive")

  #airOfAuthority or disturbingVoice
  champion_intimidate = node("champion_intimidate")
  champion_scrutiny = node("champion_scrutiny")

  #lessMinion or sureStrike
  champion_airOfAuthority = node("champion_airOfAuthority")
  champion_disturbingVoice = node("champion_disturbingVoice")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  champion_lesserMinion = node("champion_lesserMinion")
  champion_sureStrike = node("champion_sureStrike")

  champion_airOfAuthority.next.append(champion_lesserMinion)
  champion_airOfAuthority.next.append(champion_sureStrike)
  champion_disturbingVoice.next.append(champion_lesserMinion)
  champion_disturbingVoice.next.append(champion_sureStrike)

  champion_intimidate.next.append(champion_airOfAuthority)
  champion_intimidate.next.append(champion_disturbingVoice)
  champion_scrutiny.next.append(champion_airOfAuthority)
  champion_scrutiny.next.append(champion_disturbingVoice)

  champion_charm.next.append(champion_intimidate)
  champion_charm.next.append(champion_scrutiny)
  champion_deceive.next.append(champion_intimidate)
  champion_deceive.next.append(champion_scrutiny)

  champion.next.append(champion_charm)
  champion.next.append(champion_deceive)

  #dodge10 or parry10
  chosen = node("chosen")

  #quickDraw or rapidReload
  chosen_dodge10 = node("chosen_dodge10")
  chosen_parry10 = node("chosen_parry10")

  #disarm or doubleTeam
  chosen_quickDraw = node("chosen_quickDraw")
  chosen_rapidReload = node("chosen_rapidReload")

  #sureStrike or deadeyeShot
  chosen_disarm = node("chosen_disarm")
  chosen_doubleTeam = node("chosen_doubleTeam")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  chosen_sureStrike = node("chosen_sureStrike")
  chosen_deadeyeShot = node("chosen_deadeyeShot")

  chosen_disarm.next.append(chosen_sureStrike)
  chosen_disarm.next.append(chosen_doubleTeam)
  chosen_doubleTeam.next.append(chosen_sureStrike)
  chosen_doubleTeam.next.append(chosen_doubleTeam)

  chosen_quickDraw.next.append(chosen_disarm)
  chosen_quickDraw.next.append(chosen_doubleTeam)
  chosen_rapidReload.next.append(chosen_disarm)
  chosen_rapidReload.next.append(chosen_doubleTeam)

  chosen_dodge10.next.append(chosen_quickDraw)
  chosen_dodge10.next.append(chosen_rapidReload)
  chosen_parry10.next.append(chosen_quickDraw)
  chosen_parry10.next.append(chosen_rapidReload)

  chosen.next.append(chosen_dodge10)
  chosen.next.append(chosen_parry10)

  #commerce or scrutiny
  forsaken = node("forsaken")

  #commonLore or survival10
  forsaken_commerce = node("forsaken_commerce")
  forsaken_scrutiny = node("forsaken_scrutiny")

  #lightSleeper or blindFighting
  forsaken_commonLore = node("forsaken_commonLore")
  forsaken_survival10 = node("forsaken_survival10")

  #coldHearted or soundConstitution
  forsaken_lightSleeper = node("forsaken_lightSleeper")
  forsaken_blindFighting = node("forsaken_blindFighting")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  forsaken_coldHearted = node("forsaken_coldHearted")
  forsaken_soundConstitution = node("forsaken_soundConstitution")

  forsaken_lightSleeper.next.append(forsaken_coldHearted)
  forsaken_lightSleeper.next.append(forsaken_soundConstitution)
  forsaken_blindFighting.next.append(forsaken_coldHearted)
  forsaken_blindFighting.next.append(forsaken_soundConstitution)

  forsaken_commonLore.next.append(forsaken_lightSleeper)
  forsaken_commonLore.next.append(forsaken_blindFighting)
  forsaken_survival10.next.append(forsaken_lightSleeper)
  forsaken_survival10.next.append(forsaken_blindFighting)

  forsaken_commerce.next.append(forsaken_commonLore)
  forsaken_commerce.next.append(forsaken_survival10)
  forsaken_scrutiny.next.append(forsaken_commonLore)
  forsaken_scrutiny.next.append(forsaken_survival10)

  forsaken.next.append(forsaken_commerce)
  forsaken.next.append(forsaken_scrutiny)

  #deception or scrutiny
  sorcerer = node("sorcerer")

  #forbiddenLoreDaemons or forbiddenLorePsykers
  sorcerer_deception = node("sorcerer_deception")
  sorcerer_scrutiny = node("sorcerer_scrutiny")

  #meditation or mimic
  sorcerer_forbiddenLoreDaemons = node("sorcerer_forbiddenLoreDaemons")
  sorcerer_forbiddenLorePsykers = node("sorcerer_forbiddenLorePsykers")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  sorcerer_meditation = node("sorcerer_meditation")
  sorcerer_mimic = node("sorcerer_mimic")

  sorcerer_forbiddenLoreDaemons.next.append(sorcerer_meditation)
  sorcerer_forbiddenLoreDaemons.next.append(sorcerer_mimic)
  sorcerer_forbiddenLorePsykers.next.append(sorcerer_meditation)
  sorcerer_forbiddenLorePsykers.next.append(sorcerer_mimic)

  sorcerer_deception.next.append(sorcerer_forbiddenLoreDaemons)
  sorcerer_deception.next.append(sorcerer_forbiddenLorePsykers)
  sorcerer_scrutiny.next.append(sorcerer_forbiddenLoreDaemons)
  sorcerer_scrutiny.next.append(sorcerer_forbiddenLorePsykers)

  sorcerer.next.append(sorcerer_deception)
  sorcerer.next.append(sorcerer_scrutiny)

  spaceMarine_legionBolter.next.append(champion)
  spaceMarine_legionBolter.next.append(chosen)
  spaceMarine_legionBolter.next.append(forsaken)
  spaceMarine_legionBolter.next.append(sorcerer)
  spaceMarine_legionBoltPistol.next.append(champion)
  spaceMarine_legionBoltPistol.next.append(chosen)
  spaceMarine_legionBoltPistol.next.append(forsaken)
  spaceMarine_legionBoltPistol.next.append(sorcerer)

  spaceMarine.next.append(spaceMarine_legionBolter)
  spaceMarine.next.append(spaceMarine_legionBoltPistol)

  #apostate or heretek or renegade or psyker
  human = node("human")

  #dodge or parry
  apostate = node("apostate")
  
  #intimidate or commerce
  apostate_dodge = node("apostate_dodge")
  apostate_parry = node("apostate_parry")

  #charm10 or deceive10
  apostate_intimidate = node("apostate_intimidate")
  apostate_commerce = node("apostate_commerce")

  #command10 or inquiry10
  apostate_charm10 = node("apostate_charm10")
  apostate_deceive10 = node("apostate_deceive10")

  #security or stealth or logic
  apostate_command10 = node("apostate_command10")
  apostate_inquiry10 = node("apostate_inquiry10")

  #disturbingVoice or radiantPresence
  apostate_security = node("apostate_security")
  apostate_stealth = node("apostate_stealth")
  apostate_logic = node("apostate_logic")

  #polyglot or mimic
  apostate_disturbingVoice = node("apostate_disturbingVoice")
  apostate_radiantPresence = node("apostate_radiantPresence")

  #inspireWrath or ironDiscipline or lesserMinion
  apostate_polyglot = node("apostate_polyglot")
  apostate_mimic = node("apostate_mimic")

  #bestCraftSword or commonCraftPowerBlade
  apostate_inspireWrath = node("apostate_inspireWrath")
  apostate_ironDiscipline = node("apostate_ironDiscipline")
  apostate_lesserMinion = node("apostate_lesserMinion")

  #flackArmor or meshArmor
  apostate_bestCraftSword = node("apostate_bestCraftSword")
  apostate_commonCraftPowerBlade = node("apostate_commonCraftPowerBlade")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  apostate_flackArmor = node("apostate_flackArmor")
  apostate_meshArmor = node("apostate_meshArmor")

  apostate_bestCraftSword.next.append(apostate_flackArmor)
  apostate_bestCraftSword.next.append(apostate_meshArmor)
  apostate_commonCraftPowerBlade.next.append(apostate_flackArmor)
  apostate_commonCraftPowerBlade.next.append(apostate_meshArmor)

  apostate_inspireWrath.next.append(apostate_bestCraftSword)
  apostate_inspireWrath.next.append(apostate_commonCraftPowerBlade)
  apostate_ironDiscipline.next.append(apostate_bestCraftSword)
  apostate_ironDiscipline.next.append(apostate_commonCraftPowerBlade)
  apostate_lesserMinion.next.append(apostate_bestCraftSword)
  apostate_lesserMinion.next.append(apostate_commonCraftPowerBlade)

  apostate_polyglot.next.append(apostate_inspireWrath)
  apostate_polyglot.next.append(apostate_ironDiscipline)
  apostate_polyglot.next.append(apostate_lesserMinion)
  apostate_mimic.next.append(apostate_inspireWrath)
  apostate_mimic.next.append(apostate_ironDiscipline)
  apostate_mimic.next.append(apostate_lesserMinion)

  apostate_disturbingVoice.next.append(apostate_polyglot)
  apostate_disturbingVoice.next.append(apostate_mimic)
  apostate_radiantPresence.next.append(apostate_polyglot)
  apostate_radiantPresence.next.append(apostate_mimic)

  apostate_security.next.append(apostate_disturbingVoice)
  apostate_security.next.append(apostate_radiantPresence)
  apostate_stealth.next.append(apostate_disturbingVoice)
  apostate_stealth.next.append(apostate_radiantPresence)
  apostate_logic.next.append(apostate_disturbingVoice)
  apostate_logic.next.append(apostate_radiantPresence)

  apostate_command10.next.append(apostate_security)
  apostate_command10.next.append(apostate_stealth)
  apostate_command10.next.append(apostate_logic)
  apostate_inquiry10.next.append(apostate_security)
  apostate_inquiry10.next.append(apostate_stealth)
  apostate_inquiry10.next.append(apostate_logic)

  apostate_charm10.next.append(apostate_command10)
  apostate_charm10.next.append(apostate_inquiry10)
  apostate_deceive10.next.append(apostate_command10)
  apostate_deceive10.next.append(apostate_inquiry10)

  apostate_intimidate.next.append(apostate_charm10)
  apostate_intimidate.next.append(apostate_deceive10)
  apostate_commerce.next.append(apostate_charm10)
  apostate_commerce.next.append(apostate_deceive10)

  apostate_dodge.next.append(apostate_intimidate)
  apostate_dodge.next.append(apostate_commerce)
  apostate_parry.next.append(apostate_intimidate)
  apostate_parry.next.append(apostate_commerce)

  apostate.next.append(apostate_dodge)
  apostate.next.append(apostate_parry)

  #dodge or parry
  heretek = node("heretek")

  #security or techUse10
  heretek_dodge = node("heretek_dodge")
  heretek_parry = node("heretek_parry")

  #forbiddenLoreArcheotech or forbiddenLoreXenos or forbiddenLoreWarp
  heretek_security = node("heretek_security")
  heretek_techUse10 = node("heretek_techUse10")

  #scholasticLoreAstromancy or scholasticLoreChymistry
  heretek_forbiddenLoreArcheotech = node("heretek_forbiddenLoreArcheotech")
  heretek_forbiddenLoreXenos = node("heretek_forbiddenLoreXenos")
  heretek_forbiddenLoreWarp = node("heretek_forbiddenLoreWarp")

  #weaponTrainingBolt or weaponTrainingPlasma or weaponTrainingPower
  heretek_scholasticLoreAstromancy = node("heretek_scholasticLoreAstromancy")
  heretek_scholasticLoreChymistry = node("heretek_scholasticLoreChymistry")

  #mechadendriteTrainingWeapon or mechadendriteTrainingUtility
  heretek_weaponTrainingBolt = node("heretek_weaponTrainingBolt")
  heretek_weaponTrainingPlasma = node("heretek_weaponTrainingPlasma")
  heretek_weaponTrainingPower = node("heretek_weaponTrainingPower")

  #meditation or totalRecall
  heretek_mechadendriteTrainingWeapon = node("heretek_mechadendriteTrainingWeapon")
  heretek_mechadendriteTrainingUtility = node("heretek_mechadendriteTrainingUtility")

  #armorMonger or weaponTech
  heretek_meditation = node("heretek_meditation")
  heretek_totalRecall = node("heretek_totalRecall")

  #lesserMinionHeretek or coldHearted
  heretek_armorMonger = node("heretek_armorMonger")
  heretek_weaponTech = node("heretek_weaponTech")

  #commonCraftPowerAxe or goodCraftGreatAxe
  heretek_lesserMinionHeretek = node("heretek_lesserMinionHeretek")
  heretek_coldHearted = node("heretek_coldHearted")

  #opticalMechadendrite or utilityMechadendrite or ballisticMechadendrite
  heretek_commonCraftPowerAxe = node("heretek_commonCraftPowerAxe")
  heretek_goodCraftGreatAxe = node("heretek_goodCraftGreatAxe")

  #lumeninCapacitors or maglevCoils or ferricLureImplants
  heretek_opticalMechadendrite = node("heretek_opticalMechadendrite")
  heretek_utilityMechadendrite = node("heretek_utilityMechadendrite")
  heretek_ballisticMechadendrite = node("heretek_ballisticMechadendrite")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  heretek_lumeninCapacitors = node("heretek_lumeninCapacitors")
  heretek_maglevCoils = node("heretek_maglevCoils")
  heretek_ferricLureImplants = node("heretek_ferricLureImplants")

  heretek_opticalMechadendrite.next.append(heretek_lumeninCapacitors)
  heretek_opticalMechadendrite.next.append(heretek_maglevCoils)
  heretek_opticalMechadendrite.next.append(heretek_ferricLureImplants)
  heretek_utilityMechadendrite.next.append(heretek_lumeninCapacitors)
  heretek_utilityMechadendrite.next.append(heretek_maglevCoils)
  heretek_utilityMechadendrite.next.append(heretek_ferricLureImplants)
  heretek_ballisticMechadendrite.next.append(heretek_lumeninCapacitors)
  heretek_ballisticMechadendrite.next.append(heretek_maglevCoils)
  heretek_ballisticMechadendrite.next.append(heretek_ferricLureImplants)
  
  heretek_commonCraftPowerAxe.next.append(heretek_opticalMechadendrite)
  heretek_commonCraftPowerAxe.next.append(heretek_utilityMechadendrite)
  heretek_commonCraftPowerAxe.next.append(heretek_ballisticMechadendrite)
  heretek_goodCraftGreatAxe.next.append(heretek_opticalMechadendrite)
  heretek_goodCraftGreatAxe.next.append(heretek_utilityMechadendrite)
  heretek_goodCraftGreatAxe.next.append(heretek_ballisticMechadendrite)

  heretek_lesserMinionHeretek.next.append(heretek_commonCraftPowerAxe)
  heretek_lesserMinionHeretek.next.append(heretek_goodCraftGreatAxe)
  heretek_coldHearted.next.append(heretek_commonCraftPowerAxe)
  heretek_coldHearted.next.append(heretek_goodCraftGreatAxe)

  heretek_armorMonger.next.append(heretek_lesserMinionHeretek)
  heretek_armorMonger.next.append(heretek_coldHearted)
  heretek_weaponTech.next.append(heretek_lesserMinionHeretek)
  heretek_weaponTech.next.append(heretek_coldHearted)

  heretek_meditation.next.append(heretek_armorMonger)
  heretek_meditation.next.append(heretek_weaponTech)
  heretek_totalRecall.next.append(heretek_armorMonger)
  heretek_totalRecall.next.append(heretek_weaponTech)

  heretek_mechadendriteTrainingWeapon.next.append(heretek_meditation)
  heretek_mechadendriteTrainingWeapon.next.append(heretek_totalRecall)
  heretek_mechadendriteTrainingUtility.next.append(heretek_meditation)
  heretek_mechadendriteTrainingUtility.next.append(heretek_totalRecall)

  heretek_weaponTrainingBolt.next.append(heretek_mechadendriteTrainingWeapon)
  heretek_weaponTrainingBolt.next.append(heretek_mechadendriteTrainingUtility)
  heretek_weaponTrainingPlasma.next.append(heretek_mechadendriteTrainingWeapon)
  heretek_weaponTrainingPlasma.next.append(heretek_mechadendriteTrainingUtility)
  heretek_weaponTrainingPower.next.append(heretek_mechadendriteTrainingWeapon)
  heretek_weaponTrainingPower.next.append(heretek_mechadendriteTrainingUtility)

  heretek_scholasticLoreAstromancy.next.append(heretek_weaponTrainingBolt)
  heretek_scholasticLoreAstromancy.next.append(heretek_weaponTrainingPlasma)
  heretek_scholasticLoreAstromancy.next.append(heretek_weaponTrainingPower)
  heretek_scholasticLoreChymistry.next.append(heretek_weaponTrainingBolt)
  heretek_scholasticLoreChymistry.next.append(heretek_weaponTrainingPlasma)
  heretek_scholasticLoreChymistry.next.append(heretek_weaponTrainingPower)

  heretek_forbiddenLoreArcheotech.next.append(heretek_scholasticLoreAstromancy)
  heretek_forbiddenLoreArcheotech.next.append(heretek_scholasticLoreChymistry)
  heretek_forbiddenLoreXenos.next.append(heretek_scholasticLoreAstromancy)
  heretek_forbiddenLoreXenos.next.append(heretek_scholasticLoreChymistry)
  heretek_forbiddenLoreWarp.next.append(heretek_scholasticLoreAstromancy)
  heretek_forbiddenLoreWarp.next.append(heretek_scholasticLoreChymistry)

  heretek_security.next.append(heretek_forbiddenLoreArcheotech)
  heretek_security.next.append(heretek_forbiddenLoreXenos)
  heretek_security.next.append(heretek_forbiddenLoreWarp)
  heretek_techUse10.next.append(heretek_forbiddenLoreArcheotech)
  heretek_techUse10.next.append(heretek_forbiddenLoreXenos)
  heretek_techUse10.next.append(heretek_forbiddenLoreWarp)

  heretek_dodge.next.append(heretek_security)
  heretek_dodge.next.append(heretek_techUse10)
  heretek_parry.next.append(heretek_security)
  heretek_parry.next.append(heretek_techUse10)

  heretek.next.append(heretek_dodge)
  heretek.next.append(heretek_parry)

  #command or intimidate
  renegade = node("renegade")

  #dodge10 or parry10  
  renegade_command = node("renegade_command")
  renegade_intimidate = node("renegade_intimidate")

  #survival or stealth
  renegade_dodge10 = node("renegade_dodge10")
  renegade_parry10 = node("renegade_parry10")

  #techUse or medicae
  renegade_survival = node("renegade_survival")
  renegade_stealth = node("renegade_stealth")

  #weaponTrainingBolt or weaponTrainingShock
  renegade_techUse = node("renegade_techUse")
  renegade_medicae = node("renegade_medicae")

  #catfall or combatSenses
  renegade_weaponTrainingBolt = node("renegade_weaponTrainingBolt")
  renegade_weaponTrainingShock = node("renegade_weaponTrainingShock")

  #sureStrike or disarm or takedown
  renegade_catfall = node("renegade_catfall")
  renegade_combatSenses = node("renegade_combatSenses")

  #ambidextrous or hipShooting
  renegade_sureStrike = node("renegade_sureStrike")
  renegade_disarm = node("renegade_disarm")
  renegade_takedown = node("renegade_takedown")

  #bestCraftLasgun or goodCraftBoltgun or commonCraftPlasmaGun or commonCraftFlamer
  renegade_ambidextrous = node("renegade_ambidextrous")
  renegade_hipShooting = node("renegade_hipShooting")

  #bestCraftLasPistol or commonCraftBoltPistol
  renegade_bestCraftLasGun = node("renegade_bestCraftLasGun")
  renegade_goodCraftBoltGun = node("renegade_goodCraftBoltGun")
  renegade_commonCraftPlasmaGun = node("commonCraftPlasmaGun")
  renegade_commonCraftFlamer = node("commonCraftFlamer")

  #bestCraftChainsword or commonCraftPowerMace
  renegade_bestCraftLasPistol = node("renegade_bestCraftLasPistol")
  renegade_commonCraftBoltPistol = node("renegade_commonCraftBoltPistol")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  renegade_bestCraftChainsword = node("renegade_bestCraftChainsword")
  renegade_commonCraftPowerMace = node("renegade_commonCraftPowerMace")

  renegade_bestCraftLasPistol.next.append(renegade_bestCraftChainsword)
  renegade_bestCraftLasPistol.next.append(renegade_commonCraftPowerMace)
  renegade_commonCraftBoltPistol.next.append(renegade_bestCraftChainsword)
  renegade_commonCraftBoltPistol.next.append(renegade_commonCraftPowerMace)

  renegade_bestCraftLasGun.next.append(renegade_bestCraftLasPistol)
  renegade_bestCraftLasGun.next.append(renegade_commonCraftBoltPistol)
  renegade_goodCraftBoltGun.next.append(renegade_bestCraftLasPistol)
  renegade_goodCraftBoltGun.next.append(renegade_commonCraftBoltPistol)
  renegade_commonCraftPlasmaGun.next.append(renegade_bestCraftLasPistol)
  renegade_commonCraftPlasmaGun.next.append(renegade_commonCraftBoltPistol)
  renegade_commonCraftFlamer.next.append(renegade_bestCraftLasPistol)
  renegade_commonCraftFlamer.next.append(renegade_commonCraftBoltPistol)

  renegade_ambidextrous.next.append(renegade_bestCraftLasGun)
  renegade_ambidextrous.next.append(renegade_goodCraftBoltGun)
  renegade_ambidextrous.next.append(renegade_commonCraftPlasmaGun)
  renegade_ambidextrous.next.append(renegade_commonCraftFlamer)
  renegade_hipShooting.next.append(renegade_bestCraftLasGun)
  renegade_hipShooting.next.append(renegade_goodCraftBoltGun)
  renegade_hipShooting.next.append(renegade_commonCraftPlasmaGun)
  renegade_hipShooting.next.append(renegade_commonCraftFlamer)

  renegade_sureStrike.next.append(renegade_ambidextrous)
  renegade_sureStrike.next.append(renegade_hipShooting)
  renegade_disarm.next.append(renegade_ambidextrous)
  renegade_disarm.next.append(renegade_hipShooting)
  renegade_takedown.next.append(renegade_ambidextrous)
  renegade_takedown.next.append(renegade_hipShooting)

  renegade_catfall.next.append(renegade_sureStrike)
  renegade_catfall.next.append(renegade_disarm)
  renegade_catfall.next.append(renegade_takedown)
  renegade_combatSenses.next.append(renegade_sureStrike)
  renegade_combatSenses.next.append(renegade_disarm)
  renegade_combatSenses.next.append(renegade_takedown)

  renegade_weaponTrainingBolt.next.append(renegade_catfall)
  renegade_weaponTrainingBolt.next.append(renegade_combatSenses)
  renegade_weaponTrainingShock.next.append(renegade_catfall)
  renegade_weaponTrainingShock.next.append(renegade_combatSenses)

  renegade_techUse.next.append(renegade_weaponTrainingBolt)
  renegade_techUse.next.append(renegade_weaponTrainingShock)
  renegade_medicae.next.append(renegade_weaponTrainingBolt)
  renegade_medicae.next.append(renegade_weaponTrainingShock)


  renegade_survival.next.append(renegade_techUse)
  renegade_survival.next.append(renegade_medicae)
  renegade_stealth.next.append(renegade_techUse)
  renegade_stealth.next.append(renegade_medicae)

  renegade_dodge10.next.append(renegade_survival)
  renegade_dodge10.next.append(renegade_stealth)
  renegade_parry10.next.append(renegade_survival)
  renegade_parry10.next.append(renegade_stealth)

  renegade_command.next.append(renegade_dodge10)
  renegade_command.next.append(renegade_parry10)
  renegade_intimidate.next.append(renegade_dodge10)
  renegade_intimidate.next.append(renegade_parry10)

  renegade.next.append(renegade_command)
  renegade.next.append(renegade_intimidate)

  #deceive or intimidate
  psyker = node("psyker")
  
  #dodge or parry
  psyker_deceive = node("psyker_deceive")
  psyker_intimidate = node("psyker_intimidate")

  #weaponTrainingLas or weaponTrainingSP or weaponTrainingShock
  psyker_dodge = node("psyker_dodge")
  psyker_parry = node("psyker_parry")

  #warpSense or childOfTheWarp
  psyker_weaponTrainingLas = node("psyker_weaponTrainingLas")
  psyker_weaponTrainingSP = node("psyker_weaponTrainingSP")
  psyker_weaponTrainingShock = node("psyker_weaponTrainingShock")

  #commonCraftLasPistol or commonCraftStubRevolver
  psyker_warpSense = node("psyker_warpSense")
  psyker_childOfTheWarp = node("psyker_childOfTheWarp")

  #goodCraftSword or commonCraftNeuralWhip
  psyker_commonCraftLasPistol = node("psyker_commonCraftLasPistol")
  psyker_commonCraftStubRevolver = node("psyker_commonCraftStubRevolver")

  #beauty or charm or craftsmanship or devotion or fortitutde or foresight or logic or martialProwess or grace or wealth
  psyker_commonCraftSword = node("psyker_commonCraftSword")
  psyker_commonCraftNeuralWhip = node("psyker_commonCraftNeuralWhip")

  psyker_commonCraftLasPistol.next.append(psyker_commonCraftSword)
  psyker_commonCraftLasPistol.next.append(psyker_commonCraftNeuralWhip)
  psyker_commonCraftStubRevolver.next.append(psyker_commonCraftSword)
  psyker_commonCraftStubRevolver.next.append(psyker_commonCraftNeuralWhip)

  psyker_warpSense.next.append(psyker_commonCraftLasPistol)
  psyker_warpSense.next.append(psyker_commonCraftStubRevolver)
  psyker_childOfTheWarp.next.append(psyker_commonCraftLasPistol)
  psyker_childOfTheWarp.next.append(psyker_commonCraftStubRevolver)

  psyker_weaponTrainingLas.next.append(psyker_warpSense)
  psyker_weaponTrainingLas.next.append(psyker_childOfTheWarp)
  psyker_weaponTrainingSP.next.append(psyker_warpSense)
  psyker_weaponTrainingSP.next.append(psyker_childOfTheWarp)
  psyker_weaponTrainingShock.next.append(psyker_warpSense)
  psyker_weaponTrainingShock.next.append(psyker_childOfTheWarp)

  psyker_dodge.next.append(psyker_weaponTrainingLas)
  psyker_dodge.next.append(psyker_weaponTrainingSP)
  psyker_dodge.next.append(psyker_weaponTrainingShock)
  psyker_parry.next.append(psyker_weaponTrainingLas)
  psyker_parry.next.append(psyker_weaponTrainingSP)
  psyker_parry.next.append(psyker_weaponTrainingShock)

  psyker_deceive.next.append(psyker_dodge)
  psyker_deceive.next.append(psyker_parry)
  psyker_intimidate.next.append(psyker_dodge)
  psyker_intimidate.next.append(psyker_parry)

  psyker.next.append(psyker_deceive)
  psyker.next.append(psyker_intimidate)

  human.next.append(apostate)
  human.next.append(heretek)
  human.next.append(renegade)
  human.next.append(psyker)

  #betrayal or deceit or dread or destruction or gluttony or greed or hubris or regret or waste or wrath
  pride_beauty = node("pride_beauty")
  pride_charm = node("pride_charm")
  pride_craftsmanship = node("pride_craftsmanship")
  pride_devotion = node("pride_devotion")
  pride_fortitude = node("pride_fortitude")
  pride_foresight = node("pride_foresight")
  pride_logic = node("pride_logic")
  pride_martialProwess = node("pride_martialProwess")
  pride_grace = node("pride_grace")
  pride_wealth = node("pride_wealth")

  #arcane or ascendancy or dominion or immortality or innovation or legacy or nihilism or perfection or vengeance or violence
  disgrace_betrayal = node("disgrace_betrayal")
  disgrace_deceit = node("disgrace_deceit")
  disgrace_dread = node("disgrace_dread")
  disgrace_destruction = node("disgrace_destruction")
  disgrace_gluttony = node("disgrace_gluttony")
  disgrace_greed = node("disgrace_greed")
  disgrace_hubris = node("disgrace_hubris")
  disgrace_regret = node("disgrace_regret")
  disgrace_waste = node("disgrace_waste")
  disgrace_wrath = node("disgrace_wrath")

  motivation_arcane = node("motivation_arcane")
  motivation_ascendancy = node("motivation_ascendancy")
  motivation_dominion = node("motivation_dominion")
  motivation_immortality = node("motivation_immortality")
  motivation_innovation = node("motivation_innovation")
  motivation_legacy = node("motivation_legacy")
  motivation_nihilism = node("motivation_nihilism")
  motivation_perfection = node("motivation_perfection")
  motivation_vengeance = node("motivation_vengeance")
  motivation_violence = node("motivation_violence")

  disgrace_betrayal.next.append(motivation_arcane)
  disgrace_betrayal.next.append(motivation_ascendancy)
  disgrace_betrayal.next.append(motivation_dominion)
  disgrace_betrayal.next.append(motivation_immortality)
  disgrace_betrayal.next.append(motivation_innovation)
  disgrace_betrayal.next.append(motivation_legacy)
  disgrace_betrayal.next.append(motivation_nihilism)
  disgrace_betrayal.next.append(motivation_perfection)
  disgrace_betrayal.next.append(motivation_vengeance)
  disgrace_betrayal.next.append(motivation_violence)

  disgrace_deceit.next.append(motivation_arcane)
  disgrace_deceit.next.append(motivation_ascendancy)
  disgrace_deceit.next.append(motivation_dominion)
  disgrace_deceit.next.append(motivation_immortality)
  disgrace_deceit.next.append(motivation_innovation)
  disgrace_deceit.next.append(motivation_legacy)
  disgrace_deceit.next.append(motivation_nihilism)
  disgrace_deceit.next.append(motivation_perfection)
  disgrace_deceit.next.append(motivation_vengeance)
  disgrace_deceit.next.append(motivation_violence)

  disgrace_dread.next.append(motivation_arcane)
  disgrace_dread.next.append(motivation_ascendancy)
  disgrace_dread.next.append(motivation_dominion)
  disgrace_dread.next.append(motivation_immortality)
  disgrace_dread.next.append(motivation_innovation)
  disgrace_dread.next.append(motivation_legacy)
  disgrace_dread.next.append(motivation_nihilism)
  disgrace_dread.next.append(motivation_perfection)
  disgrace_dread.next.append(motivation_vengeance)
  disgrace_dread.next.append(motivation_violence)

  disgrace_destruction.next.append(motivation_arcane)
  disgrace_destruction.next.append(motivation_ascendancy)
  disgrace_destruction.next.append(motivation_dominion)
  disgrace_destruction.next.append(motivation_immortality)
  disgrace_destruction.next.append(motivation_innovation)
  disgrace_destruction.next.append(motivation_legacy)
  disgrace_destruction.next.append(motivation_nihilism)
  disgrace_destruction.next.append(motivation_perfection)
  disgrace_destruction.next.append(motivation_vengeance)
  disgrace_destruction.next.append(motivation_violence)

  disgrace_gluttony.next.append(motivation_arcane)
  disgrace_gluttony.next.append(motivation_ascendancy)
  disgrace_gluttony.next.append(motivation_dominion)
  disgrace_gluttony.next.append(motivation_immortality)
  disgrace_gluttony.next.append(motivation_innovation)
  disgrace_gluttony.next.append(motivation_legacy)
  disgrace_gluttony.next.append(motivation_nihilism)
  disgrace_gluttony.next.append(motivation_perfection)
  disgrace_gluttony.next.append(motivation_vengeance)
  disgrace_gluttony.next.append(motivation_violence)

  disgrace_greed.next.append(motivation_arcane)
  disgrace_greed.next.append(motivation_ascendancy)
  disgrace_greed.next.append(motivation_dominion)
  disgrace_greed.next.append(motivation_immortality)
  disgrace_greed.next.append(motivation_innovation)
  disgrace_greed.next.append(motivation_legacy)
  disgrace_greed.next.append(motivation_nihilism)
  disgrace_greed.next.append(motivation_perfection)
  disgrace_greed.next.append(motivation_vengeance)
  disgrace_greed.next.append(motivation_violence)

  disgrace_hubris.next.append(motivation_arcane)
  disgrace_hubris.next.append(motivation_ascendancy)
  disgrace_hubris.next.append(motivation_dominion)
  disgrace_hubris.next.append(motivation_immortality)
  disgrace_hubris.next.append(motivation_innovation)
  disgrace_hubris.next.append(motivation_legacy)
  disgrace_hubris.next.append(motivation_nihilism)
  disgrace_hubris.next.append(motivation_perfection)
  disgrace_hubris.next.append(motivation_vengeance)
  disgrace_hubris.next.append(motivation_violence)

  disgrace_regret.next.append(motivation_arcane)
  disgrace_regret.next.append(motivation_ascendancy)
  disgrace_regret.next.append(motivation_dominion)
  disgrace_regret.next.append(motivation_immortality)
  disgrace_regret.next.append(motivation_innovation)
  disgrace_regret.next.append(motivation_legacy)
  disgrace_regret.next.append(motivation_nihilism)
  disgrace_regret.next.append(motivation_perfection)
  disgrace_regret.next.append(motivation_vengeance)
  disgrace_regret.next.append(motivation_violence)

  disgrace_waste.next.append(motivation_arcane)
  disgrace_waste.next.append(motivation_ascendancy)
  disgrace_waste.next.append(motivation_dominion)
  disgrace_waste.next.append(motivation_immortality)
  disgrace_waste.next.append(motivation_innovation)
  disgrace_waste.next.append(motivation_legacy)
  disgrace_waste.next.append(motivation_nihilism)
  disgrace_waste.next.append(motivation_perfection)
  disgrace_waste.next.append(motivation_vengeance)
  disgrace_waste.next.append(motivation_violence)

  disgrace_wrath.next.append(motivation_arcane)
  disgrace_wrath.next.append(motivation_ascendancy)
  disgrace_wrath.next.append(motivation_dominion)
  disgrace_wrath.next.append(motivation_immortality)
  disgrace_wrath.next.append(motivation_innovation)
  disgrace_wrath.next.append(motivation_legacy)
  disgrace_wrath.next.append(motivation_nihilism)
  disgrace_wrath.next.append(motivation_perfection)
  disgrace_wrath.next.append(motivation_vengeance)
  disgrace_wrath.next.append(motivation_violence)

  pride_beauty.next.append(disgrace_betrayal)
  pride_beauty.next.append(disgrace_deceit)
  pride_beauty.next.append(disgrace_dread)
  pride_beauty.next.append(disgrace_destruction)
  pride_beauty.next.append(disgrace_gluttony)
  pride_beauty.next.append(disgrace_greed)
  pride_beauty.next.append(disgrace_hubris)
  pride_beauty.next.append(disgrace_regret)
  pride_beauty.next.append(disgrace_waste)
  pride_beauty.next.append(disgrace_wrath)

  pride_charm.next.append(disgrace_betrayal)
  pride_charm.next.append(disgrace_deceit)
  pride_charm.next.append(disgrace_dread)
  pride_charm.next.append(disgrace_destruction)
  pride_charm.next.append(disgrace_gluttony)
  pride_charm.next.append(disgrace_greed)
  pride_charm.next.append(disgrace_hubris)
  pride_charm.next.append(disgrace_regret)
  pride_charm.next.append(disgrace_waste)
  pride_charm.next.append(disgrace_wrath)

  pride_craftsmanship.next.append(disgrace_betrayal)
  pride_craftsmanship.next.append(disgrace_deceit)
  pride_craftsmanship.next.append(disgrace_dread)
  pride_craftsmanship.next.append(disgrace_destruction)
  pride_craftsmanship.next.append(disgrace_gluttony)
  pride_craftsmanship.next.append(disgrace_greed)
  pride_craftsmanship.next.append(disgrace_hubris)
  pride_craftsmanship.next.append(disgrace_regret)
  pride_craftsmanship.next.append(disgrace_waste)
  pride_craftsmanship.next.append(disgrace_wrath)

  pride_devotion.next.append(disgrace_betrayal)
  pride_devotion.next.append(disgrace_deceit)
  pride_devotion.next.append(disgrace_dread)
  pride_devotion.next.append(disgrace_destruction)
  pride_devotion.next.append(disgrace_gluttony)
  pride_devotion.next.append(disgrace_greed)
  pride_devotion.next.append(disgrace_hubris)
  pride_devotion.next.append(disgrace_regret)
  pride_devotion.next.append(disgrace_waste)
  pride_devotion.next.append(disgrace_wrath)

  pride_fortitude.next.append(disgrace_betrayal)
  pride_fortitude.next.append(disgrace_deceit)
  pride_fortitude.next.append(disgrace_dread)
  pride_fortitude.next.append(disgrace_destruction)
  pride_fortitude.next.append(disgrace_gluttony)
  pride_fortitude.next.append(disgrace_greed)
  pride_fortitude.next.append(disgrace_hubris)
  pride_fortitude.next.append(disgrace_regret)
  pride_fortitude.next.append(disgrace_waste)
  pride_fortitude.next.append(disgrace_wrath)

  pride_foresight.next.append(disgrace_betrayal)
  pride_foresight.next.append(disgrace_deceit)
  pride_foresight.next.append(disgrace_dread)
  pride_foresight.next.append(disgrace_destruction)
  pride_foresight.next.append(disgrace_gluttony)
  pride_foresight.next.append(disgrace_greed)
  pride_foresight.next.append(disgrace_hubris)
  pride_foresight.next.append(disgrace_regret)
  pride_foresight.next.append(disgrace_waste)
  pride_foresight.next.append(disgrace_wrath)

  pride_logic.next.append(disgrace_betrayal)
  pride_logic.next.append(disgrace_deceit)
  pride_logic.next.append(disgrace_dread)
  pride_logic.next.append(disgrace_destruction)
  pride_logic.next.append(disgrace_gluttony)
  pride_logic.next.append(disgrace_greed)
  pride_logic.next.append(disgrace_hubris)
  pride_logic.next.append(disgrace_regret)
  pride_logic.next.append(disgrace_waste)
  pride_logic.next.append(disgrace_wrath)

  pride_martialProwess.next.append(disgrace_betrayal)
  pride_martialProwess.next.append(disgrace_deceit)
  pride_martialProwess.next.append(disgrace_dread)
  pride_martialProwess.next.append(disgrace_destruction)
  pride_martialProwess.next.append(disgrace_gluttony)
  pride_martialProwess.next.append(disgrace_greed)
  pride_martialProwess.next.append(disgrace_hubris)
  pride_martialProwess.next.append(disgrace_regret)
  pride_martialProwess.next.append(disgrace_waste)
  pride_martialProwess.next.append(disgrace_wrath)

  pride_grace.next.append(disgrace_betrayal)
  pride_grace.next.append(disgrace_deceit)
  pride_grace.next.append(disgrace_dread)
  pride_grace.next.append(disgrace_destruction)
  pride_grace.next.append(disgrace_gluttony)
  pride_grace.next.append(disgrace_greed)
  pride_grace.next.append(disgrace_hubris)
  pride_grace.next.append(disgrace_regret)
  pride_grace.next.append(disgrace_waste)
  pride_grace.next.append(disgrace_wrath)

  pride_wealth.next.append(disgrace_betrayal)
  pride_wealth.next.append(disgrace_deceit)
  pride_wealth.next.append(disgrace_dread)
  pride_wealth.next.append(disgrace_destruction)
  pride_wealth.next.append(disgrace_gluttony)
  pride_wealth.next.append(disgrace_greed)
  pride_wealth.next.append(disgrace_hubris)
  pride_wealth.next.append(disgrace_regret)
  pride_wealth.next.append(disgrace_waste)
  pride_wealth.next.append(disgrace_wrath)

  champion_lesserMinion.next.append(pride_beauty)
  champion_lesserMinion.next.append(pride_charm)
  champion_lesserMinion.next.append(pride_craftsmanship)
  champion_lesserMinion.next.append(pride_devotion)
  champion_lesserMinion.next.append(pride_fortitude)
  champion_lesserMinion.next.append(pride_foresight)
  champion_lesserMinion.next.append(pride_logic)
  champion_lesserMinion.next.append(pride_martialProwess)
  champion_lesserMinion.next.append(pride_grace)
  champion_lesserMinion.next.append(pride_wealth)

  champion_sureStrike.next.append(pride_beauty)
  champion_sureStrike.next.append(pride_charm)
  champion_sureStrike.next.append(pride_craftsmanship)
  champion_sureStrike.next.append(pride_devotion)
  champion_sureStrike.next.append(pride_fortitude)
  champion_sureStrike.next.append(pride_foresight)
  champion_sureStrike.next.append(pride_logic)
  champion_sureStrike.next.append(pride_martialProwess)
  champion_sureStrike.next.append(pride_grace)
  champion_sureStrike.next.append(pride_wealth)

  chosen_sureStrike.next.append(pride_beauty)
  chosen_sureStrike.next.append(pride_charm)
  chosen_sureStrike.next.append(pride_craftsmanship)
  chosen_sureStrike.next.append(pride_devotion)
  chosen_sureStrike.next.append(pride_fortitude)
  chosen_sureStrike.next.append(pride_foresight)
  chosen_sureStrike.next.append(pride_logic)
  chosen_sureStrike.next.append(pride_martialProwess)
  chosen_sureStrike.next.append(pride_grace)
  chosen_sureStrike.next.append(pride_wealth)

  chosen_deadeyeShot.next.append(pride_beauty)
  chosen_deadeyeShot.next.append(pride_charm)
  chosen_deadeyeShot.next.append(pride_craftsmanship)
  chosen_deadeyeShot.next.append(pride_devotion)
  chosen_deadeyeShot.next.append(pride_fortitude)
  chosen_deadeyeShot.next.append(pride_foresight)
  chosen_deadeyeShot.next.append(pride_logic)
  chosen_deadeyeShot.next.append(pride_martialProwess)
  chosen_deadeyeShot.next.append(pride_grace)
  chosen_deadeyeShot.next.append(pride_wealth)

  forsaken_coldHearted.next.append(pride_beauty)
  forsaken_coldHearted.next.append(pride_charm)
  forsaken_coldHearted.next.append(pride_craftsmanship)
  forsaken_coldHearted.next.append(pride_devotion)
  forsaken_coldHearted.next.append(pride_fortitude)
  forsaken_coldHearted.next.append(pride_foresight)
  forsaken_coldHearted.next.append(pride_logic)
  forsaken_coldHearted.next.append(pride_martialProwess)
  forsaken_coldHearted.next.append(pride_grace)
  forsaken_coldHearted.next.append(pride_wealth)

  forsaken_soundConstitution.next.append(pride_beauty)
  forsaken_soundConstitution.next.append(pride_charm)
  forsaken_soundConstitution.next.append(pride_craftsmanship)
  forsaken_soundConstitution.next.append(pride_devotion)
  forsaken_soundConstitution.next.append(pride_fortitude)
  forsaken_soundConstitution.next.append(pride_foresight)
  forsaken_soundConstitution.next.append(pride_logic)
  forsaken_soundConstitution.next.append(pride_martialProwess)
  forsaken_soundConstitution.next.append(pride_grace)
  forsaken_soundConstitution.next.append(pride_wealth)

  sorcerer_meditation.next.append(pride_beauty)
  sorcerer_meditation.next.append(pride_charm)
  sorcerer_meditation.next.append(pride_craftsmanship)
  sorcerer_meditation.next.append(pride_devotion)
  sorcerer_meditation.next.append(pride_fortitude)
  sorcerer_meditation.next.append(pride_foresight)
  sorcerer_meditation.next.append(pride_logic)
  sorcerer_meditation.next.append(pride_martialProwess)
  sorcerer_meditation.next.append(pride_grace)
  sorcerer_meditation.next.append(pride_wealth)

  sorcerer_mimic.next.append(pride_beauty)
  sorcerer_mimic.next.append(pride_charm)
  sorcerer_mimic.next.append(pride_craftsmanship)
  sorcerer_mimic.next.append(pride_devotion)
  sorcerer_mimic.next.append(pride_fortitude)
  sorcerer_mimic.next.append(pride_foresight)
  sorcerer_mimic.next.append(pride_logic)
  sorcerer_mimic.next.append(pride_martialProwess)
  sorcerer_mimic.next.append(pride_grace)
  sorcerer_mimic.next.append(pride_wealth)

  apostate_flackArmor.next.append(pride_beauty)
  apostate_flackArmor.next.append(pride_charm)
  apostate_flackArmor.next.append(pride_craftsmanship)
  apostate_flackArmor.next.append(pride_devotion)
  apostate_flackArmor.next.append(pride_fortitude)
  apostate_flackArmor.next.append(pride_foresight)
  apostate_flackArmor.next.append(pride_logic)
  apostate_flackArmor.next.append(pride_martialProwess)
  apostate_flackArmor.next.append(pride_grace)
  apostate_flackArmor.next.append(pride_wealth)

  apostate_meshArmor.next.append(pride_beauty)
  apostate_meshArmor.next.append(pride_charm)
  apostate_meshArmor.next.append(pride_craftsmanship)
  apostate_meshArmor.next.append(pride_devotion)
  apostate_meshArmor.next.append(pride_fortitude)
  apostate_meshArmor.next.append(pride_foresight)
  apostate_meshArmor.next.append(pride_logic)
  apostate_meshArmor.next.append(pride_martialProwess)
  apostate_meshArmor.next.append(pride_grace)
  apostate_meshArmor.next.append(pride_wealth)

  heretek_lumeninCapacitors.next.append(pride_beauty)
  heretek_lumeninCapacitors.next.append(pride_charm)
  heretek_lumeninCapacitors.next.append(pride_craftsmanship)
  heretek_lumeninCapacitors.next.append(pride_devotion)
  heretek_lumeninCapacitors.next.append(pride_fortitude)
  heretek_lumeninCapacitors.next.append(pride_foresight)
  heretek_lumeninCapacitors.next.append(pride_logic)
  heretek_lumeninCapacitors.next.append(pride_martialProwess)
  heretek_lumeninCapacitors.next.append(pride_grace)
  heretek_lumeninCapacitors.next.append(pride_wealth)

  heretek_maglevCoils.next.append(pride_beauty)
  heretek_maglevCoils.next.append(pride_charm)
  heretek_maglevCoils.next.append(pride_craftsmanship)
  heretek_maglevCoils.next.append(pride_devotion)
  heretek_maglevCoils.next.append(pride_fortitude)
  heretek_maglevCoils.next.append(pride_foresight)
  heretek_maglevCoils.next.append(pride_logic)
  heretek_maglevCoils.next.append(pride_martialProwess)
  heretek_maglevCoils.next.append(pride_grace)
  heretek_maglevCoils.next.append(pride_wealth)

  heretek_ferricLureImplants.next.append(pride_beauty)
  heretek_ferricLureImplants.next.append(pride_charm)
  heretek_ferricLureImplants.next.append(pride_craftsmanship)
  heretek_ferricLureImplants.next.append(pride_devotion)
  heretek_ferricLureImplants.next.append(pride_fortitude)
  heretek_ferricLureImplants.next.append(pride_foresight)
  heretek_ferricLureImplants.next.append(pride_logic)
  heretek_ferricLureImplants.next.append(pride_martialProwess)
  heretek_ferricLureImplants.next.append(pride_grace)
  heretek_ferricLureImplants.next.append(pride_wealth)

  renegade_bestCraftChainsword.next.append(pride_beauty)
  renegade_bestCraftChainsword.next.append(pride_charm)
  renegade_bestCraftChainsword.next.append(pride_craftsmanship)
  renegade_bestCraftChainsword.next.append(pride_devotion)
  renegade_bestCraftChainsword.next.append(pride_fortitude)
  renegade_bestCraftChainsword.next.append(pride_foresight)
  renegade_bestCraftChainsword.next.append(pride_logic)
  renegade_bestCraftChainsword.next.append(pride_martialProwess)
  renegade_bestCraftChainsword.next.append(pride_grace)
  renegade_bestCraftChainsword.next.append(pride_wealth)

  renegade_commonCraftPowerMace.next.append(pride_beauty)
  renegade_commonCraftPowerMace.next.append(pride_charm)
  renegade_commonCraftPowerMace.next.append(pride_craftsmanship)
  renegade_commonCraftPowerMace.next.append(pride_devotion)
  renegade_commonCraftPowerMace.next.append(pride_fortitude)
  renegade_commonCraftPowerMace.next.append(pride_foresight)
  renegade_commonCraftPowerMace.next.append(pride_logic)
  renegade_commonCraftPowerMace.next.append(pride_martialProwess)
  renegade_commonCraftPowerMace.next.append(pride_grace)
  renegade_commonCraftPowerMace.next.append(pride_wealth)

  psyker_commonCraftSword.next.append(pride_beauty)
  psyker_commonCraftSword.next.append(pride_charm)
  psyker_commonCraftSword.next.append(pride_craftsmanship)
  psyker_commonCraftSword.next.append(pride_devotion)
  psyker_commonCraftSword.next.append(pride_fortitude)
  psyker_commonCraftSword.next.append(pride_foresight)
  psyker_commonCraftSword.next.append(pride_logic)
  psyker_commonCraftSword.next.append(pride_martialProwess)
  psyker_commonCraftSword.next.append(pride_grace)
  psyker_commonCraftSword.next.append(pride_wealth)

  psyker_commonCraftNeuralWhip.next.append(pride_beauty)
  psyker_commonCraftNeuralWhip.next.append(pride_charm)
  psyker_commonCraftNeuralWhip.next.append(pride_craftsmanship)
  psyker_commonCraftNeuralWhip.next.append(pride_devotion)
  psyker_commonCraftNeuralWhip.next.append(pride_fortitude)
  psyker_commonCraftNeuralWhip.next.append(pride_foresight)
  psyker_commonCraftNeuralWhip.next.append(pride_logic)
  psyker_commonCraftNeuralWhip.next.append(pride_martialProwess)
  psyker_commonCraftNeuralWhip.next.append(pride_grace)
  psyker_commonCraftNeuralWhip.next.append(pride_wealth)

  start.next.append(spaceMarine)
  start.next.append(human)
  
  return start

def randRecursiveWalk(start):
  print(start.name)
  length = len(start.next)
  if(length > 0):
    choice = randint(0, length-1)
    randRecursiveWalk(start.next[choice])

start = initializeTest2()
randRecursiveWalk(start)
