import discord
import random
import re
import asyncio
import time
import datetime
import os


pokemonlist = {'bulbasaur':'1SpA', 'ivysaur':'1SpA, 1SpD', 'venusaur':'2SpA, 1SpD', 'charmander':'1Spe', 'charmeleon':'1SpA, 1Spe', 'charizard':'3SpA', 'squirtle':'1Def', 'wartortle':'1Def, 1SpD', 'blastoise':'3SpD', 'caterpie':'1HP', 'metapod':'2Def', 'butterfree':'2SpA, 1SpD', 'weedle':'1Spe', 'kakuna':'2Def', 'beedrill':'2Atk, 1SpD', 'pidgey':'1Spe', 'pidgeotto':'2Spe', 'pidgeot':'3Spe', 'rattata':'1Spe', 'raticate':'2Spe', 'spearow':'1Spe', 'fearow':'2Spe', 'ekans':'1Atk', 'arbok':'2Atk', 'pikachu':'2Spe', 'raichu':'3Spe', 'sandshrew':'1Def', 'sandslash':'2Def', 'nidoran':'♀: 1HP, ♂: 1Atk', 'nidorino':'2HP', 'nidoqueen':'3HP', 'nidorino':'2Atk', 'nidoking':'3Atk', 'clefairy':'2HP', 'clefable':'3HP', 'vulpix':'1Spe', 'ninetales':'1SpD, 1Spe', 'jugglypuff':'2HP', 'wigglypuff':'3HP', 'zubat':'1Spe', 'golbat':'2Spe', 'oddish':'1SpA', 'gloom':'2SpA', 'vileplume':'3SpA', 'paras':'1Atk', 'parasect':'2Atk', 'venonat':'1SpD', 'venomoth':'1SpA, 1Spe', 'diglett':'1Spe', 'dugtrio':'2Spe', 'meowth':'1Spe', 'persian':'2Spe', 'psyduck':'1SpA', 'golduck':'2SpA', 'mankey':'1Atk', 'primeape':'2Atk', 'growlithe':'1Atk', 'arcanine':'2Atk', 'poliwag':'1Spe', 'poliwhirl':'2Spe', 'poliwrath':'3Def', 'abra':'1SpD', 'kadabra':'2SpD', 'alakazam':'3SpD', 'machop':'1Atk', 'machoke':'2Atk', 'machamp':'3Atk', 'bellsprout':'1Atk', 'weepinbell':'2Atk', 'victreebel':'3Atk', 'tentacool':'1SpD', 'tentacruel':'2SpD', 'geodude':'1Def', 'graveler':'2Def', 'golem':'3Def', 'ponyta':'1Spe', 'rapidash':'2Spe', 'slowpoke':'1HP', 'slowbro':'2Def', 'magnemite':'1SpD', 'magnetone':'2SpD', 'farfetchd':'1Atk', 'doduo':'1Atk', 'dodrio':'2Atk', 'seel':'1SpD', 'dewgong':'2SpD', 'grimer':'1HP', 'muk':'1HP, 1Atk', 'shellder':'1Def', 'cloyster':'2Def', 'gastly':'1SpA', 'haunter':'2SpA', 'gengar':'3SpA', 'onix':'1Def', 'drowzee':'1SpD', 'hypno':'2SpD', 'krabby':'1Atk', 'kingler':'2Atk', 'voltorb':'1Spe', 'electrode':'2Spe', 'exeggcute':'1Def', 'exeggutor':'2SpA', 'cubone':'1Def', 'marowak':'2Def', 'hitmonlee':'2Atk', 'hitmonchan':'2SpD', 'lickitung':'2HP', 'koffing':'1Def', 'weezing':'2Def', 'rhyhorn':'1Def', 'rhydon':'2Atk', 'chansey':'2HP', 'tangela':'1Def', 'kangaskhan':'2HP', 'horsea':'1SpA', 'seadra':'1Def, 1SpA', 'goldeen':'1Atk', 'seaking':'2Atk', 'staryu':'1Spe', 'starmie':'2Spe', 'mr. mime':'2SpD', 'scyther':'1Atk', 'jynx':'2SpA', 'electabuzz':'2Spe', 'magmar':'2SpA', 'pinsir':'2Atk', 'tauros':'1Atk', 'magikarp':'1Spe', 'gyarados':'2Atk', 'lapras':'2HP', 'ditto':'1HP', 'eevee':'1SpD', 'vaporeon':'2HP', 'jolteon':'2Spe', 'flareon':'2Atk', 'porygon':'1SpA', 'omanyte':'1Def', 'omastar':'2Def', 'kabuto':'1Def', 'kabutops':'2Atk', 'aerodactyl':'2Spe', 'snorlax':'2HP', 'articuno':'3SpD', 'zapdos':'3SpA', 'moltres':'3SpA', 'dratini':'1Atk', 'dragonair':'2Atk', 'dragonite':'3Atk', 'mewtwo':'3SpA', 'mew':'3HP', 'chikorita':'1SpD', 'bayleef':'1Def, 1SpD', 'meganium':'1Def, 2SpD', 'cyndaquil':'1Spe', 'quilava':'1SpA, 1Spe', 'typhlosion':'3SpA', 'totodile':'1Atk', 'croconaw':'1Atk, 1Def', 'feraligatr':'2Atk, 1Def', 'sentret':'1Atk', 'furret':'1Spe', 'hoothoot':'1HP', 'noctowl':'2HP', 'ledyba':'1SpD', 'ledian':'2SpD', 'spinarak':'1Atk', 'ariados':'2Atk', 'crobat':'3Spe', 'chinchou':'1HP', 'lanturn':'2HP', 'pichu':'1Spe', 'cleffa':'1SpD', 'igglybuff':'1HP', 'togepi':'1SpD', 'togetic':'2SpD', 'natu':'1SpA', 'xatu':'1SpA, 1Spe', 'mareep':'1SpA', 'flaaffy':'2SpA', 'ampharos':'3SpA', 'bellossom':'3SpD', 'marill':'2HP', 'azumarill':'3HP', 'sudowoodoo':'2Def', 'politoed':'3SpD', 'hoppip':'1SpD', 'skiploom':'2Spe', 'jumpluff':'3Spe', 'aipom':'1Spe', 'sunkern':'1SpA', 'sunflora':'2SpA', 'yanma':'1Spe', 'wooper':'1HP', 'quagsire':'2HP', 'espeon':'2SpA', 'umbreon':'2SpD', 'murkrow':'1Spe', 'slowking':'3SpD', 'misdeavus':'1SpD', 'unown':'1Atk', 'wobbuffet':'2HP', 'girafarig':'2SpA', 'pimeco':'1Def', 'forretress':'2Def', 'dunsparce':'1HP', 'gligar':'1Def', 'steelix':'2Def', 'snubbull':'1Atk', 'granbull':'2Atk', 'qwillfish':'1Atk', 'scizor':'2Atk', 'shuckle':'1Def, 1SpD', 'heracross':'2Atk', 'sneasel':'1Spe', 'teddiursa':'1Atk', 'ursaring':'2Atk', 'slugma':'1SpA', 'magcargo':'2Def', 'swinub':'1Atk', 'piloswine':'1HP, 1Atk', 'corsola':'1Def', 'remoraid':'1SpA', 'octillery':'1Atk, 1SpA', 'delibird':'1Spe', 'mantine':'2SpD', 'skarmory':'2Def', 'houndour':'1SpA', 'houndoom':'2SpA', 'kingdra':'1Atk, 1SpA, 1SpD', 'phanpy':'1HP', 'donphan':'1Atk, 1Def', 'porygon2':'2SpA', 'stantler':'1Atk', 'smeargle':'1Spe', 'tyrogue':'1Atk', 'hitmontop':'2SpD', 'smoochum':'1SpA', 'elekid':'1Spe', 'magby':'1Spe', 'miltank':'2Def', 'blissey':'3HP', 'raikou':'1SpA, 2Spe', 'entei':'1HP, 2Atk', 'suicune':'1Def, 2SpD', 'larvitar':'1Atk', 'pupitar':'2Atk', 'tyranitar':'3Atk', 'lugia':'3SpD', 'ho-oh':'3SpD', 'celebi':'3HP', 'treecko':'1Spe', 'grovyle':'2Spe', 'sceptile':'3Spe', 'torchik':'1SpA', 'combusken':'1Atk, 1SpA', 'blaziken':'3Atk', 'mudkip':'1Atk', 'marshtomp':'2Atk', 'swampert':'3Atk', 'poochyena':'1Atk', 'mightyena':'2Atk', 'zigzagoon':'1Spe', 'linoone':'2Spe', 'wurmple':'1HP', 'silcoon':'2Def', 'beautifly':'3SpA', 'cascoon':'2Def', 'dustox':'3SpD', 'lotad':'1SpD', 'lombre':'2SpD', 'ludicolo':'3SpD', 'seedot':'1Def', 'nuzleaf':'2Atk', 'shiftry':'3Atk', 'taillow':'1Spe', 'swellow':'2Spe', 'wingull':'1Spe', 'pelliper':'2Def', 'ralts':'1SpA', 'kirlia':'2SpA', 'gardevoir':'3SpA', 'surskit':'1Spe', 'masquerain':'1SpA, 1SpD', 'shroomish':'1HP', 'breeloom':'2Atk', 'slakoth':'1HP', 'vigoroth':'2Spe', 'slaking':'3HP', 'nincada':'1Def', 'ninjask':'2Spe', 'shedinja':'2HP', 'whismur':'1HP', 'loudred':'2HP', 'exploud':'3HP', 'makuhita':'1HP', 'hariyama':'2HP', 'azurill':'1HP', 'nosepass':'1Def', 'skitty':'1Spe', 'delcatty':'1HP, 1Spe', 'sableye':'1Atk, 1Def', 'mawile':'1Def, 1Def', 'aron':'1Def', 'lairon':'2Def', 'aggron':'3Def', 'meditite':'1Spe', 'medicham':'2Spe', 'electrike':'1Spe', 'manectric':'2Spe', 'plusle':'1Spe', 'minun':'1Spe', 'volbeat':'1Spe', 'illumise':'1Spe', 'roselia':'2SpA', 'gulpin':'1HP', 'swalot':'2HP', 'carvanha':'1Atk', 'sharpedo':'2Atk', 'wailmer':'1HP', 'wailord':'2HP', 'numel':'1SpA', 'camerupt':'1Atk, 1SpA', 'torkoal':'2Def', 'spoink':'1SpD','grumpig':'2SpD', 'spinda':'1SpA', 'trapinch':'1Atk', 'vibrava':'1Atk, 1Spe', 'flygon':'1Atk, 2Spe', 'cacnea':'1SpA', 'cacturne':'1Atk, 1SpA', 'swablu':'1SpD', 'altaria':'2SpD', 'zangoose':'2Atk', 'seviper':'1Atk, 1SpA', 'lunatone':'2SpD', 'solrock':'2Atk', 'barboach':'1HP', 'whiscash':'2HP', 'corphish':'1Atk', 'crawdaunt':'2Atk', 'baltoy':'1SpD', 'claydol':'2SpD', 'lileep':'1SpD', 'cradily':'2SpD', 'anorith':'1Atk', 'armaldo':'2Atk', 'feebas':'1Spe', 'milotic':'2SpD', 'castform':'1HP', 'kecleon':'1SpD', 'shuppet':'1Atk', 'banette':'2Atk', 'duskull':'1SpD', 'dusclops':'1Def, 1SpD', 'tropius':'2HP', 'chimecho':'1SpA, 1SpD', 'absol':'2Atk', 'wynaut':'1HP', 'snorunt':'1HP', 'glalie':'1HP', 'spheal':'1HP', 'sealeo':'2HP', 'walrein':'3HP', 'clamperl':'1Def', 'huntail':'1Atk, 1Def', 'gorebyss':'2SpD', 'relicanth':'1HP, 1Def', 'luvdisc':'1Spe', 'bagon':'1Atk', 'shelgon':'2Def', 'salamence':'3Atk', 'beldum':'1Def', 'metang':'2Def', 'metagross':'3Def', 'regirock':'3Def', 'regice':'3SpD', 'registeel':'2Def, 1SpD', 'latias':'3SpD', 'latios':'3SpA', 'kyogre':'3SpA', 'groudon':'3Atk', 'rayquaza':'2Atk, 1SpA', 'jirachi':'3HP', 'deoxys':'1Atk, 1SpAm 1Spe', 'turtwig':'1Atk', 'grotle':'1Atk, 1Def', 'torterra':'2Atk, 1Def', 'chimchar':'1Spe', 'monferno':'1SpA, 1Spe', 'infernape':'1Atk, 1SpA, 1Spe', 'piplup':'1SpA', 'prinlup':'2SpA', 'empoleon':'3SpA', 'starly':'1Spe', 'staravia':'2Spe', 'staraptor':'3Atk', 'bidoof':'1HP', 'bibarel':'2Atk', 'kricketot':'1Def', 'kricketune':'2Atk', 'shinx':'1Atk', 'luxio':'2Atk', 'luxray':'3Atk', 'budew':'1SpA', 'roserade':'3SpA', 'cranidos':'1Atk', 'rampardos':'2Atk', 'shieldon':'1Def', 'bastiodon':'2Def', 'burmy':'1SpD', 'wormada':'2SpD', 'mothim':'1Atk, 1SpA', 'combee':'1Spe', 'vespiqueen':'1Def, 1SpD', 'pachirisu':'1Spe', 'buizel':'1Spe', 'floatzzel':'2Spe', 'cherubi':'1SpA', 'cherrim':'2SpA', 'shellos':'1HP', 'gastrodon':'2HP', 'ambipom':'2Spe', 'drifloon':'1HP', 'drifblim':'2HP', 'buneary':'1Spe', 'lopunny':'2Spe', 'mismagius':'1SpA, 1SpD', 'honchkrow':'2Atk', 'glameow':'1Spe', 'purugly':'2Spe', 'chingling':'1SpA', 'stunky':'1Spe', 'skuntank':'2HP', 'bronzor':'1Def', 'bonsly':'1Def, 1SpD', 'mime jr.':'1SpD', 'happiny':'1HP', 'chatot':'1Atk', 'spiritomb':'1Def, 1SpD', 'gible':'1Atk', 'gabite':'2Atk', 'garchomp':'3Atk', 'munchlax':'1HP', 'riolu':'1Atk', 'lucario':'1Atk, 1SpA', 'hippopotas':'1Def', 'hippodon':'2Def', 'skorupi':'1Def', 'drapion':'2Def', 'croagunk':'1Atk', 'toxicroak':'2Atk', 'carnivine':'2Atk', 'finneon':'1Spe', 'lumineon':'2Spe', 'mantyke':'1SpD', 'snover':'1Atk', 'abomasnow':'1Atk, 1SpA', 'weavile':'1Atk, 1Spe', 'magnezone':'3SpA', 'licklicky':'3HP', 'rhyperior':'3Atk', 'tangrowth':'2Def', 'electivire':'3Atk', 'magmortar':'3SpA', 'togekiss':'2SpA, 1SpD', 'yanmega':'2Atk', 'leafeon':'2Def', 'glaceon':'2SpA', 'gliscor':'2Def', 'mamoswine':'3Atk', 'porygonz':'3SpA', 'gallade':'3Atk', 'probopass':'1Def, 2SpD', 'dusknoir':'1Def, 2SpD', 'froslass':'2Spe', 'rotom':'1SpA, 1Spe', 'uxie':'2Def, 1SpD', 'mespirit':'1Atk, 1SpA, 1SpD', 'azelf':'2Atk, 1SpA', 'dialga':'3SpA', 'palkia':'3SpA', 'heatran':'3SpA', 'regigigas':'3Atk', 'giratina':'3HP', 'cresselia':'3SpD', 'phione':'1HP', 'manaphy':'3HP', 'darkrai':'2SpA, 1Spe', 'shaymin':'3HP', 'arceus':'3HP', 'victini':'3HP', 'snivy':'1Spe', 'servine':'2Spe', 'serperior':'3Spe', 'tepig':'1HP', 'pignite':'2Atk', 'emboar':'3Atk', 'oshawott':'1SpA', 'dewott':'2SpA', 'samurott':'3SpA', 'patrat':'1Atk', 'watchog':'2Atk', 'lillipup':'1Atk', 'herdier':'2Atk', 'stoutland':'3Atk', 'purrloin':'1Spe', 'liepard':'2Spe', 'pansage':'1Spe', 'simisage':'2Spe', 'pansear':'1Spe', 'simisear':'2Spe', 'panpour':'1Spe', 'simipour':'2Spe', 'munna':'1HP', 'musharna':'2HP', 'pidove':'1Atk', 'tranquill':'2Atk', 'unfezant':'3Atk', 'blitzle':'1Spe', 'zebstrike':'2Spe', 'roggenrola':'1Def', 'boldore':'1Atk, 1Def', 'gigalith':'3Atk', 'woobat':'1Spe', 'swoobat':'2Spe', 'drilbur':'1Atk', 'excadrill':'2Atk', 'audino':'2HP', 'timburr':'1Atk', 'gurdurr':'2Atk', 'conkeldurr':'3Atk', 'tympole':'1Spe', 'palpitoad':'2HP', 'seismitoad':'3HP', 'throh':'2HP', 'sawk':'2Atk', 'sewaddle':'1Atk', 'swadloon':'2Atk', 'leavanny':'3Atk', 'venipede':'1Def', 'whirlipede':'2Def', 'scolipede':'3Spe', 'cottonee':'1Spe', 'petilil':'2Spe', 'lilligant':'2SpA', 'basculin':'2Spe', 'sandile':'1Atk', 'krokorok':'2Atk', 'krookodile':'3Atk', 'darumaka':'1Atk', 'darmanitan':'2Atk', 'maractus':'2SpA', 'dwebble':'1Def', 'crustle':'2Def', 'scraggy':'1Atk', 'scrafty':'1Def, 1SpD', 'sigilyph':'2SpA', 'yamask':'1Def', 'cofagrigus':'2Def', 'tirtouga':'1Def', 'carracosta':'2Def', 'archen':'1Atk', 'archeops':'2Atk', 'trubbish':'1Spe', 'garbodor':'2Atk', 'zorua':'1SpA', 'zoroark':'2SpA', 'minccino':'1Spe', 'cinccino':'2Spe', 'gothita':'1SpD', 'gothorita':'2SpD', 'gothitelle':'3SpD', 'solosis':'1SpA', 'duosion':'2SpA', 'reuniclus':'3SpA', 'ducklett':'1HP', 'swanna':'2Spe', 'vanillite':'1SpA', 'vanillish':'2SpA', 'vanilluxe':'3SpA', 'deerling':'1Spe', 'sawsbuck':'2Atk', 'emolga':'2Spe', 'karrablast':'1Atk', 'escavalier':'2Atk', 'foongus':'1HP', 'amoongus':'2HP', 'frillish':'1SpD', 'jellicent':'2SpD', 'alomomola':'2HP', 'joltik':'1Spe', 'galvantula':'2Spe', 'ferroseed':'1Def', 'ferrothorn':'2Def', 'klink':'1Def', 'klang':'2Def', 'klinklang':'3Def', 'tynamo':'1Spe', 'elektrik':'2Atk', 'eelektross':'3Atk', 'elgyem':'1SpA', 'beheeyem':'2SpA', 'litwick':'1SpA', 'lampent':'2SpA', 'chandelure':'3SpA', 'axew':'1Atk', 'fraxure':'2Atk', 'haxorus':'3Atk', 'chubchoo':'1Atk', 'beartic':'2Atk', 'cryogonal':'2SpD', 'shelmet':'1Def', 'accelgor':'2Spe', 'stunfisk':'2HP', 'mienfoo':'1Atk', 'mienshao':'2Atk', 'druddigon':'2Atk', 'golett':'1Atk', 'golurk':'2Atk', 'pawniard':'1Atk', 'bisharp':'2Atk', 'bouffalant':'2Atk', 'rufflet':'1Atk', 'braviary':'2Atk', 'vullaby':'1Def', 'mandibuzz':'2SpA', 'heatmor':'2SpA', 'durant':'2Def', 'deino':'1Atk', 'zweilous':'2Atk', 'hydreigon':'3SpA', 'larvesta':'1Atk', 'volcarona':'3SpA', 'cobalion':'3Def', 'terrakion':'3Atk', 'virizion':'3SpD', 'tornadus':'3Atk', 'thundurus':'3Atk', 'reshiram':'3SpA', 'zekrom':'3Atk', 'landorus':'3SpA', 'kyurem':'1HP, 1Atk, 1SpA', 'keldeo':'3SpA', 'meloetta':'1SpA, 1SpD, 1Spe', 'genesect':'1Atk, 1SpA, 1Spe', 'chespin':'1Def', 'quilladin':'2Def', 'chesnaught':'3Def', 'fennekin':'1SpA', 'braixen':'2SpA', 'delphox':'3SpA', 'froakie':'1Spe', 'frogadier':'2Spe', 'greninja':'3Spe', 'bunnelby':'1Spe', 'diggersby':'2HP', 'fletchling':'1Spe', 'fletchinder':'2Spe', 'talonflame':'3Spe', 'scatterbug':'1Def', 'spewpa':'2Def', 'vivillon':'1HP, 1SpA, 1Spe', 'litleo':'1SpA', 'pyroar':'2SpA', 'flabebe':'1SpD', 'floette':'2SpD', 'florges':'3SpD', 'skiddo':'1HP', 'gogoat':'2HP', 'pancham':'1Atk', 'pangoro':'2Atk', 'furfrou':'1Spe', 'espurr':'1Spe', 'meowstic':'2Spe', 'honedge':'1Def', 'doublade':'2Def', 'aegislash':'2Atk, 1SpA', 'spritzee':'1HP', 'aromatisse':'2HP', 'swirlix':'1Def', 'slurpuff':'2Def', 'inkey':'1Atk', 'malamar':'2Atk', 'binacle':'1Atk', 'barbacle':'2Atk', 'skrepl':'1SpD', 'dragalge':'2SpD', 'clauncher':'1SpA', 'clawitzer':'2SpA', 'helioptile':'1Spe', 'tyrunt':'1Atk', 'tyrantrum':'2Atk', 'amaura':'1HP', 'aurorus':'2HP', 'sylveon':'2SpD', 'hawlucha':'2Atk', 'dedenne':'2Spe', 'carbink':'1Def, 1SpD', 'goomy':'1SpD', 'sliggoo':'2SpD', 'goodra':'3SpD', 'klefki':'1Def', 'phantump':'1Atk', 'trevenant':'2Atk', 'pumpkaboo':'1Def', 'gourgeist':'2Def', 'bergmite':'1Def', 'avalugg':'2Def', 'noibat':'1Spe', 'noivern':'2Spe', 'xerneas':'3HP', 'yveltal':'3HP', 'zygarde':'3HP', 'diancie':'1Def, 2SpD', 'hoopa':'3SpA', 'volcanion':'3SpA', 'rowlet':'1HP', 'dartrix':'2HP', 'decideueye':'3Atk', 'litten':'1Spe', 'torracat':'2Spe', 'incineroar':'3Atk', 'popplio':'1SpA', 'brionne':'2SpA', 'primarina':'3SpA', 'pikipek':'1Atk', 'trumbeak':'2Atk', 'toucannon':'3Atk', 'yungoos':'1Atk', 'gumshoos':'2Atk', 'grubbin':'1Atk', 'charjabug':'2Def', 'vikavolt':'3SpA', 'crabrawler':'1Atk', 'crabominable':'2Atk', 'oricorio':'2SpA', 'cutiefly':'1Spe', 'ribombee':'2Spe', 'rockruff':'1Atk', 'lycanroc':'2Atk', 'wighiwashi':'1HP', 'mareanie':'1Def', 'toxapex':'2Def', 'mudbray':'1Atk', 'mudsdale':'2Atk', 'dewpider':'1SpA', 'araquinid':'2SpA', 'fomantis':'1Atk', 'lurantis':'2Atk', 'morelull':'1SpD', 'shiinotic':'2SpD', 'salandit':'1Spe', 'salazze':'2Spe', 'stufful':'1Atk', 'bewear':'2Atk', 'bounsweet':'1HP', 'steenee':'2Spe', 'tsareena':'3Atk', 'comfey':'2SpD', 'oranguru':'2SpD', 'passimian':'2Atk', 'wimpod':'1Spe', 'golisopod':'2Def', 'sandygast':'1Def', 'palossand':'2Def', 'pyukumuku':'2SpD', 'type: null':'2HP', 'silvally':'3HP', 'minior':'1Def', 'komala':'2Atk', 'turtonator':'2Def', 'togedemaru':'2Atk', 'mimikyu':'2SpD', 'bruxish':'2Atk', 'drampa':'2SpA', 'dhelmise':'2Atk', 'jangmo-o':'1Def', 'hakamo-o':'2Def', 'kommo-o':'3Def', 'tapu koko':'3Spe', 'tapu lele':'3SpA', 'tapu bulu':'3Atk', 'tapu fini':'3SpD', 'cosmog':'1HP', 'cosmoem':'1Def, 1SpD', 'solgaleo':'3Atk', 'lunala':'3SpA', 'nihilego':'3SpD', 'buzzwole':'1Atk, 2Def', 'pheromosa':'3Spe', 'xurkitree':'3SpA', 'celesteela':'1Atk, 1Def, 1SpA', 'kartana':'3Atk', 'guzzlord':'3HP', 'necrozma':'1Atk, 2SpA', 'magearna':'3SpA', 'marshadow':'2Atk, 1Spe', 'poipole':'1Spe', 'naganadel':'3SpA', 'stakataka':'3Def', 'blacephalon':'3SpA', 'zeraora':'3Spe'}

pokemonphoto = {'bulbasaur':'https://pokemongolife.ru/p/Bulbasaur.png','ivysaur':'https://pokemongolife.ru/p/Ivysaur.png','venusaur':'https://pokemongolife.ru/p/Venusaur.png','charmander':'https://pokemongolife.ru/p/Charmander.png','charmeleon':'https://pokemongolife.ru/p/Charmeleon.png','Charizard':'https://pokemongolife.ru/p/Charizard.png','squirtle':'https://pokemongolife.ru/p/Squirtle.png','wartortle':'https://pokemongolife.ru/p/Wartortle.png','blastoise':'https://pokemongolife.ru/p/Blastoise.png','caterpie':'https://pokemongolife.ru/p/Caterpie.png','metapod':'https://pokemongolife.ru/p/Metapod.png','butterfree':'https://pokemongolife.ru/p/Butterfree.png','weedle':'https://pokemongolife.ru/p/Weedle.png','kakuna':'https://pokemongolife.ru/p/Kakuna.png','beedrill':'https://pokemongolife.ru/p/Beedrill.png','pidgey':'https://pokemongolife.ru/p/Pidgey.png','pidgeotto':'https://pokemongolife.ru/p/Pidgeotto.png','pidgeot':'https://pokemongolife.ru/p/Pidgeot.png','rattata':'https://pokemongolife.ru/p/Rattata.png','raticate':'https://pokemongolife.ru/p/Raticate.png','spearow':'https://pokemongolife.ru/p/Spearow.png','fearow':'https://pokemongolife.ru/p/Fearow.png','ekans':'https://pokemongolife.ru/p/Ekans.png','arbok':'https://pokemongolife.ru/p/Arbok.png','pikachu':'https://pokemongolife.ru/p/Pikachu.png','raichu':'https://pokemongolife.ru/p/Raichu.png','sandshrew':'https://pokemongolife.ru/p/Sandshrew.png','sandslash':'https://pokemongolife.ru/p/Sandslash.png','nidoran':'https://pokemongolife.ru/p/Nidoran-female.png','nidorino':'https://pokemongolife.ru/p/Nidorino.png','nidoqueen':'https://pokemongolife.ru/p/Nidoqueen.png','nidorino':'https://pokemongolife.ru/p/Nidorino.png','nidoking':'https://pokemongolife.ru/p/Nidoking.png','clefairy':'https://pokemongolife.ru/p/Clefairy.png','clefable':'https://pokemongolife.ru/p/Clefable.png','vulpix':'https://pokemongolife.ru/p/Vulpix.png','ninetales':'https://pokemongolife.ru/p/Ninetales.png','jugglypuff':'https://pokemongolife.ru/p/Jigglypuff.png','wigglypuff':'https://pokemongolife.ru/p/Wigglypuff.png','zubat':'https://pokemongolife.ru/p/Zubat.png','golbat':'https://pokemongolife.ru/p/Golbat.png','oddish':'https://pokemongolife.ru/p/Oddish.png','gloom':'https://pokemongolife.ru/p/Gloom.png','vileplume':'https://pokemongolife.ru/p/Vileplume.png','paras':'https://pokemongolife.ru/p/Paras.png','parasect':'https://pokemongolife.ru/p/Parasect.png','venonat':'https://pokemongolife.ru/p/Venonat.png','venomoth':'https://pokemongolife.ru/p/Venomoth.png','diglett':'https://pokemongolife.ru/p/Diglett.png','dugtrio':'https://pokemongolife.ru/p/Dugtrio.png','meowth':'https://pokemongolife.ru/p/Meowth.png','persian':'https://pokemongolife.ru/p/Persian.png','psyduck':'https://pokemongolife.ru/p/Psyduck.png','golduck':'https://pokemongolife.ru/p/Golduck.png','mankey':'https://pokemongolife.ru/p/Mankey.png','primeape':'https://pokemongolife.ru/p/Primeape.png','growlithe':'https://pokemongolife.ru/p/Growlithe.png','arcanine':'https://pokemongolife.ru/p/Arcanine.png','poliwag':'https://pokemongolife.ru/p/Poliwag.png','poliwhirl':'https://pokemongolife.ru/p/Poliwhirl.png','poliwrath':'https://pokemongolife.ru/p/Poliwrath.png','abra':'https://pokemongolife.ru/p/Abra.png','kadabra':'https://pokemongolife.ru/p/Kadabra.png','alakazam':'https://pokemongolife.ru/p/Alakazam.png','machop':'https://pokemongolife.ru/p/Machop.png','machoke':'https://pokemongolife.ru/p/Machoke.png','machamp':'https://pokemongolife.ru/p/Machamp.png','bellsprout':'https://pokemongolife.ru/p/Bellsprout.png','weepinbell':'https://pokemongolife.ru/p/Weepinbell.png','victreebel':'https://pokemongolife.ru/p/Victreebel.png','tentacool':'https://pokemongolife.ru/p/Tentacool.png','tentacruel':'https://pokemongolife.ru/p/Tentacruel.png','geodude':'https://pokemongolife.ru/p/Geodude.png','graveler':'https://pokemongolife.ru/p/Graveler.png','golem':'https://pokemongolife.ru/p/Golem.png','ponyta':'https://pokemongolife.ru/p/Ponyta.png','rapidash':'https://pokemongolife.ru/p/Rapidash.png','slowpoke':'https://pokemongolife.ru/p/Slowpoke.png','slowbro':'https://pokemongolife.ru/p/Slowbro.png','magnemite':'https://pokemongolife.ru/p/Magnemite.png','magnetone':'https://pokemongolife.ru/p/Magnetone.png','farfetchd':'https://pokemongolife.ru/p/Farfetch.png','doduo':'https://pokemongolife.ru/p/Doduo.png','dodrio':'https://pokemongolife.ru/p/Dodrio.png','seel':'https://pokemongolife.ru/p/Seel.png','dewgong':'https://pokemongolife.ru/p/Dewgong.png','grimer':'https://pokemongolife.ru/p/Grimer.png','muk':'https://pokemongolife.ru/p/Muk.png','shellder':'https://pokemongolife.ru/p/Shellder.png','cloyster':'https://pokemongolife.ru/p/Cloyster.png','gastly':'https://pokemongolife.ru/p/Gastly.png','haunter':'https://pokemongolife.ru/p/Haunter.png','gengar':'https://pokemongolife.ru/p/Gengar.png','onix':'https://pokemongolife.ru/p/Onix.png','drowzee':'https://pokemongolife.ru/p/Drowzee.png','hypno':'https://pokemongolife.ru/p/Hypno.png','krabby':'https://pokemongolife.ru/p/Krabby.png','kingler':'https://pokemongolife.ru/p/Kingler.png','voltorb':'https://pokemongolife.ru/p/Voltorb.png','electrode':'https://pokemongolife.ru/p/Electrode.png','exeggcute':'https://pokemongolife.ru/p/Exeggcute.png','exeggutor':'https://pokemongolife.ru/p/Exeggutor.png','cubone':'https://pokemongolife.ru/p/Cubone.png','marowak':'https://pokemongolife.ru/p/Marowak.png','hitmonlee':'https://pokemongolife.ru/p/Hitmonlee.png','hitmonchan':'https://pokemongolife.ru/p/Hitmonchan.png','lickitung':'https://pokemongolife.ru/p/Lickitung.png','koffing':'https://pokemongolife.ru/p/Koffing.png','weezing':'https://pokemongolife.ru/p/Weezing.png','rhyhorn':'https://pokemongolife.ru/p/Rhyhorn.png','rhydon':'https://pokemongolife.ru/p/Rhydon.png','chansey':'https://pokemongolife.ru/p/Chansey.png','tangela':'https://pokemongolife.ru/p/Tangela.png','kangaskhan':'https://pokemongolife.ru/p/Kangaskhan.png','horsea':'https://pokemongolife.ru/p/Horsea.png','seadra':'https://pokemongolife.ru/p/Seadra.png','goldeen':'https://pokemongolife.ru/p/Goldeen.png','seaking':'https://pokemongolife.ru/p/Seaking.png','staryu':'https://pokemongolife.ru/p/Staryu.png','starmie':'https://pokemongolife.ru/p/Starmie.png','mr.mime':'https://pokemongolife.ru/p/Mr-Mime.png','scyther':'https://pokemongolife.ru/p/Scyther.png','jynx':'https://pokemongolife.ru/p/Jynx.png','electabuzz':'https://pokemongolife.ru/p/Electabuzz.png','magmar':'https://pokemongolife.ru/p/Magmar.png','pinsir':'https://pokemongolife.ru/p/Pinsir.png','tauros':'https://pokemongolife.ru/p/Tauros.png','magikarp':'https://pokemongolife.ru/p/Magikarp.png','gyarados':'https://pokemongolife.ru/p/Gyarados.png','lapras':'https://pokemongolife.ru/p/Lapras.png','ditto':'https://pokemongolife.ru/p/Ditto.png','eevee':'https://pokemongolife.ru/p/Eevee.png','vaporeon':'https://pokemongolife.ru/p/Vaporeon.png','jolteon':'https://pokemongolife.ru/p/Jolteon.png','flareon':'https://pokemongolife.ru/p/Flareon.png','porygon':'https://pokemongolife.ru/p/Porygon.png','omanyte':'https://pokemongolife.ru/p/Omanyte.png','omastar':'https://pokemongolife.ru/p/Omastar.png','kabuto':'https://pokemongolife.ru/p/Kabuto.png','kabutops':'https://pokemongolife.ru/p/Kabutops.png','aerodactyl':'https://pokemongolife.ru/p/Aerodactyl.png','snorlax':'https://pokemongolife.ru/p/Snorlax.png','articuno':'https://pokemongolife.ru/p/Articuno.png','zapdos':'https://pokemongolife.ru/p/Zapdos.png','moltres':'https://pokemongolife.ru/p/Moltres.png','dratini':'https://pokemongolife.ru/p/Dratini.png','dragonair':'https://pokemongolife.ru/p/Dragonair.png','dragonite':'https://pokemongolife.ru/p/Dragonite.png','mewtwo':'https://pokemongolife.ru/p/Mewtwo.png','mew':'https://pokemongolife.ru/p/Mew.png','chikorita':'https://pokemongolife.ru/p/Chikorita.png','bayleef':'https://pokemongolife.ru/p/Bayleef.png','meganium':'https://pokemongolife.ru/p/Meganium.png','cyndaquil':'https://pokemongolife.ru/p/Cyndaquill.png','quilava':'https://pokemongolife.ru/p/Quilava.png','typhlosion':'https://pokemongolife.ru/p/Typhlosion.png','totodile':'https://pokemongolife.ru/p/Totodile.png','croconaw':'https://pokemongolife.ru/p/Croconaw.png','feraligatr':'https://pokemongolife.ru/p/Feraligatr.png','sentret':'https://pokemongolife.ru/p/Sentret.png','furret':'https://pokemongolife.ru/p/Furret.png','hoothoot':'https://pokemongolife.ru/p/Hoothoot.png','noctowl':'https://pokemongolife.ru/p/Noctowl.png','ledyba':'https://pokemongolife.ru/p/Ledyba.png','ledian':'https://pokemongolife.ru/p/Ledian.png','spinarak':'https://pokemongolife.ru/p/Spinarak.png','ariados':'https://pokemongolife.ru/p/Ariados.png','crobat':'https://pokemongolife.ru/p/Crobat.png','chinchou':'https://pokemongolife.ru/p/Chinchou.png','lanturn':'https://pokemongolife.ru/p/Lanturn.png','pichu':'https://pokemongolife.ru/p/Pichu.png','cleffa':'https://pokemongolife.ru/p/Cleffa.png','igglybuff':'https://pokemongolife.ru/p/Igglybuff.png','togepi':'https://pokemongolife.ru/p/Togepi.png','togetic':'https://pokemongolife.ru/p/Togetic.png','natu':'https://pokemongolife.ru/p/Natu.png','xatu':'https://pokemongolife.ru/p/Xatu.png','mareep':'https://pokemongolife.ru/p/Mareep.png','flaaffy':'https://pokemongolife.ru/p/Flaaffy.png','ampharos':'https://pokemongolife.ru/p/Ampharos.png','bellossom':'https://pokemongolife.ru/p/Bellossom.png','marill':'https://pokemongolife.ru/p/Marill.png','azumarill':'https://pokemongolife.ru/p/Azumarill.png','sudowoodoo':'https://pokemongolife.ru/p/Sudowoodoo.png','politoed':'https://pokemongolife.ru/p/Politoed.png','hoppip':'https://pokemongolife.ru/p/Hoppip.png','skiploom':'https://pokemongolife.ru/p/Skiploom.png','jumpluff':'https://pokemongolife.ru/p/Jumpluff.png','aipom':'https://pokemongolife.ru/p/Aipom.png','sunkern':'https://pokemongolife.ru/p/Sunkern.png','sunflora':'https://pokemongolife.ru/p/Sunflora.png','yanma':'https://pokemongolife.ru/p/Yanma}.png','wooper':'https://pokemongolife.ru/p/Wooper.png','quagsire':'https://pokemongolife.ru/p/Quagsire.png','espeon':'https://pokemongolife.ru/p/Espeon.png','umbreon':'https://pokemongolife.ru/p/Umbreon.png','murkrow':'https://pokemongolife.ru/p/Murkrow.png','slowking':'https://pokemongolife.ru/p/Slowking.png','misdreavus':'https://pokemongolife.ru/p/Misdreavus.png','unown':'https://pokemongolife.ru/p/Unown.png','wobbuffet':'https://pokemongolife.ru/p/Wobbuffet.png','girafarig':'https://pokemongolife.ru/p/Girafarig.png','pimeco':'https://pokemongolife.ru/p/Pimeco.png','forretress':'https://pokemongolife.ru/p/Forretress.png','dunsparce':'https://pokemongolife.ru/p/Dunsparce.png','gligar':'https://pokemongolife.ru/p/Gligar.png','steelix':'https://pokemongolife.ru/p/Steelix.png','snubbull':'https://pokemongolife.ru/p/Snubbull.png','granbull':'https://pokemongolife.ru/p/Granbull.png','qwillfish':'https://pokemongolife.ru/p/Qwillfish.png','scizor':'https://pokemongolife.ru/p/Scizor.png','shuckle':'','heracross':'https://pokemongolife.ru/p/Shuckle.png','sneasel':'https://pokemongolife.ru/p/Sneasel.png','teddiursa':'https://pokemongolife.ru/p/Teediursa.png','ursaring':'https://pokemongolife.ru/p/Ursaring.png','slugma':'https://pokemongolife.ru/p/Slugma.png','magcargo':'https://pokemongolife.ru/p/Magcargo.png','swinub':'https://pokemongolife.ru/p/Swinub.png','piloswine':'https://pokemongolife.ru/p/Piloswine.png','corsola':'https://pokemongolife.ru/p/Corsola.png','remoraid':'https://pokemongolife.ru/p/Remoraid.png','octillery':'https://pokemongolife.ru/p/Octillery.png','delibird':'https://pokemongolife.ru/p/Delibird.png','mantine':'https://pokemongolife.ru/p/Mantine.png','skarmory':'https://pokemongolife.ru/p/Skarmory.png','houndour':'https://pokemongolife.ru/p/Houndour.png','houndoom':'https://pokemongolife.ru/p/Houndoom.png','kingdra':'https://pokemongolife.ru/p/Kingdra.png','phanpy':'https://pokemongolife.ru/p/Phanpy.png','donphan':'https://pokemongolife.ru/p/Donphan.png','porygon2':'https://pokemongolife.ru/p/Porygon2.png','stantler':'https://pokemongolife.ru/p/Stanler.png','smeargle':'https://pokemongolife.ru/p/Smergle.png','tyrogue':'https://pokemongolife.ru/p/Tyrogue.png','hitmontop':'https://pokemongolife.ru/p/Hitmontop.png','smoochum':'https://pokemongolife.ru/p/Smoochum.png','elekid':'https://pokemongolife.ru/p/Elekid.png','magby':'https://pokemongolife.ru/p/Magby.png','miltank':'https://pokemongolife.ru/p/Miltank.png','blissey':'https://pokemongolife.ru/p/Blissey.png','raikou':'https://pokemongolife.ru/p/Raikou.png','entei':'https://pokemongolife.ru/p/Entei.png','suicune':'https://pokemongolife.ru/p/Suicune.png','larvitar':'https://pokemongolife.ru/p/Larvitar.png','pupitar':'https://pokemongolife.ru/p/Pupitar.png','tyranitar':'https://pokemongolife.ru/p/Tyranitar.png','lugia':'https://pokemongolife.ru/p/Lugia.png','ho-oh':'https://pokemongolife.ru/p/Ho-Oh.png','celebi':'https://pokemongolife.ru/p/Celebi.png','treecko':'https://pokemongolife.ru/p/Treecko.png','grovyle':'https://pokemongolife.ru/p/Grovyle.png','sceptile':'https://pokemongolife.ru/p/Sceptile.png','torchik':'https://pokemongolife.ru/p/Torchik.png','combusken':'https://pokemongolife.ru/p/Combusken.png','blaziken':'https://pokemongolife.ru/p/Blaziken.png','mudkip':'https://pokemongolife.ru/p/Mudkip.png','marshtomp':'https://pokemongolife.ru/p/Marshtomp.png','swampert':'https://pokemongolife.ru/p/Swampert.png','poochyena':'https://pokemongolife.ru/p/Poochyena.png','mightyena':'https://pokemongolife.ru/p/Mightyena.png','zigzagoon':'https://pokemongolife.ru/p/Zigzagoon.png','linoone':'https://pokemongolife.ru/p/Linoone.png','wurmple':'https://pokemongolife.ru/p/Wurmple.png','silcoon':'https://pokemongolife.ru/p/Silcoon.png','beautifly':'https://pokemongolife.ru/p/Beautifly.png','cascoon':'https://pokemongolife.ru/p/Cascoon.png','dustox':'https://pokemongolife.ru/p/Dustox.png','lotad':'https://pokemongolife.ru/p/Lotad.png','lombre':'https://pokemongolife.ru/p/Lombre.png','ludicolo':'https://pokemongolife.ru/p/Ludicolo.png','seedot':'https://pokemongolife.ru/p/Seedot.png','nuzleaf':'https://pokemongolife.ru/p/Nuzleaf.png','shiftry':'https://pokemongolife.ru/p/Shiftry.png','taillow':'https://pokemongolife.ru/p/Taillow.png','swellow':'https://pokemongolife.ru/p/Swellow.png','wingull':'https://pokemongolife.ru/p/Wingull.png','pelliper':'https://pokemongolife.ru/p/Pelliper.png','ralts':'https://pokemongolife.ru/p/Ralts.png','kirlia':'https://pokemongolife.ru/p/Kirlia.png','gardevoir':'https://pokemongolife.ru/p/Gardevoir.png','surskit':'https://pokemongolife.ru/p/Surskit.png','masquerain':'https://pokemongolife.ru/p/Masquerain.png','shroomish':'https://pokemongolife.ru/p/Shroomish.png','breeloom':'https://pokemongolife.ru/p/Breeloom.png','slakoth':'https://pokemongolife.ru/p/Slakoth.png','vigoroth':'https://pokemongolife.ru/p/Vigoroth.png','slaking':'https://pokemongolife.ru/p/Slaking.png','nincada':'https://pokemongolife.ru/p/Nincada.png','ninjask':'https://pokemongolife.ru/p/Ninjask.png','shedinja':'https://pokemongolife.ru/p/Shedinja.png','whismur':'https://pokemongolife.ru/p/Whismur.png','loudred':'https://pokemongolife.ru/p/Loudred.png','exploud':'https://pokemongolife.ru/p/Exploud.png','makuhita':'https://pokemongolife.ru/p/Makuhita.png','hariyama':'https://pokemongolife.ru/p/Hariyama.png','azurill':'https://pokemongolife.ru/p/Azurill.png','nosepass':'https://pokemongolife.ru/p/Nosepass.png','skitty':'https://pokemongolife.ru/p/Skitty.png','delcatty':'https://pokemongolife.ru/p/Delcatty.png','sableye':'https://pokemongolife.ru/p/Sableye.png','mawile':'https://pokemongolife.ru/p/Mawile.png','aron':'https://pokemongolife.ru/p/Aron.png','lairon':'https://pokemongolife.ru/p/Lairon.png','aggron':'https://pokemongolife.ru/p/Aggron.png','meditite':'https://pokemongolife.ru/p/Meditite.png','medicham':'https://pokemongolife.ru/p/Medicham.png','electrike':'https://pokemongolife.ru/p/Electrike.png','manectric':'https://pokemongolife.ru/p/Manectric.png','plusle':'https://pokemongolife.ru/p/Plusle.png','minun':'https://pokemongolife.ru/p/Minun.png','volbeat':'https://pokemongolife.ru/p/Volbeat.png','illumise':'https://pokemongolife.ru/p/Illumise.png','roselia':'https://pokemongolife.ru/p/Roselia.png','gulpin':'https://pokemongolife.ru/p/Gulpin.png','swalot':'https://pokemongolife.ru/p/Swalot.png','carvanha':'https://pokemongolife.ru/p/Carvanha.png','sharpedo':'https://pokemongolife.ru/p/Sharpedo.png','wailmer':'https://pokemongolife.ru/p/Wailmer.png','wailord':'https://pokemongolife.ru/p/Wailord.png','numel':'https://pokemongolife.ru/p/Numel.png','camerupt':'https://pokemongolife.ru/p/Camerupt.png','torkoal':'https://pokemongolife.ru/p/Torkoal.png','spoink':'https://pokemongolife.ru/p/Spoink.png','grumpig':'https://pokemongolife.ru/p/Grumpig.png','spinda':'https://pokemongolife.ru/p/Spinda.png','trapinch':'https://pokemongolife.ru/p/Trapinch.png','vibrava':'https://pokemongolife.ru/p/Vibrava.png','flygon':'https://pokemongolife.ru/p/Flygon.png','cacnea':'https://pokemongolife.ru/p/Cacnea.png','cacturne':'https://pokemongolife.ru/p/Cacturne.png','swablu':'https://pokemongolife.ru/p/Swablu.png','altaria':'https://pokemongolife.ru/p/Altaria.png','zangoose':'https://pokemongolife.ru/p/Zangoose.png','seviper':'https://pokemongolife.ru/p/Seviper.png','lunatone':'https://pokemongolife.ru/p/Lunatone.png','solrock':'https://pokemongolife.ru/p/Solrock.png','barboach':'https://pokemongolife.ru/p/Barboach.png','whiscash':'https://pokemongolife.ru/p/Whiscash.png','corphish':'https://pokemongolife.ru/p/Corphish.png','crawdaunt':'https://pokemongolife.ru/p/Crawdaunt.png','baltoy':'https://pokemongolife.ru/p/Baltoy.png','claydol':'https://pokemongolife.ru/p/Claydol.png','lileep':'https://pokemongolife.ru/p/Lileep.png','cradily':'https://pokemongolife.ru/p/Cradily.png','anorith':'https://pokemongolife.ru/p/Anorith.png','armaldo':'https://pokemongolife.ru/p/Armaldo.png','feebas':'https://pokemongolife.ru/p/Feebas.png','milotic':'https://pokemongolife.ru/p/Milotic.png','castform':'https://pokemongolife.ru/p/Castform.png','kecleon':'https://pokemongolife.ru/p/Kecleon.png','shuppet':'https://pokemongolife.ru/p/Shuppet.png','banette':'https://pokemongolife.ru/p/Banette.png','duskull':'https://pokemongolife.ru/p/Duskull.png','dusclops':'https://pokemongolife.ru/p/Dusclops.png','tropius':'https://pokemongolife.ru/p/Tropius.png','chimecho':'https://pokemongolife.ru/p/Chimecho.png','absol':'https://pokemongolife.ru/p/Absol.png','wynaut':'https://pokemongolife.ru/p/Wynaut.png','snorunt':'https://pokemongolife.ru/p/Snorunt.png','glalie':'https://pokemongolife.ru/p/Glalie.png','spheal':'https://pokemongolife.ru/p/Spheal.png','sealeo':'https://pokemongolife.ru/p/Sealeo.png','walrein':'https://pokemongolife.ru/p/Walrein.png','clamperl':'https://pokemongolife.ru/p/Clamperl.png','huntail':'https://pokemongolife.ru/p/Huntail.png','gorebyss':'https://pokemongolife.ru/p/Gorebyss.png','relicanth':'https://pokemongolife.ru/p/Relicanth.png','luvdisc':'https://pokemongolife.ru/p/Luvdisc.png','bagon':'https://pokemongolife.ru/p/Bagon.png','shelgon':'https://pokemongolife.ru/p/Shelgon.png','salamence':'https://pokemongolife.ru/p/Salamence.png','beldum':'https://pokemongolife.ru/p/Beldum.png','metang':'https://pokemongolife.ru/p/Metang.png','metagross':'https://pokemongolife.ru/p/Metagross.png','regirock':'https://pokemongolife.ru/p/Regirock.png','regice':'https://pokemongolife.ru/p/Regice.png','registeel':'https://pokemongolife.ru/p/Registeel.png','latias':'https://pokemongolife.ru/p/Latias.png','latios':'https://pokemongolife.ru/p/Latios.png','kyogre':'https://pokemongolife.ru/p/Kyogre.png','groudon':'https://pokemongolife.ru/p/Groudon.png','rayquaza':'https://pokemongolife.ru/p/Rayquaza.png','jirachi':'https://pokemongolife.ru/p/Jirachi.png','deoxys':'https://pokemongolife.ru/p/Deoxys.png','turtwig':'https://pokemongolife.ru/p/Turtwig.png','grotle':'https://pokemongolife.ru/p/Grotle.png','torterra':'https://pokemongolife.ru/p/Torterra.png','chimchar':'https://pokemongolife.ru/p/Chimchar.png','monferno':'https://pokemongolife.ru/p/Monferno.png','infernape':'https://pokemongolife.ru/p/Infernape.png','piplup':'https://pokemongolife.ru/p/Piplup.png','prinlup':'https://pokemongolife.ru/p/Prinlup.png','empoleon':'https://pokemongolife.ru/p/Empoleon.png','starly':'https://pokemongolife.ru/p/Starly.png','staravia':'https://pokemongolife.ru/p/Staravia.png','staraptor':'https://pokemongolife.ru/p/Staraptor.png','bidoof':'https://pokemongolife.ru/p/Bidoof.png','bibarel':'https://pokemongolife.ru/p/Bibarel.png','kricketot':'https://pokemongolife.ru/p/Kricketot.png','kricketune':'https://pokemongolife.ru/p/Kricketune.png','shinx':'https://pokemongolife.ru/p/Shinx.png','luxio':'https://pokemongolife.ru/p/Luxio.png','luxray':'https://pokemongolife.ru/p/Luxray.png','budew':'https://pokemongolife.ru/p/Budew.png','roserade':'https://pokemongolife.ru/p/Roserade.png','cranidos':'https://pokemongolife.ru/p/Cranidos.png','rampardos':'https://pokemongolife.ru/p/Rampardos.png','shieldon':'https://pokemongolife.ru/p/Shieldon.png','bastiodon':'https://pokemongolife.ru/p/Bastiodon.png','burmy':'https://pokemongolife.ru/p/Burmy.png','wormada':'https://pokemongolife.ru/p/Wormada.png','mothim':'https://pokemongolife.ru/p/Mothim.png','combee':'https://pokemongolife.ru/p/Combee.png','vespiqueen':'https://pokemongolife.ru/p/Vespiqueen.png','pachirisu':'https://pokemongolife.ru/p/Pachirisu.png','buizel':'https://pokemongolife.ru/p/Buizel.png','floatzel':'https://pokemongolife.ru/p/Floatzel.png','cherubi':'https://pokemongolife.ru/p/Cherubi.png','cherrim':'https://pokemongolife.ru/p/Cherrim.png','shellos':'https://pokemongolife.ru/p/Shellos.png','gastrodon':'https://pokemongolife.ru/p/Gastrodon.png','ambipom':'https://pokemongolife.ru/p/Ambipom.png','drifloon':'https://pokemongolife.ru/p/Drifloon.png','drifblim':'https://pokemongolife.ru/p/Drifblim.png','buneary':'https://pokemongolife.ru/p/Buneary.png','lopunny':'https://pokemongolife.ru/p/Lopunny.png','mismagius':'https://pokemongolife.ru/p/Mismagius.png','honchkrow':'https://pokemongolife.ru/p/Honchkrow.png','glameow':'https://pokemongolife.ru/p/Glameow.png','purugly':'https://pokemongolife.ru/p/Purugly.png','chingling':'https://pokemongolife.ru/p/Chingling.png','stunky':'https://pokemongolife.ru/p/Stunky.png','skuntank':'https://pokemongolife.ru/p/Skuntank.png','bronzor':'https://pokemongolife.ru/p/Bronzor.png','bonsly':'https://pokemongolife.ru/p/Bonsly.png','mimejr.':'https://pokemongolife.ru/p/Mime.png','happiny':'https://pokemongolife.ru/p/Happiny.png','chatot':'https://pokemongolife.ru/p/Chatot.png','spiritomb':'https://pokemongolife.ru/p/Spiritomb.png','gible':'https://pokemongolife.ru/p/Gible.png','gabite':'https://pokemongolife.ru/p/Gabite.png','garchomp':'https://pokemongolife.ru/p/Garchomp.png','munchlax':'https://pokemongolife.ru/p/Munchlax.png','riolu':'https://pokemongolife.ru/p/Riolu.png','lucario':'https://pokemongolife.ru/p/Lucario.png','hippopotas':'https://pokemongolife.ru/p/Hippopotas.png','hippodon':'https://pokemongolife.ru/p/Hippodon.png','skorupi':'https://pokemongolife.ru/p/Skorupi.png','drapion':'https://pokemongolife.ru/p/Drapion.png','croagunk':'https://pokemongolife.ru/p/Croagunk.png','toxicroak':'https://pokemongolife.ru/p/Toxicroak.png','carnivine':'https://pokemongolife.ru/p/Cranivine.png','finneon':'https://pokemongolife.ru/p/Finneon.png','lumineon':'https://pokemongolife.ru/p/Lumineon.png','mantyke':'https://pokemongolife.ru/p/Mantyke.png','snover':'https://pokemongolife.ru/p/Snover.png','abomasnow':'https://pokemongolife.ru/p/Abomasnow.png','weavile':'https://pokemongolife.ru/p/Weavile.png','magnezone':'https://pokemongolife.ru/p/Magnezone.png','licklicky':'https://pokemongolife.ru/p/Lickilicky.png','rhyperior':'https://pokemongolife.ru/p/Rhyperior.png','tangrowth':'https://pokemongolife.ru/p/Tangrowth.png','electivire':'https://pokemongolife.ru/p/Electivire.png','magmortar':'https://pokemongolife.ru/p/Magmortar.png','togekiss':'https://pokemongolife.ru/p/Togekiss.png','yanmega':'https://pokemongolife.ru/p/Yanmega.png','leafeon':'https://pokemongolife.ru/p/Leafeon.png','glaceon':'https://pokemongolife.ru/p/Glaceon.png','gliscor':'https://pokemongolife.ru/p/Gliscor.png','mamoswine':'https://pokemongolife.ru/p/Mamoswine.png','porygonz':'https://pokemongolife.ru/p/Porygon-Z.png','gallade':'https://pokemongolife.ru/p/Gallade.png','probopass':'https://pokemongolife.ru/p/Probopass.png','dusknoir':'https://pokemongolife.ru/p/Dusknoir.png','froslass':'https://pokemongolife.ru/p/Froslass.png','rotom':'https://pokemongolife.ru/p/Rotom.png','uxie':'https://pokemongolife.ru/p/Uxie.png','mespirit':'https://pokemongolife.ru/p/Mespirit.png','azelf':'https://pokemongolife.ru/p/Azelf.png','dialga':'https://pokemongolife.ru/p/Dialga.png','palkia':'https://pokemongolife.ru/p/Palkia.png','heatran':'https://pokemongolife.ru/p/Heatran.png','regigigas':'https://pokemongolife.ru/p/Regigigas.png','giratina':'https://pokemongolife.ru/p/Giratina.png','cresselia':'https://pokemongolife.ru/p/Cresselia.png','phione':'https://pokemongolife.ru/p/Phione.png','manaphy':'https://pokemongolife.ru/p/Manaphy.png','darkrai':'https://pokemongolife.ru/p/Darkrai.png','shaymin':'https://pokemongolife.ru/p/Shaymin.png','arceus':'https://pokemongolife.ru/p/Arceus.png','victini':'https://pokemongolife.ru/p/Victini.png','snivy':'https://pokemongolife.ru/p/Snivy.png','servine':'https://pokemongolife.ru/p/Servine.png','serperior':'https://pokemongolife.ru/p/Serperior.png','tepig':'https://pokemongolife.ru/p/Tepig.png','pignite':'https://pokemongolife.ru/p/Pignite.png','emboar':'https://pokemongolife.ru/p/Emboar.png','oshawott':'https://pokemongolife.ru/p/Oshawott.png','dewott':'https://pokemongolife.ru/p/Dewott.png','samurott':'https://pokemongolife.ru/p/Samurott.png','patrat':'https://pokemongolife.ru/p/Patrat.png','watchog':'https://pokemongolife.ru/p/Watchog.png','lillipup':'https://pokemongolife.ru/p/Lillipup.png','herdier':'https://pokemongolife.ru/p/Herdier.png','stoutland':'https://pokemongolife.ru/p/Stoutland.png','purrloin':'https://pokemongolife.ru/p/Purrloin.png','liepard':'https://pokemongolife.ru/p/Liepard.png','pansage':'https://pokemongolife.ru/p/Pansage.png','simisage':'https://pokemongolife.ru/p/Simisage.png','pansear':'https://pokemongolife.ru/p/Pansear.png','simisear':'https://pokemongolife.ru/p/Simisear.png','panpour':'https://pokemongolife.ru/p/Panpour.png','simipour':'https://pokemongolife.ru/p/Simipour.png','munna':'https://pokemongolife.ru/p/Munna.png','musharna':'https://pokemongolife.ru/p/Musharna.png','pidove':'https://pokemongolife.ru/p/Pidove.png','tranquill':'https://pokemongolife.ru/p/Tranquill.png','unfezant':'https://pokemongolife.ru/p/Unfezant.png','blitzle':'https://pokemongolife.ru/p/Blitzle.png','zebstrike':'https://pokemongolife.ru/p/Zebstrike.png','roggenrola':'https://pokemongolife.ru/p/Roggenrola.png','boldore':'https://pokemongolife.ru/p/Boldore.png','gigalith':'https://pokemongolife.ru/p/Gigalith.png','woobat':'https://pokemongolife.ru/p/Woobat.png','swoobat':'https://pokemongolife.ru/p/Swoobat.png','drilbur':'https://pokemongolife.ru/p/Drillbur.png','excadrill':'https://pokemongolife.ru/p/Excadrill.png','audino':'https://pokemongolife.ru/p/Audino.png','timburr':'https://pokemongolife.ru/p/Timburr.png','gurdurr':'https://pokemongolife.ru/p/Gurdurr.png','conkeldurr':'https://pokemongolife.ru/p/Conkeldurr.png','tympole':'https://pokemongolife.ru/p/Tympole.png','palpitoad':'https://pokemongolife.ru/p/Palpitoad.png','seismitoad':'https://pokemongolife.ru/p/Seismitoad.png','throh':'https://pokemongolife.ru/p/Throh.png','sawk':'https://pokemongolife.ru/p/Sawk.png','sewaddle':'https://pokemongolife.ru/p/Sewaddle.png','swadloon':'https://pokemongolife.ru/p/Swadloon.png','leavanny':'https://pokemongolife.ru/p/Leavanny.png','venipede':'https://pokemongolife.ru/p/Venipede.png','whirlipede':'https://pokemongolife.ru/p/Whirlepede.png','scolipede':'https://pokemongolife.ru/p/Scolipede.png','cottonee':'https://pokemongolife.ru/p/Cottonee.png','petilil':'https://pokemongolife.ru/p/Petilil.png','lilligant':'https://pokemongolife.ru/p/Lilligant.png','basculin':'https://pokemongolife.ru/p/Basculin.png','sandile':'https://pokemongolife.ru/p/Sandile.png','krokorok':'https://pokemongolife.ru/p/Krokorok.png','krookodile':'https://pokemongolife.ru/p/Krookodile.png','darumaka':'https://pokemongolife.ru/p/Darumaka.png','darmanitan':'https://pokemongolife.ru/p/Darmanitan.png','maractus':'https://pokemongolife.ru/p/Maractus.png','dwebble':'https://pokemongolife.ru/p/Dwebble.png','crustle':'https://pokemongolife.ru/p/Crustle.png','scraggy':'https://pokemongolife.ru/p/Scraggy.png','scrafty':'https://pokemongolife.ru/p/Scrafty.png','sigilyph':'https://pokemongolife.ru/p/Sigilyph.png','yamask':'https://pokemongolife.ru/p/Yamask.png','cofagrigus':'https://pokemongolife.ru/p/Cofagrigus.png','tirtouga':'https://pokemongolife.ru/p/Tirtouga.png','carracosta':'https://pokemongolife.ru/p/Carracosta.png','archen':'https://pokemongolife.ru/p/Archen.png','archeops':'https://pokemongolife.ru/p/Archeops.png','trubbish':'https://pokemongolife.ru/p/Trubbish.png','garbodor':'https://pokemongolife.ru/p/Garbodor.png','zorua':'https://pokemongolife.ru/p/Zorua.png','zoroark':'https://pokemongolife.ru/p/Zoroark.png','minccino':'https://pokemongolife.ru/p/Minccino.png','cinccino':'https://pokemongolife.ru/p/Cinccino.png','gothita':'https://pokemongolife.ru/p/Gothita.png','gothorita':'https://pokemongolife.ru/p/Gothorita.png','gothitelle':'https://pokemongolife.ru/p/Gothitelle.png','solosis':'https://pokemongolife.ru/p/Solosis.png','duosion':'https://pokemongolife.ru/p/Duosion.png','reuniclus':'https://pokemongolife.ru/p/Reuniclus.png','ducklett':'https://pokemongolife.ru/p/Ducklett.png','swanna':'https://pokemongolife.ru/p/Swanna.png','vanillite':'https://pokemongolife.ru/p/Vanillite.png','vanillish':'https://pokemongolife.ru/p/Vanillish.png','vanilluxe':'https://pokemongolife.ru/p/Vanilluxe.png','deerling':'https://pokemongolife.ru/p/Deerling.png','sawsbuck':'https://pokemongolife.ru/p/Sawsbuck.png','emolga':'https://pokemongolife.ru/p/Emolga.png','karrablast':'https://pokemongolife.ru/p/Karrablast.png','escavalier':'https://pokemongolife.ru/p/Escavalier.png','foongus':'https://pokemongolife.ru/p/Foongus.png','amoongus':'https://pokemongolife.ru/p/Amoongus.png','frillish':'https://pokemongolife.ru/p/Frillish.png','jellicent':'https://pokemongolife.ru/p/Jellicent.png','alomomola':'https://pokemongolife.ru/p/Alomomola.png','joltik':'https://pokemongolife.ru/p/Joltik.png','galvantula':'https://pokemongolife.ru/p/Galvantula.png','ferroseed':'https://pokemongolife.ru/p/Ferroseed.png','ferrothorn':'https://pokemongolife.ru/p/Ferrothorn.png','klink':'https://pokemongolife.ru/p/Klink.png','klang':'https://pokemongolife.ru/p/Klang.png','klinklang':'https://pokemongolife.ru/p/Klinkklang.png','tynamo':'https://pokemongolife.ru/p/Tynamo.png','elektrik':'https://pokemongolife.ru/p/Elektrik.png','eelektross':'https://pokemongolife.ru/p/Eelektross.png','elgyem':'https://pokemongolife.ru/p/Elgyem.png','beheeyem':'https://pokemongolife.ru/p/Beheeyem.png','litwick':'https://pokemongolife.ru/p/Litwick.png','lampent':'https://pokemongolife.ru/p/Lampent.png','chandelure':'https://pokemongolife.ru/p/Chandelure.png','axew':'https://pokemongolife.ru/p/Axew.png','fraxure':'https://pokemongolife.ru/p/Fraxure.png','haxorus':'https://pokemongolife.ru/p/Haxorus.png','chubchoo':'https://pokemongolife.ru/p/Chubchoo.png','beartic':'https://pokemongolife.ru/p/Beartic.png','cryogonal':'https://pokemongolife.ru/p/Cryogonal.png','shelmet':'https://pokemongolife.ru/p/Shelmet.png','accelgor':'https://pokemongolife.ru/p/Accelgor.png','stunfisk':'https://pokemongolife.ru/p/Stunfisk.png','mienfoo':'https://pokemongolife.ru/p/Mienfoo.png','mienshao':'https://pokemongolife.ru/p/Mienshao.png','druddigon':'https://pokemongolife.ru/p/Druddigon.png','golett':'https://pokemongolife.ru/p/Golett.png','golurk':'https://pokemongolife.ru/p/Golurk.png','pawniard':'https://pokemongolife.ru/p/Pawniard.png','bisharp':'https://pokemongolife.ru/p/Bisharp.png','bouffalant':'https://pokemongolife.ru/p/Bouffalant.png','rufflet':'https://pokemongolife.ru/p/Rufflet.png','braviary':'https://pokemongolife.ru/p/Braviary.png','vullaby':'https://pokemongolife.ru/p/Vullaby.png','mandibuzz':'https://pokemongolife.ru/p/Mandybuzz.png','heatmor':'https://pokemongolife.ru/p/Heatmor.png','durant':'https://pokemongolife.ru/p/Durant.png','deino':'https://pokemongolife.ru/p/Deino.png','zweilous':'https://pokemongolife.ru/p/Zweilous.png','hydreigon':'https://pokemongolife.ru/p/Hydreigon.png','larvesta':'https://pokemongolife.ru/p/Larvesta.png','volcarona':'https://pokemongolife.ru/p/Volcarona.png','cobalion':'https://pokemongolife.ru/p/Cobalion.png','terrakion':'https://pokemongolife.ru/p/Terrakion.png','virizion':'https://pokemongolife.ru/p/Virizion.png','tornadus':'https://pokemongolife.ru/p/Tornadus.png','thundurus':'https://pokemongolife.ru/p/Thundurus.png','reshiram':'https://pokemongolife.ru/p/Reshiram.png','zekrom':'https://pokemongolife.ru/p/Zekrom.png','landorus':'https://pokemongolife.ru/p/Landorus.png','kyurem':'https://pokemongolife.ru/p/Kyurem.png','keldeo':'https://pokemongolife.ru/p/Keldeo.png','meloetta':'https://pokemongolife.ru/p/Meloetta.png','genesect':'https://pokemongolife.ru/p/Genesect.png','chespin':'https://pokemongolife.ru/p/Chespin.png','quilladin':'https://pokemongolife.ru/p/Quilladin.png','chesnaught':'https://pokemongolife.ru/p/Chesnaught.png','fennekin':'https://pokemongolife.ru/p/Fennekin.png','braixen':'https://pokemongolife.ru/p/Braixen.png','delphox':'https://pokemongolife.ru/p/Delphox.png','froakie':'https://pokemongolife.ru/p/Froakie.png','frogadier':'https://pokemongolife.ru/p/Frogadier.png','greninja':'https://pokemongolife.ru/p/Greninja.png','bunnelby':'https://pokemongolife.ru/p/Bunnelby.png','diggersby':'https://pokemongolife.ru/p/Diggersby.png','fletchling':'https://pokemongolife.ru/p/Fletchling.png','fletchinder':'https://pokemongolife.ru/p/Fletchinder.png','talonflame':'https://pokemongolife.ru/p/Talonflame.png','scatterbug':'https://pokemongolife.ru/p/Scatterbug.png','spewpa':'https://pokemongolife.ru/p/Spewpa.png','vivillon':'https://pokemongolife.ru/p/Vivllon.png','litleo':'https://pokemongolife.ru/p/Litleo.png','pyroar':'https://pokemongolife.ru/p/Pyroar.png','flabebe':'https://pokemongolife.ru/p/Flabebe.png','floette':'https://pokemongolife.ru/p/Floette.png','florges':'https://pokemongolife.ru/p/Florges.png','skiddo':'https://pokemongolife.ru/p/Skiddo.png','gogoat':'https://pokemongolife.ru/p/Gogoat.png','pancham':'https://pokemongolife.ru/p/Pancham.png','pangoro':'https://pokemongolife.ru/p/Pangoro.png','furfrou':'https://pokemongolife.ru/p/Furfrou.png','espurr':'https://pokemongolife.ru/p/Espurr.png','meowstic':'https://pokemongolife.ru/p/Meowstic.png','honedge':'https://pokemongolife.ru/p/Honedge.png','doublade':'https://pokemongolife.ru/p/Doublade.png','aegislash':'https://pokemongolife.ru/p/Aegislash.png','spritzee':'https://pokemongolife.ru/p/Spritzee.png','aromatisse':'https://pokemongolife.ru/p/Aromatisse.png','swirlix':'https://pokemongolife.ru/p/Swirlix.png','slurpuff':'https://pokemongolife.ru/p/Slurpuff.png','inkey':'https://pokemongolife.ru/p/Inkey.png','malamar':'https://pokemongolife.ru/p/Malamar.png','binacle':'https://pokemongolife.ru/p/Binacle.png','barbacle':'https://pokemongolife.ru/p/Barbacle.png','skrepl':'https://pokemongolife.ru/p/Skrepl.png','dragalge':'https://pokemongolife.ru/p/Dragalge.png','clauncher':'https://pokemongolife.ru/p/Clauncher.png','clawitzer':'https://pokemongolife.ru/p/Clawitzer.png','helioptile':'https://pokemongolife.ru/p/Helioptile.png','tyrunt':'https://pokemongolife.ru/p/Tyrunt.png','tyrantrum':'https://pokemongolife.ru/p/Tyrantrum.png','amaura':'https://pokemongolife.ru/p/Amaura.png','aurorus':'https://pokemongolife.ru/p/Aurorus.png','sylveon':'https://pokemongolife.ru/p/Sylveon.png','hawlucha':'https://pokemongolife.ru/p/Hawlucha.png','dedenne':'https://pokemongolife.ru/p/Dedenne.png','carbink':'https://pokemongolife.ru/p/Carbink.png','goomy':'https://pokemongolife.ru/p/Goomy.png','sliggoo':'https://pokemongolife.ru/p/Sliggoo.png','goodra':'https://pokemongolife.ru/p/Goodra.png','klefki':'https://pokemongolife.ru/p/Klefki.png','phantump':'https://pokemongolife.ru/p/Phantump.png','trevenant':'https://pokemongolife.ru/p/Trevenant.png','pumpkaboo':'https://pokemongolife.ru/p/Pumpkaboo.png','gourgeist':'https://pokemongolife.ru/p/Gourgeist.png','bergmite':'https://pokemongolife.ru/p/Bergmite.png','avalugg':'https://pokemongolife.ru/p/Avalugg.png','noibat':'https://pokemongolife.ru/p/Noibat.png','noivern':'https://pokemongolife.ru/p/Noivern.png','xerneas':'https://pokemongolife.ru/p/Xerneas.png','yveltal':'https://pokemongolife.ru/p/Yveltal.png','zygarde':'https://pokemongolife.ru/p/Zygarde.png','diancie':'https://pokemongolife.ru/p/Diancie.png','hoopa':'https://pokemongolife.ru/p/Hoopa.png','volcanion':'http://pokeliga.com/pictures/sprites/SM_fansprites/P721sn.png','rowlet':'http://pokeliga.com/pictures/sprites/SM_fansprites/P722sn.png','dartrix':'http://pokeliga.com/pictures/sprites/SM_fansprites/P723sn.png','decideueye':'http://pokeliga.com/pictures/sprites/SM_fansprites/P724sn.png','litten':'http://pokeliga.com/pictures/sprites/SM_fansprites/P725sn.png','torracat':'http://pokeliga.com/pictures/sprites/SM_fansprites/P726sn.png','incineroar':'http://pokeliga.com/pictures/sprites/SM_fansprites/P727sn.png','popplio':'http://pokeliga.com/pictures/sprites/SM_fansprites/P728sn.png','brionne':'http://pokeliga.com/pictures/sprites/SM_fansprites/P729sn.png','primarina':'http://pokeliga.com/pictures/sprites/SM_fansprites/P730sn.png','pikipek':'http://pokeliga.com/pictures/sprites/SM_fansprites/P731sn.png','trumbeak':'http://pokeliga.com/pictures/sprites/SM_fansprites/P732sn.png','toucannon':'http://pokeliga.com/pictures/sprites/SM_fansprites/P733sn.png','yungoos':'http://pokeliga.com/pictures/sprites/SM_fansprites/P734sn.png','gumshoos':'http://pokeliga.com/pictures/sprites/SM_fansprites/P735sn.png','grubbin':'http://pokeliga.com/pictures/sprites/SM_fansprites/P736sn.png','charjabug':'http://pokeliga.com/pictures/sprites/SM_fansprites/P737sn.png','vikavolt':'http://pokeliga.com/pictures/sprites/SM_fansprites/P738sn.png','crabrawler':'http://pokeliga.com/pictures/sprites/SM_fansprites/P739sn.png','crabominable':'http://pokeliga.com/pictures/sprites/SM_fansprites/P740sn.png','oricorio':'http://pokeliga.com/pictures/sprites/SM_fansprites/P741_1sn.png','cutiefly':'http://pokeliga.com/pictures/sprites/SM_fansprites/P742sn.png','ribombee':'http://pokeliga.com/pictures/sprites/SM_fansprites/P743sn.png','rockruff':'http://pokeliga.com/pictures/sprites/SM_fansprites/P744sn.png','lycanroc':'http://pokeliga.com/pictures/sprites/SM_fansprites/P745_1sn.png','wighiwashi':'http://pokeliga.com/pictures/sprites/SM_fansprites/P746_1sn.png','mareanie':'http://pokeliga.com/pictures/sprites/SM_fansprites/P747sn.png','toxapex':'http://pokeliga.com/pictures/sprites/SM_fansprites/P748sn.png','mudbray':'http://pokeliga.com/pictures/sprites/SM_fansprites/P749sn.png','mudsdale':'http://pokeliga.com/pictures/sprites/SM_fansprites/P750sn.png','dewpider':'http://pokeliga.com/pictures/sprites/SM_fansprites/P751sn.png','araquinid':'http://pokeliga.com/pictures/sprites/SM_fansprites/P752sn.png','fomantis':'http://pokeliga.com/pictures/sprites/SM_fansprites/P753sn.png','lurantis':'http://pokeliga.com/pictures/sprites/SM_fansprites/P754sn.png','morelull':'http://pokeliga.com/pictures/sprites/SM_fansprites/P755sn.png','shiinotic':'http://pokeliga.com/pictures/sprites/SM_fansprites/P756sn.png','salandit':'http://pokeliga.com/pictures/sprites/SM_fansprites/P757sn.png','salazze':'http://pokeliga.com/pictures/sprites/SM_fansprites/P758sn.png','stufful':'http://pokeliga.com/pictures/sprites/SM_fansprites/P759sn.png','bewear':'http://pokeliga.com/pictures/sprites/SM_fansprites/P760sn.png','bounsweet':'http://pokeliga.com/pictures/sprites/SM_fansprites/P761sn.png','steenee':'http://pokeliga.com/pictures/sprites/SM_fansprites/P762sn.png','tsareena':'http://pokeliga.com/pictures/sprites/SM_fansprites/P763sn.png','comfey':'http://pokeliga.com/pictures/sprites/SM_fansprites/P764sn.png','oranguru':'http://pokeliga.com/pictures/sprites/SM_fansprites/P765sn.png','passimian':'http://pokeliga.com/pictures/sprites/SM_fansprites/P766sn.png','wimpod':'http://pokeliga.com/pictures/sprites/SM_fansprites/P767sn.png','golisopod':'http://pokeliga.com/pictures/sprites/SM_fansprites/P768sn.png','sandygast':'http://pokeliga.com/pictures/sprites/SM_fansprites/P769sn.png','palossand':'http://pokeliga.com/pictures/sprites/SM_fansprites/P770sn.png','pyukumuku':'http://pokeliga.com/pictures/sprites/SM_fansprites/P771sn.png','type:null':'http://pokeliga.com/pictures/sprites/SM_fansprites/P772sn.png','silvally':'http://pokeliga.com/pictures/sprites/SM_fansprites/P773_02sn.png','minior':'http://pokeliga.com/pictures/sprites/SM_fansprites/P774_1sn.png','komala':'http://pokeliga.com/pictures/sprites/SM_fansprites/P775sn.png','turtonator':'http://pokeliga.com/pictures/sprites/SM_fansprites/P776sn.png','togedemaru':'http://pokeliga.com/pictures/sprites/SM_fansprites/P777sn.png','mimikyu':'http://pokeliga.com/pictures/sprites/SM_fansprites/P778sn.png','bruxish':'http://pokeliga.com/pictures/sprites/SM_fansprites/P779sn.png','drampa':'http://pokeliga.com/pictures/sprites/SM_fansprites/P780sn.png','dhelmise':'http://pokeliga.com/pictures/sprites/SM_fansprites/P781sn.png','jangmo-o':'http://pokeliga.com/pictures/sprites/SM_fansprites/P782sn.png','hakamo-o':'http://pokeliga.com/pictures/sprites/SM_fansprites/P783sn.png','kommo-o':'http://pokeliga.com/pictures/sprites/SM_fansprites/P784sn.png','tapukoko':'http://pokeliga.com/pictures/sprites/SM_fansprites/P785sn.png','tapulele':'http://pokeliga.com/pictures/sprites/SM_fansprites/P786sn.png','tapubulu':'http://pokeliga.com/pictures/sprites/SM_fansprites/P787sn.png','tapufini':'http://pokeliga.com/pictures/sprites/SM_fansprites/P788sn.png','cosmog':'http://pokeliga.com/pictures/sprites/SM_fansprites/P789sn.png','cosmoem':'http://pokeliga.com/pictures/sprites/SM_fansprites/P790sn.png','solgaleo':'http://pokeliga.com/pictures/sprites/SM_fansprites/P791sn.png','lunala':'http://pokeliga.com/pictures/sprites/SM_fansprites/P792sn.png','nihilego':'http://pokeliga.com/pictures/sprites/SM_fansprites/P793sn.png','buzzwole':'http://pokeliga.com/pictures/sprites/SM_fansprites/P794sn.png','pheromosa':'http://pokeliga.com/pictures/sprites/SM_fansprites/P795sn.png','xurkitree':'http://pokeliga.com/pictures/sprites/SM_fansprites/P796.png','celesteela':'http://pokeliga.com/pictures/sprites/SM_fansprites/P797sn.png','kartana':'http://pokeliga.com/pictures/sprites/SM_fansprites/P798sn.png','guzzlord':'http://pokeliga.com/pictures/sprites/SM_fansprites/P799sn.png','necrozma':'http://pokeliga.com/pictures/sprites/SM_fansprites/P800sn.png','magearna':'http://pokeliga.com/pictures/sprites/SM_fansprites/P801sn.png','marshadow':'https://i.imgur.com/1sA436j.png','poipole':'https://i.imgur.com/zMnARjN.png','naganadel':'https://i.imgur.com/fr0BFsP.png','stakataka':'https://i.imgur.com/HGp8yuU.png','blacephalon':'https://i.imgur.com/Bpy4tm3.png','zeraora':'https://i.imgur.com/tcJnNBQ.png'}

evslist = {'hp': 'Nidoran♀, Slowpoke, Grimer, Vaporeon, Marill, Phanpy', 'atk': 'Ekans, Nidoran♂, Machop, Krabby, Kingler, Goldeen, Seaking, Larvitar, Poochyena, Trapinch, Corphish, Crawdaunt, Shinx, Sandile, Pawniard, Bisharp', 'def': 'Sandshrew, Geodude, Shellder, Onix, Cubone, Marowak, Magcargo, Pelipper, Bronzor, Skorupi, Sewaddle, Swadloon, Venipede, Klink, Klang', 'spa': 'Oddish, Psyduck, Golduck, Abra, Gastly, Slugma, Glaceon', 'spd': 'Tentacool, Tentacruel, Seel, Mantine, Duskull, Dewpider', 'spe': 'Rattata, Raticate, Pikachu, Zubat, Golbat, Diglett, Meowth, Poliwag, Poliwhirl, Ponyta, Staryu, Magikarp, Electrike, Pachirisu, Blitzle, Woobat, Swoobat, Froakie, Frogadier, Helioptile, Salandit, Salazzle'}

botstream = discord.Streaming(name = 'Say: -help', url = 'https://www.twitch.tv/alexfives')

topfact1 = 'Всегда ищите Starmie с природой Adamant. Это  лучшее, что может быть для него.:thumbsup:'
topfact2 = 'Против фей очень эффективно ставить драконов, так как фея, тип атаки которой схож с её типом (STAB-эффект), ничего не сделает Вашему покемону, а вот дракон наоборот нанесёт двойной урон.:ok_hand:'
topfact3 = 'Всегда пытайтесь найти Staraptor\'a с природой Modest. Ничего не может быть лучше!:thumbsup:'
topfact4 = 'Если против Вас стоит Primal Kyogre или Primal Groudon, то нет ничего лучше, кроме как бежать, ибо они не контрятся!:frowning2: '
topfact5 = 'Если Вы увидели у противника Donphan\'a 25lvl, то уходите из боя, ведь он, будьте уверены, багнут и в любом случае выживет с 1 хп, когда Ваш любимец погибнет!:crying_cat_face: '
topfact6 = 'Каждому известно, что нельзя стоять под деревом во время грозы, ведь, если молния ударит в дерево, оно мало того, что загорится:fire:, так ещё и окружающая его земля также получит заряд, который способен причинить Вам вред. Так к чему это я... Эффективно бить атакой электрического типа земляных покемонов.:warning: Это подтверждают законы физики!:heavy_check_mark: '
topfact7 = ''
topfact8 = ''
topfact9 = ''
topfact10 = ''





client = discord.Client()



async def mute_check():
    while True:
        with open('kvakepmutedmembers.txt', 'r') as fin:
            with open('kvakepmutedmembersnew.txt', 'w') as fout:
                for line in fin:
                    try:
                        Y = re.search(r'Время: \d{4}-', line)
                        Y = Y.group(0)
                        Y = Y[7:]
                        Y = Y.replace('-', '')
                        Y = int(Y)
                        M = re.search(r'Время: \d{4}-\d{2}-', line)
                        M = M.group(0)
                        M = M[12:]
                        M = M.replace('-', '')
                        M = int(M)
                        D = re.search(r'Время: \d{4}-\d{2}-\d{2} ', line)
                        D = D.group(0)
                        D = D[15:]
                        D = D.replace(' ', '')
                        D = int(D)
                        h = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:', line)
                        h = h.group(0)
                        h = h[18:]
                        h = h.replace(':', '')
                        h = int(h)
                        m = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:', line)
                        m = m.group(0)
                        m = m[21:]
                        m = m.replace(':', '')
                        m = int(m)
                        s = re.search(r'Время: \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
                        s = s.group(0)
                        s = s[24:]
                        s = int(s)

                        if datetime.datetime.today() > datetime.datetime(Y, M, D, h, m, s):
                            
                            guild = re.search(r'Сервер: \d{1,20};', line)
                            guild = guild.group(0)
                            guild = guild[8:]
                            guild = guild.replace(';', '')
                            guild = client.get_guild(int(guild))

                            member = re.search(r'Пользователь: \d{1,20};', line)
                            member = member.group(0)
                            member = member[14:]
                            member = member.replace(';', '')
                            member = guild.get_member(int(member))

                            unmute = discord.Embed(
                                title = 'Хорошая новость!',
                                description = 'С Вас был снят мут!',
                                color = discord.Color.gold()
                            )

                            for r in guild.roles:
                                if int(r.permissions.value) == 1049600:
                                    muterole = r
                                    break
                            else:
                                muterole = await guild.create_role(
                                    name = 'Muted',
                                    permissions = discord.Permissions(permissions = 1049600),
                                    color = discord.Color.dark_grey(),
                                    reason = 'Роль для мутов'
                                )
                            await member.remove_roles(muterole, reason = 'Unmute')
                            await member.send(embed = unmute)
                        else:
                            fout.write(line)
                    except:
                        pass
                fout.close()
            fin.close()
        try:
            os.remove('kvakepmutedmembers.txt')
            os.renames('kvakepmutedmembersnew.txt', 'kvakepmutedmembers.txt')
        except:
            pass
        await asyncio.sleep(10)



@client.event
async def on_ready():
    print('{0.user} is ready!'.format(client))
    print('----------')
    await client.change_presence(status=discord.Status.dnd, activity=botstream)
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(mute_check())



@client.event
async def on_message(message):

    msglower = message.content.lower()

    if message.author == client.user:
        return

    if msglower.startswith('-help'):
        await message.delete()
        embed=discord.Embed(title="**Help:**", description="Здесь Вы можете просмотреть список моих команд.", color=0x00ff80)
        embed.add_field(
            name='***-evs имя_покемона***',
            value='Показывает ЕВс, которые даёт покемон после убийства.',
            inline=True
        )
        embed.add_field(
            name='***-evs стат***',
            value='Показывает покемонов, которые дают данный стат после убийства.',
            inline=True
        )
        embed.add_field(
            name='***-flip***',
            value='Случайное подбрасывание монетки.',
            inline=True
        )
        embed.add_field(
            name='***-lovelist*** или ***-ll***',
            value='Выводит список любимых игроков по мнению kvakep\'a. `(roflan)`',
            inline=True
        )
        embed.add_field(
            name='***-topfact*** или ***-tf***',
            value='kvakep рассказывает "топовый" факт, к которому лучше не прислушиваться. `(roflan)`',
            inline=True
        )
        embed.add_field(
            name='***-avatar*** или ***-ava***',
            value='Показывает аватарку пользователя.',
            inline=True
        )
        embed.set_footer(
            text="made by Alex5555"
        )
        embed.set_thumbnail(
            url='https://i.imgur.com/PkP3JUE.png'
        )
        await message.channel.send(embed=embed)

    if msglower.startswith('-lovelist') or msglower.startswith('-ll'):
        await message.delete()
        embed=discord.Embed(title='***___Список любимых игроков сервера:___***', color=0x0a4a76)
        embed.add_field(
            name='wwwnekit',
            value='MaryFranc',
            inline=True
        )
        embed.add_field(
            name='fihid',
            value='Mephislofel',
            inline=True
        )
        embed.add_field(    
            name='Radells',
            value='Wwweter',
            inline=True
        )
        embed.add_field(
            name='kvakep',
            value='Be3yH4uK',
            inline=True
        )
        embed.add_field(
            name='hyper_44',
            value='Deepsy9',
            inline=True
        )
        embed.add_field(
            name='Hoochuu',
            value='BrOnYaShANyasha',
            inline=True
        )
        embed.set_footer(
            text='made by {}'.format(client.get_user(499284863686279201))
        )
        await message.channel.send(embed=embed)

    if msglower.startswith('-flip'):
        await message.delete()
        orel1 = client.get_emoji(596784734571593748)
        reshka1 = client.get_emoji(596784735758319619)
        orel = 'https://i.imgur.com/lKRzOJT.png'
        reshka = 'https://i.imgur.com/RLrFINV.png'
        color = discord.Color.teal()
        flip = random.choice([orel, reshka])
        if flip == orel:
            msg = 'Орёл'
            emoji = orel1
        else:
            msg = 'Решка'
            emoji = reshka1
        flp = discord.Embed(
            description = 'Выбор монеты: **{}**!'.format(msg),
            color = color
        )
        flp.set_thumbnail(url = flip)
        m = await message.channel.send(embed = flp)
        await m.add_reaction(emoji)
    
    if msglower.startswith('-evs'):
        
        pokemon = message.content.lower()
        pokemon = pokemon[5:]
        pokeurl = pokemonphoto.get(pokemon)
        p = pokemonlist.get(pokemon)
        e = evslist.get(pokemon)
        colour = random.choice([0xff8000, 0xffff00, 0x00ff00, 0x00ffff, 0x032ef8, 0x800080])
        await message.delete()

        if pokemon in pokemonlist:
            pokemon = pokemon.title()
            embed=discord.Embed(
                description='**—Pokemon: __{pokemon}__\n—Даёт __{ev}__ EV!**'.format(pokemon=pokemon, ev=p),
                color=colour
            )
            embed.set_thumbnail(
                url=pokeurl
            )
            embed.set_author(
                name='𝔼𝕍𝕤 𝕚𝕟𝕗𝕠: ',
                icon_url='https://i.imgur.com/treYwnd.png'
            )
            embed.set_footer(
                text='Requested by {}'.format(message.author),
                icon_url='https://i.imgur.com/PkP3JUE.png'
            )
            await message.channel.send(embed=embed)
            del(pokemon, p, e, pokeurl, colour)

        elif pokemon in evslist:
            pokemon = pokemon.title()

            embed=discord.Embed(
                description=('**—EV: __{ev}__**\n**—Дают: __{pok}__**'.format(ev=pokemon, pok=e)),
                color=colour
            )
            embed.set_author(
                name='𝔼𝕍𝕤 𝕚𝕟𝕗𝕠: ',
                icon_url='https://i.imgur.com/treYwnd.png'
            )
            embed.set_footer(
                text='Requested by {}'.format(message.author),
                icon_url='https://i.imgur.com/PkP3JUE.png'
            )
            embed.set_thumbnail(
                url='https://media1.giphy.com/media/NS7gPxeumewkWDOIxi/giphy.gif?cid=790b76115cefcfce634a33554df6fcf5&rid=giphy.gif'
            )
            await message.channel.send(embed=embed)

            del(pokemon, p, e, pokeurl, colour)

        else:
            del(pokemon, p, e, pokeurl, colour)
            embed=discord.Embed(title=':slight_frown: ', description='Не найдено!:astonished:', color=0xff0000)
            await message.channel.send(embed=embed)
    
    if msglower.startswith('-topfact') or msglower.startswith('-tf'):
        colour = random.choice([0xff0000, 0xff8000, 0xffff00, 0x00ff00, 0x00ffff, 0x032ef8, 0x800080])
        topfact = random.choice([topfact1, topfact2, topfact3, topfact4, topfact5, topfact6])
        topemb=discord.Embed(
            title='"Топ" факт!:thinking::thumbsup::ok_hand:',
            description=topfact,
            color=colour
        )
        topemb.set_footer(
            text='Подтверждено kvakep\'ом ✔'
        )
        await message.delete()
        await message.channel.send(embed=topemb)

    if msglower.startswith('-say'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            await message.delete()
            msg = message.content.split(' ', 1)
            myemojis = client.emojis
            for e in range(len(myemojis)):
                if myemojis[e].name in msg[1]:
                    emoji = myemojis[e]
                    msg[1] = msg[1].replace(':{}:'.format(emoji.name), str(emoji))
                    continue
            try:
                say = msg[1]
                semb = discord.Embed(
                    description = say,
                    color = 0x00ff00
                )
                await message.channel.send(embed = semb)
            except:
                await message.channel.send('Используйте: -say [message]', delete_after = 15)               

    if msglower.startswith('-whisper'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            whisper = message.content.split(' ', 2)
            await message.delete()
            whisper[1] = whisper[1].replace('<', '')
            whisper[1] = whisper[1].replace('>', '')
            whisper[1] = whisper[1].replace('@', '')
            member = message.guild.get_member(int(whisper[1]))
            myemojis = client.emojis
            for e in range(len(myemojis)):
                if myemojis[e].name in whisper[2]:
                    emoji = myemojis[e]
                    whisper[2] = whisper[2].replace(':{}:'.format(emoji.name), str(emoji))
                    continue
            try:
                msg = whisper[2]
                await member.send(msg)
            except:
                await message.channel.send('Используйте: -whisper [@member/member_id] [message]', delete_after = 15)

    if msglower.startswith('-ava'):
        colour = random.choice([0xff0000, 0xff8000, 0xffff00, 0x00ff00, 0x00ffff, 0x032ef8, 0x800080])
        msg = message.content.split(' ')
        await message.delete()
        try:
            msg[1] = msg[1].replace('<', '')
            msg[1] = msg[1].replace('>', '')
            msg[1] = msg[1].replace('@', '')
            member = message.guild.get_member(int(msg[1]))
        except:
            await message.channel.send('Используйте: -ava [@member/member_id]', delete_after = 15)
        img = member.avatar_url
        ava = discord.Embed(
            description = '***Аватар пользователя {0.name}***'.format(member),
            color = colour
        )
        ava.set_image(url = img)
        ava.set_footer(text = 'Requested by {}'.format(message.author),
            icon_url = 'https://i.imgur.com/Ojia4Ni.png'
        )
        await message.channel.send(embed = ava)

    if msglower.startswith('-kick'):
        if message.author.guild_permissions.kick_members or message.author.id == 400231667408699392:
            await message.delete()
            try:
                msg = message.content.split(' ')

                try:
                    member = msg[1]
                    member = member.replace('', '')
                    member = member.replace('', '')
                    member = member.replace('', '')
                    member = int(member)
                    member = message.guild.get_member(member)
                except:
                    await message.channel.send('Используйте: -kick [@member/member_id] ([reason])', delete_after = 15)
                    return
                
                try:
                    reason = msg[2]
                except:
                    reason = ''
                
                kvakeplogs = discord.CategoryChannel
                overwrites = {
                    message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                    message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
                }
                for cat in message.guild.categories:
                    if cat.name == 'kvakep-logs':
                        kvakeplogs = cat
                        break
                else:
                    kvakeplogs = await message.guild.create_category_channel(
                        name = 'kvakep-logs',
                        overwrites = overwrites,
                        reason = 'Category for kvakep\'s logs'
                    )
                for chan in kvakeplogs.channels:
                    if chan.name == 'kicks':
                        kickslog = chan
                        break
                else:
                    kickslog = await kvakeplogs.create_text_channel(
                        name = 'kicks',
                        overwrites = overwrites,
                        reason = 'Channel for kvakep\'s kicks'
                    )

                if message.author.guild_permissions.administrator:
                    kickauthor = 'администратором'
                else:
                    kickauthor = 'модератором'

                if reason != '':
                    tologs = discord.Embed(
                        description = 'Пользователь {} был исключён {} {}.\nПричина: {}'.format(member, kickauthor, message.author, reason),
                        color = discord.Color.dark_grey()
                    )
                    tomember = discord.Embed(
                        description = 'Вы были исключены {} {}.\nПричина: {}'.format(kickauthor, message.author, reason)
                    )
                    await message.guild.kick(member, reason = 'Исключён: {} {}\nПричина: {}'.format(kickauthor, message.author, reason))
                else:
                    tologs = discord.Embed(
                        description = 'Пользователь {} был исключён {} {}.'.format(member, kickauthor, message.author),
                        color = discord.Color.dark_grey()
                    )
                    tomember = discord.Embed(
                        description = 'Вы были исключены {} {}.'.format(kickauthor, message.author)
                    )
                    await message.guild.kick(member, reason = 'Исключён: {} {}'.format(kickauthor, message.author))
                
                invitation = await message.channel.create_invite(max_uses = 1, reason = 'After kick')

                
                await message.channel.send('Пользователь {} был успешно исключён! :white_check_mark:'.format(member), delete_after = 15)
                await kickslog.send(embed = tologs)
                await member.send(content = invitation.url, embed = tomember)
            except:
                await message.channel.send('Вы не можете исключить данного пользователя!', delete_after = 15)
        else:
            await message.channel.send('У Вас недостаточно прав!', delete_after = 15)

    if msglower.startswith('-purge') or msglower.startswith('-clear'):
        if message.author.guild_permissions.manage_messages or message.author.id == 400231667408699392:
            param = message.content.split(' ', 2)
            quantity = int(param[1])
            await message.delete()
            if quantity <= 100:
                if len(param) < 2:
                    await message.channel.send('Искользуйте: -purge [количество сообщений(не более 100)]', delete_after = 15)
                else:
                    trash = discord.Embed(
                        description = 'Выполняется очистка...',
                        color = 0x246f58
                    )
                    trash.set_image(url = 'https://i.imgur.com/mMrEVUW.gif')
                    purge = discord.Embed(
                        description = ':white_check_mark: Успешно удалено последних сообщений: **{}**'.format(quantity),
                        color = 0x246f58
                    )
                    purge.set_thumbnail(url = 'https://i.imgur.com/pm0FS6X.png')
                    await message.channel.send(embed = trash, delete_after = 2)
                    await asyncio.sleep(3)
                    await message.channel.purge(limit = quantity)
                    await message.channel.send(embed = purge, delete_after = 15)   
            else:
                await message.delete()
                await message.channel.send('Количество сообщений превышает 100!', delete_after = 15)
        else:
            await message.delete()
            await message.channel.send('Вы не имеете прав на удаление сообщений!', delete_after = 15)
    
    if msglower.startswith('-roles'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            roles = message.guild.roles
            lenroles = len(roles)
            msg = ''
            for i in range(lenroles):
                msg += '{}\n'.format(roles[i])
            await message.delete()
            await message.author.send('{}:\n{}'.format(message.guild, msg))

    if msglower.startswith('-guilds'):
        if message.author.id == 400231667408699392:
            await message.delete()
            guilds = client.guilds
            guildslen = len(guilds)
            msg = ''
            for g in range(guildslen):
                msg += '{}\n'.format(guilds[g])
            await message.author.send('Список серверов:\n{}'.format(msg))
        else:
            pass

    if msglower.startswith('-groles'):
        if message.author.id == 400231667408699392:
            msg = message.content.split(' ', 1)
            if len(msg) != 2:
                await message.author.send('Используйте: -groles [guild]')
            else:
                guilds = client.guilds
                guildslen = len(guilds)
                for g in range(guildslen):
                    if msg[1] == str(guilds[g]):
                        roles = guilds[g].roles
                        lenroles = len(roles)
                        msg = ''
                        for r in range(len(roles)):
                            msg += '{}\n'.format(roles[r])
                        await message.author.send('Роли сервера {}:\n{}'.format(guilds[g], msg))
                        break
                else:
                    await message.author.send('Сервер не найден!', delete_after = 15)
        else:
            pass

    if msglower.startswith('-serverinfo'):
        await message.delete()

        name = message.guild

        large = message.guild.member_count

        owner = message.guild.owner

        created = message.guild.created_at.date()
        year = created.year
        month = created.month
        if month == 1:
            month = 'января'
        elif month == 2:
            month = 'февраля'
        elif month == 3:
            month = 'марта'
        elif month == 4:
            month = 'апреля'
        elif month == 5:
            month = 'мая'
        elif month == 6:
            month = 'июня'
        elif month == 7:
            month = 'июля'
        elif month == 8:
            month = 'августа'
        elif month == 9:
            month = 'сентября'
        elif month == 10:
            month = 'октября'
        elif month == 11:
            month = 'ноября'
        elif month == 12:
            month = 'декабря'
        day = created.day

        roles = len(message.guild.roles)

        icon = message.guild.icon_url

        text_channels = len(message.guild.text_channels)
        voice_channels = len(message.guild.voice_channels)
        channels = text_channels + voice_channels
        nsfw = 0
        news = 0
        for t in range(len(message.guild.text_channels)):
            if message.guild.text_channels[t].is_nsfw():
                nsfw += 1
            if message.guild.text_channels[t].is_news():
                news += 1

        emojis = len(message.guild.emojis)
        animated_emojis = 0
        for e in range(len(message.guild.emojis)):
            if message.guild.emojis[e].animated:
                animated_emojis += 1
        common_emojis = emojis - animated_emojis

        region = str(message.guild.region).title()

        verification = message.guild.verification_level
        if str(verification) == 'none':
            verification = 'Отсутствует'
        elif str(verification) == 'low':
            verification = 'Низкий'
        elif str(verification) == 'medium':
            verification  = 'Средний'
        elif str(verification) == 'high':
            verification = 'Высокий'
        elif str(verification) == 'extreme':
            verification = 'Высочайший'

        online_member = client.get_emoji(596453205341241355)
        idle_member = client.get_emoji(596453234227413031)
        dnd_member = client.get_emoji(596453249712652308)
        offline_member = client.get_emoji(596453263927279729)
        bot_member = client.get_emoji(596680939401117707)
        membersonguild = ''
        online = 0
        idle = 0
        dnd = 0
        offline = 0
        bot = 0
        for m in range(len(message.guild.members)):
            if message.guild.members[m].status == discord.Status.online:
                online += 1
            elif message.guild.members[m].status == discord.Status.idle:
                idle += 1
            elif message.guild.members[m].status == discord.Status.dnd:
                dnd += 1
            elif message.guild.members[m].status == discord.Status.offline:
                offline += 1
            if message.guild.members[m].bot:
                bot += 1

        info = discord.Embed(
            description = 'Информация о сервере: ',
            color = 0xfcb803
        )
        info.add_field(
            name = '**Название:**',
            value = name
        )
        info.add_field(
            name = '**Регион: **',
            value = region
        )
        info.add_field(
            name = '**Создатель: **',
            value = owner.mention
        )
        info.add_field(
            name = '**Создан: **',
            value = '{} {} {}'.format(day, month, year)
        )
        info.add_field(
            name = '**Каналов: **',
            value = 'Всего: {}\nТекстовых: {}\n  NSFW: {}\n  News: {}\nГолосовых: {}'.format(channels, text_channels, nsfw, news, voice_channels)
        )
        info.add_field(
            name = '**Участников: **',
            value = 'Всего: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}'.format(large, online_member, online, idle_member, idle, dnd_member, dnd, offline_member, offline, bot_member, bot)
        )
        info.add_field(
            name = '**Количество ролей: **',
            value = roles
        )
        info.add_field(
            name = '**Эмодзи: **',
            value = 'Всего: {}\nОбычных: {}\nАнимированных: {}'.format(emojis, common_emojis, animated_emojis)
        )
        info.add_field(
            name = '**Уровень проверки: **',
            value = verification
        )
        info.set_thumbnail(url = icon)
        await message.channel.send(embed = info)

    if msglower.startswith('-addreac') and message.author.id == 400231667408699392:
        msg = message.content.split(' ')
        await message.delete()
        if len(msg) < 3:
            await message.channel.send('Используйте: -addreac [message_id] [emoji]', delete_after = 15)
        else:
            msg[2] = msg[2].replace(':', '')
            emo = client.emojis
            for e in range(len(emo)):
                emoji = emo[e]
                if msg[2] in str(emoji):
                    break
            else:
                emoji = msg[2]
            msghistory = await message.channel.history(limit = 100).flatten()
            for m in range(len(msghistory)):
                if int(msg[1]) == msghistory[m].id:
                    msg = msghistory[m]
                    break
            else:        
                await message.channel.send('Сообщение не найдено!', delete_after = 15)
                return
            try:
                await msg.add_reaction(emoji)
            except discord.errors.HTTPException:
                emoji = emoji.replace(':', '')
                try:
                    await msg.add_reaction(emoji)
                except discord.errors.HTTPException:
                    await message.channel.send('Эмодзи не найдено!', delete_after = 15)
            
    if msglower.startswith('-delreacts') and message.author.id == 400231667408699392:
        msg = message.content.split(' ')
        await message.delete()
        if len(msg) != 2:
            await message.channel.send('Используйте: -delreacts [message_id]', delete_after = 15)
        else:
            msghistory = await message.channel.history(limit = 100).flatten()
            for m in range(len(msghistory)):
                if int(msg[1]) == msghistory[m].id:
                    msg = msghistory[m]
                    break
            else:
                await message.channel.send('Сообщение не найдено!', delete_after = 15)
                return
            await msg.clear_reactions()

    if msglower.startswith('-resend'):
        if message.author.guild_permissions.administrator or message.author.id == 400231667408699392:
            mes = message.content.split(' ', 2)
            index = mes[1]
            await message.delete()
            if len(mes) < 2:
                await message.channel.send('Используйте: -resend [message_id] ([comment])', delete_after = 15)
            else:
                msg = discord.Message
                msghistory = await message.channel.history(limit = 1000).flatten()
                for m in range(len(msghistory)):
                    if int(index) == msghistory[m].id:
                        msg = msghistory[m]
                        break
                else:
                    await message.channel.send('Сообщение не найдено!', delete_after = 15)
                    return
                year = msg.created_at.year
                month = msg.created_at.month
                if month == 1:
                    month = 'января'
                elif month == 2:
                    month = 'февраля'
                elif month == 3:
                    month = 'марта'
                elif month == 4:
                    month = 'апреля'
                elif month == 5:
                    month = 'мая'
                elif month == 6:
                    month = 'июня'
                elif month == 7:
                    month = 'июля'
                elif month == 8:
                    month = 'августа'
                elif month == 9:
                    month = 'сентября'
                elif month == 10:
                    month = 'октября'
                elif month == 11:
                    month = 'ноября'
                elif month == 12:
                    month = 'декабря'
                day = msg.created_at.day
                hour = msg.created_at.hour + 3
                if hour > 23:
                    hour -= 24
                if hour == 0:
                    hour = '00'
                elif hour == 1:
                    hour = '01'
                elif hour == 2:
                    hour = '02'
                elif hour == 3:
                    hour = '03'
                elif hour == 4:
                    hour = '04'
                elif hour == 5:
                    hour = '05'
                elif hour == 6:
                    hour = '06'
                elif hour == 7:
                    hour = '07'
                elif hour == 8:
                    hour = '08'
                elif hour == 9:
                    hour = '09'
                minute = msg.created_at.minute
                if minute == 0:
                    minute = '00'
                elif minute == 1:
                    minute = '01'
                elif minute == 2:
                    minute = '02'
                elif minute == 3:
                    minute = '03'
                elif minute == 4:
                    minute = '04'
                elif minute == 5:
                    minute = '05'
                elif minute == 6:
                    minute = '06'
                elif minute == 7:
                    minute = '07'
                elif minute == 8:
                    minute = '08'
                elif minute == 9:
                    minute = '09'
                created = '{} {} {} в {}:{}'.format(day, month, year, hour, minute)
                embed = message.embeds
                if len(embed) != 0:
                    embed = embed[0].copy()
                    await message.channel.send(content = '{}\n{}'.format(msg.author, created),embed = embed)
                else:
                    if len(mes) > 2:
                        resend = discord.Embed(
                            description = msg.content,
                            color = 0x800080
                        )
                        resend.set_author(
                            name = '{}        {}'.format(msg.author, created),
                            icon_url = msg.author.avatar_url,
                            url = msg.jump_url
                        )
                        await message.channel.send(embed = resend, content = mes[2])
                    else:
                        resend = discord.Embed(
                            description = msg.content,
                            color = 0x800080
                        )
                        resend.set_author(
                            name = '{}        {}'.format(msg.author, created),
                            icon_url = msg.author.avatar_url,
                            url = msg.jump_url
                        )
                        await message.channel.send(embed = resend)

    """if msglower.startswith('-wrembed') and message.author.id == 400231667408699392:
        msg = message.content.split(' ', 2)
        author = msg[1]
        try:
            author = author.replace('<', '')
            author = author.replace('@', '')
            author = author.replace('>', '')
            author = int(author)
            author = client.get_user(author)
        except:
            pass
        try:
            img = author.avatar_url
        except:
            img = 'https://i.imgur.com/9aT6cF9.png'
        await message.delete()
        if len(msg) != 3:
            await message.channel.send('Используйте: -writeas [author] [message]')
        else:
            write = discord.Embed(
                description = msg[2],
                color = 0xd6750a
            )
            write.set_author(
                name = '{}:'.format(author),
                icon_url = img
            )
            await message.channel.send(embed = write)"""

    if msglower.startswith('-myemo') and message.author.id == 400231667408699392:
        content = message.content.split(' ', 1)
        await message.delete()
        emojinames = []
        emojipics = []
        emojis = client.emojis
        emojilist = []
        global myemojismsg, embedlist, emojiindex
        myemojismsg = discord.Message
        embedlist = []
        emojiindex = 0
        name = ''
        msg = ''
        for i in range(len(emojis)):
            name = str(emojis[i]).split(':', 2)
            name = name[1]
            name = name.replace('*', '\*')
            name = name.replace('`', '\`')
            name = name.replace('_', '\_')
            name = name.replace('~', '\~')
            name = name.replace('|', '\|')
            name = name.replace('<', '\<')
            name = name.replace('>', '\>')
            emojinames.append(name)
            emojipics.append(emojis[i])
        for e in range(len(emojinames)):
            msg += '{} - {}\n'.format(emojinames[e], emojipics[e])
            if e % 20 == 0 and e != 0:
                emojilist.append(msg)
                msg = ''
                continue
        if msg == '':
            pass
        else:   
            emojilist.append(msg)
        for i in range(len(emojilist)):
            emojiembed = discord.Embed(
                name = 'Мои эмодзи: ',
                description = emojilist[i],
                color = 0x704b60
            )
            emojiembed.set_author(
                name = 'Страница #{}'.format(i+1),
                icon_url = 'https://i.imgur.com/EuR39pj.gif'
            )
            emojiembed.set_footer(
                text = 'Всего {} эмодзи'.format(len(emojis)),
                icon_url = client.user.avatar_url
            )
            embedlist.append(emojiembed)
        if len(content) == 2:
            if 'all' in content[1]:
                for i in range(len(embedlist)):
                    await message.author.send(embed = embedlist[i])
            elif 'count' in content[1]:
                count = len(client.emojis)
                await message.channel.send('У меня имеется {} эмодзи!'.format(count), delete_after = 20)
            else:
                await message.channel.send('Используйте: -myemo ([all/count])', delete_after = 15)
        else:
            myemojismsg = await message.channel.send(embed = embedlist[0])
            await myemojismsg.add_reaction('◀')
            await myemojismsg.add_reaction('▶')

    if msglower.startswith('-giverole'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 2)
            await message.delete()
            try:
                role = msg[2]
                role = role.replace('@', '')
                role = role.replace('&', '')
                role = role.replace('>', '')
                role = role.replace('<', '')
            except:
                await message.channel.send('Используйте: -giverole [@member/member_id] [@role/role_id]', delete_after = 15)
                return
            member = msg[1]
            member = member.replace('<', '')
            member = member.replace('>', '')
            member = member.replace('@', '')
            for r in range(len(message.guild.roles)):
                if role == str(message.guild.roles[r]):
                    role = message.guild.roles[r]
                    break
            else:
                for r in range(len(message.guild.roles)):
                    if int(role) == message.guild.roles[r].id:
                        role = message.guild.roles[r]
                        break
                else:
                    await message.channel.send('Роль не найдена!', delete_after = 15)
                    return
            try:
                member = message.guild.get_member(int(member))
                await member.add_roles(role, reason = message.content)
                await message.channel.send('Роль {} успешно добавлена пользователю {}!'.format(role, member), delete_after = 15)
            except:
                await message.channel.send('Пользователь не найден!', delete_after = 15)

    if msglower.startswith('-delrole'):
        if message.author.guild_permissions.manage_roles or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 2)
            await message.delete()
            try:
                role = msg[2]
                role = role.replace('@', '')
                role = role.replace('&', '')
                role = role.replace('>', '')
                role = role.replace('<', '')
            except:
                await message.channel.send('Используйте: -delrole [@member/member_id] [@role/role_id]', delete_after = 15)
                return
            member = msg[1]
            member = member.replace('<', '')
            member = member.replace('>', '')
            member = member.replace('@', '')
            for r in range(len(message.guild.roles)):
                if role == str(message.guild.roles[r]):
                    role = message.guild.roles[r]
                    break
            else:
                await message.channel.send('Роль не найдена!', delete_after = 15)
                return
            try:
                member = message.guild.get_member(int(member))
                await member.remove_roles(role, reason = message.content)
                await message.channel.send('Роль {} успешно снята с пользователя {}!'.format(role, memberid), delete_after = 15)
            except:
                await message.channel.send('Пользователь не найден!', delete_after = 15)

    if msglower.startswith('-perms') and message.author.id == 400231667408699392:
        msg = message.content.split(' ')
        await message.delete()
        member = message.guild.get_member(int(msg[1]))
        perms = []
        perms.append(member)
        if member.guild_permissions.administrator:
            perms.append('administrator')
            msg = 'administrator'
        else:
            if member.guild_permissions.create_instant_invite:
                perms.append('create_instant_invite')
            if member.guild_permissions.kick_members:
                perms.append('kick_members')
            if member.guild_permissions.ban_members:
                perms.append('ban_members')
            if member.guild_permissions.manage_channels:
                perms.append('manage_channels')
            if member.guild_permissions.manage_guild:
                perms.append('manage_guild')
            if member.guild_permissions.add_reactions:
                perms.append('add_reactions')
            if member.guild_permissions.view_audit_log:
                perms.append('view_audit_log')
            if member.guild_permissions.priority_speaker:
                perms.append('priority_speaker')
            if member.guild_permissions.stream:
                perms.append('stream')
            if member.guild_permissions.read_messages:
                perms.append('read_messages')
            if member.guild_permissions.send_messages:
                perms.append('send_messages')
            if member.guild_permissions.send_tts_messages:
                perms.append('send_tts_messages')
            if member.guild_permissions.manage_messages:
                perms.append('manage_messages')
            if member.guild_permissions.embed_links:
                perms.append('embed_links')
            if member.guild_permissions.attach_files:
                perms.append('attach_files')
            if member.guild_permissions.read_message_history:
                perms.append('read_message_history')
            if member.guild_permissions.mention_everyone:
                perms.append('mention_everyone')
            if member.guild_permissions.external_emojis:
                perms.append('external_emojis')
            if member.guild_permissions.connect:
                perms.append('connect')
            if member.guild_permissions.speak:
                perms.append('speak')
            if member.guild_permissions.mute_members:
                perms.append('mute_members')
            if member.guild_permissions.deafen_members:
                perms.append('deafen_members')
            if member.guild_permissions.move_members:
                perms.append('move_members')
            if member.guild_permissions.use_voice_activation:
                perms.append('use_voice_activation')
            if member.guild_permissions.change_nickname:
                perms.append('change_nickname')
            if member.guild_permissions.manage_nicknames:
                perms.append('manage_nicknames')
            if member.guild_permissions.manage_roles:
                perms.append('manage_roles')
            if member.guild_permissions.manage_webhooks:
                perms.append('manage_webhooks')
            if member.guild_permissions.manage_emojis:
                perms.append('manage_emojis')
            msg = ''
            for i in range(1, len(perms)):
                msg += '{}\n'.format(perms[i])
        permissions = discord.Embed(
            title = '{}\'s perms:'.format(member),
            description = msg,
            color = discord.Color.dark_magenta()
        )
        await message.channel.send(embed = permissions, delete_after = 120)

    if msglower.startswith('-writeas') and message.author.id == 400231667408699392:
        msg = message.content.split(' ', 2)
        await message.delete()
        webhooks = await message.channel.webhooks()
        try:
            web = webhooks[0]
            webid = web.id
            webtoken = web.token
        except:
            await message.channel.send('Вебхуки не найдены!', delete_after = 15)
            return
        try:
            author = msg[1].replace('<', '')
            author = author.replace('>', '')
            author = author.replace('@', '')
            author = message.guild.get_member(int(author))
        except:
            await message.channel.send('Используйте: -writeas [author] [message]', delete_after = 15)
            return
        webhook = discord.Webhook.partial(
            id = webid,
            token = webtoken,
            adapter = discord.RequestsWebhookAdapter()
        )
        try:
            content = msg[2]
        except:
            await message.channel.send('Используйте: -writeas [author] [message]', delete_after = 15)
            return
        webhook.send(
            content = content,
            username = author.display_name,
            avatar_url = author.avatar_url,
        )

    """if msglower.startswith('-exec') and message.author.id == 400231667408699392:
        msg = message.content[5:]
        msg = msg.replace('/', '    ')
        await message.delete()
        command = 'async def on_msg(message: discord.Message):\n' + msg
        print(command)
        exec(command)"""

    if msglower.startswith('-ping'):
        await message.delete()
        msg = await message.channel.send('Считаю...')
        ping = int((msg.created_at.microsecond - message.created_at.microsecond) / 10000)
        pingemoji = client.get_emoji(596025886537678869)
        await msg.edit(content = 'Задержка: **{}** ms! {}'.format(ping, pingemoji), delete_after = 15)

    if msglower.startswith('-mute'):
        if message.author.guild_permissions.mute_members or message.author.id == 400231667408699392:
            msg = message.content.split(' ', 3)
            await message.delete()

            try:
                member = msg[1]
                member = member.replace('<', '')
                member = member.replace('>', '')
                member = member.replace('@', '')
                member = int(member)
                member = message.guild.get_member(member)
            except:
                await message.channel.send('Используйте: -mute [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            try:
                time = msg[2]
                days = re.search(r'\d{1,2}d', time)
                hours = re.search(r'\d{1,2}h', time)
                minutes = re.search(r'\d{1,2}m', time)
                seconds = re.search(r'\d{1,2}s', time)
                try:
                    days = days.group(0)
                    days = days.replace('d', '')
                    days = int(days)
                except:
                    days = 0
                try:
                    hours = hours.group(0)
                    hours = hours.replace('h', '')
                    hours = int(hours)
                except:
                    hours = 0
                try:
                    minutes = minutes.group(0)
                    minutes = minutes.replace('m', '')
                    minutes = int(minutes)
                except:
                    minutes = 0
                try:
                    seconds = seconds.group(0)
                    seconds = seconds.replace('s', '')
                    seconds = int(seconds)
                except:
                    seconds = 0
                time = datetime.datetime.now() + datetime.timedelta(days = days, hours = hours, minutes = minutes, seconds  = seconds)
                msgtime = re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', str(time))
                msgtime = msgtime.group(0)
            except:
                await message.channel.send('Используйте: -mute [@member/member_id] [time(2d2m8s)] ([reason])', delete_after = 15)
                return

            silence = client.get_emoji(597389163096178688)
            panic = client.get_emoji(594496061989584897)


            try:
                reason = msg[3]
            except:
                reason = ''

            muteauthor = ''
            if message.author.guild_permissions.administrator:
                muteauthor = 'администратором'
            else:
                muteauthor = 'модератором'

            muted = open('kvakepmutedmembers.txt', 'r')
            lines = muted.readlines()
            muted.close()
            for l in range(len(lines)):
                if 'Пользователь: {}'.format(member.id) in lines[l]:
                    lines[l] = 'Сервер: {}; Пользователь: {}; Время: {}; Замучен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason)
                    m = open('kvakepmutedmembers.txt', 'a')
                    m.writelines(lines)
                    m.close()
                    break
            else:
                muted = open('kvakepmutedmembers.txt', 'a')
                muted.write('Сервер: {}; Пользователь: {}; Время: {}; Замучен: {}; Причина: {}\n'.format(message.guild.id, member.id, time, message.author.id, reason))
                muted.close()

            if reason != '':
                tomember = discord.Embed(
                    description = 'Вы были замучены {} до {}.\nПричина: {}\n{}'.format(message.author, msgtime, reason, panic),
                    color = discord.Color.dark_red()
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был заглушён {} {} до {}.\nПричина: {}'.format(member, muteauthor, message.author, msgtime, reason),
                    color = discord.Color.dark_grey()
                )
            else:
                tomember = discord.Embed(
                    description = 'Вы были замучены {} до {}.\n{}'.format(message.author, msgtime, panic),
                    color = discord.Color.dark_red()
                )
                tolog = discord.Embed(
                    description = 'Пользователь {} был заглушён {} {} до {}.\n{}'.format(member, muteauthor, message.author, msgtime, silence),
                    color = discord.Color.dark_grey()
                )

            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages = False),
                message.guild.me: discord.PermissionOverwrite(read_messages = True, send_messages = True, manage_messages = True),
            }
            for cat in message.guild.categories:
                if cat.name == 'kvakep-logs':
                    kvakeplogs = cat
                    break
            else:
                kvakeplogs = await message.guild.create_category_channel(
                    name = 'kvakep-logs',
                    overwrites = overwrites,
                    reason = 'Category for kvakep\'s logs'
                )
            for chan in kvakeplogs.channels:
                if chan.name == 'mutes':
                    muteslog = chan
                    break
            else:
                muteslog = await kvakeplogs.create_text_channel(
                    name = 'mutes',
                    overwrites = overwrites,
                    reason = 'Channel for kvakep\'s mutes'
                )

            muterole = discord.Role
            for r in message.guild.roles:
                if int(r.permissions.value) == 1049600:
                    muterole = r
                    break
            else:
                muterole = await message.guild.create_role(
                    name = 'Muted',
                    permissions = discord.Permissions(permissions = 1049600),
                    color = discord.Color.dark_grey(),
                    reason = 'Роль для мутов'
                )
            await member.add_roles(muterole, reason = 'Muted')
            await muteslog.send(embed = tolog)
            await member.send(embed = tomember)
        else:
            await message.channel.send('У Вас недостаточно прав!', delete_after = 15)

    if msglower.startswith('-mlogs'):
        try:
            f = open('kvakepmutedmembers.txt', 'r')
            lines = f.readlines()
            await message.channel.send(lines)
        except Exception as e:
            await message.channel.send(e)



@client.event
async def on_reaction_add(reaction, user):

    if user == client.user:
        return

    if str(reaction.emoji) == '🚩' and user.id == 400231667408699392:
        await reaction.message.delete()

    if str(reaction.emoji) == '📌':
        if user.guild_permissions.manage_messages or user.id == 400231667408699392:
            await reaction.message.remove_reaction('📌', user)
            await reaction.message.pin()
        
    try:
        if reaction.message.id == myemojismsg.id and user.id == 400231667408699392:
            global emojiindex
            if str(reaction.emoji) == '◀':
                try:
                    await myemojismsg.edit(embed = embedlist[emojiindex-1])
                    emojiindex -= 1
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
                except IndexError:
                    emojiindex = 0
                    await myemojismsg.edit(embed = embedlist[emojiindex-1])
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
            if str(reaction.emoji) == '▶':
                try:
                    await myemojismsg.edit(embed = embedlist[emojiindex+1])
                    emojiindex += 1
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
                except IndexError:
                    emojiindex = 0
                    await myemojismsg.edit(embed = embedlist[emojiindex])
                    await myemojismsg.clear_reactions()
                    await myemojismsg.add_reaction('◀')
                    await myemojismsg.add_reaction('▶')
    except:
        pass
    


















client.run('NTgxODIzNzgzMDI3OTk4NzIx.XOvTSg.JeSzfKMWffPnEMTcgmGLNm1KsC0')