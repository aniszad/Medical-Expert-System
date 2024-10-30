from aima3.logic import FolKB, fol_fc_ask, fol_bc_ask
from aima3.utils import *

from .agenda import Agenda


def diagnose(kb, agenda, memory, c1, username):
    seen = set()  # Keep track of the conditions already processed
    c2 = 0
    while agenda.agenda and c2 < c1:
        p = agenda.remove_from_agenda(f'symp{c2}')
        print('popped', p)
        if p in seen:
            c2 += 1
            continue  # Skip the condition if it has already been processed
        seen.add(p)
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
            print('memory check----', f'{memory}')
        else:
            print(f'{p} is false.')
            memory[p] = False
        c2 += 1

        if memory.get(expr(f'Fever({username})'), False) and memory.get(expr(f'Cough({username})'),
                                                                        False) and memory.get(
                expr(f'BodyAches({username})'), False) and memory.get(expr(f'Fatigue({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Flu({username})'))
        if memory.get(expr(f'Fever({username})'), False) and memory.get(expr(f'Chills({username})'),
                                                                        False) and memory.get(
                expr(f'Headache({username})'), False) and memory.get(expr(f'BodyAches({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Flu({username})'))
        if memory.get(expr(f'Fever({username})'), False) and memory.get(expr(f'Snictitation({username})'),
                                                                        False) and memory.get(
                expr(f'SoreThroat({username})'), False) and memory.get(expr(f'Fatigue({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Flu({username})'))
        if memory.get(expr(f'SoreThroat({username})'), False) and memory.get(expr(f'RunnyNose({username})'),
                                                                             False) and memory.get(
                expr(f'Sneezing({username})'), False) and memory.get(expr(f'MildFever({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'CommonCold({username})'))
        if memory.get(expr(f'StuffyNose({username})'), False) and memory.get(expr(f'Coughing({username})'),
                                                                             False) and memory.get(
                expr(f'Sneezing({username})'), False) and memory.get(expr(f'MildFever({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'CommonCold({username})'))
        if memory.get(expr(f'SoreThroat({username})'), False) and memory.get(expr(f'RunnyNose({username})'),
                                                                             False) and memory.get(
                expr(f'Headache({username})'), False) and memory.get(expr(f'MildFever({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'CommonCold({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'MucusProduction({username})'),
                                                                        False) and memory.get(
                expr(f'ChestDiscomfort({username})'), False) and memory.get(expr(f'Fatigue({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Bronchitis({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'WheezeBreathing({username})'),
                                                                        False) and memory.get(
                expr(f'ChestDiscomfort({username})'), False) and memory.get(expr(f'LowFever({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Bronchitis({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'MucusProduction({username})'),
                                                                        False) and memory.get(
                expr(f'ChestDiscomfort({username})'), False) and memory.get(expr(f'Headache({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Bronchitis({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'ChestPain({username})'),
                                                                        False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'HighFever({username})'),
                                                                    False) and memory.get(
            expr(f'ShortBreath({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Pneumonia({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'ChestPain({username})'),
                                                                        False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'HighFever({username})'),
                                                                    False) and memory.get(
            expr(f'ChillsAndShivering({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Pneumonia({username})'))
        if memory.get(expr(f'Cough({username})'), False) and memory.get(expr(f'ChestPain({username})'),
                                                                        False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'HighFever({username})'),
                                                                    False) and memory.get(
            expr(f'NauseaAndVomiting({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Pneumonia({username})'))
        if memory.get(expr(f'WheezeBreathing({username})'), False) and memory.get(expr(f'ChestTightness({username})'),
                                                                                  False) and memory.get(
            expr(f'CoughingAndWheezing({username})'), False) and memory.get(expr(f'ShortBreath({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Asthma({username})'))
        if memory.get(expr(f'WheezeBreathing({username})'), False) and memory.get(expr(f'ChestTightness({username})'),
                                                                                  False) and memory.get(
            expr(f'CoughingAndWheezing({username})'), False) and memory.get(expr(f'SleepDisturbance({username})'),
                                                                            False):
            agenda.add_to_agenda("diagnosis", expr(f'Asthma({username})'))
        if memory.get(expr(f'WheezeBreathing({username})'), False) and memory.get(expr(f'ChestTightness({username})'),
                                                                                  False) and memory.get(
                expr(f'CoughingAndWheezing({username})'), False) and memory.get(expr(f'ActivityLimitation({username})'),
                                                                                False):
            agenda.add_to_agenda("diagnosis", expr(f'Asthma({username})'))
        if memory.get(expr(f'RunnyNose({username})'), False) and memory.get(expr(f'Sneezing({username})'),
                                                                            False) and memory.get(
                expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'ItchyEyes({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'AllergicRhinitis({username})'))
        if memory.get(expr(f'RunnyNose({username})'), False) and memory.get(expr(f'Sneezing({username})'),
                                                                            False) and memory.get(
                expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'NosalItching({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'AllergicRhinitis({username})'))
        if memory.get(expr(f'RunnyNose({username})'), False) and memory.get(expr(f'Sneezing({username})'),
                                                                            False) and memory.get(
                expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'ThroatIrritation({username})'),
                                                                            False):
            agenda.add_to_agenda("diagnosis", expr(f'AllergicRhinitis({username})'))
        if memory.get(expr(f'FacialPain({username})'), False) and memory.get(expr(f'FacialPressure({username})'),
                                                                             False) and memory.get(
            expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'FeverAndFatigue({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Sinusitis({username})'))
        if memory.get(expr(f'FacialPain({username})'), False) and memory.get(expr(f'FacialPressure({username})'),
                                                                             False) and memory.get(
                expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'ToothPain({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Sinusitis({username})'))
        if memory.get(expr(f'FacialPain({username})'), False) and memory.get(expr(f'FacialPressure({username})'),
                                                                             False) and memory.get(
                expr(f'NasalCongestion({username})'), False) and memory.get(expr(f'BadBreath({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Sinusitis({username})'))
        if memory.get(expr(f'SevereThroatPain({username})'), False) and memory.get(
                expr(f'DifficultySwallowing({username})'),
                False) and memory.get(
            expr(f'FeverAndHeadache({username})'), False) and memory.get(expr(f'SwollenLymphNodes({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'StrepThroat({username})'))
        if memory.get(expr(f'SevereThroatPain({username})'), False) and memory.get(
                expr(f'DifficultySwallowing({username})'),
                False) and memory.get(
            expr(f'FeverAndHeadache({username})'), False) and memory.get(expr(f'RedSwollenTonsils({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'StrepThroat({username})'))
        if memory.get(expr(f'SevereThroatPain({username})'), False) and memory.get(
                expr(f'DifficultySwallowing({username})'),
                False) and memory.get(
            expr(f'FeverAndHeadache({username})'), False) and memory.get(expr(f'WhitePatches({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'StrepThroat({username})'))
        if memory.get(expr(f'Diarrhea({username})'), False) and memory.get(expr(f'Vomiting({username})'),
                                                                           False) and memory.get(
                expr(f'AbdominalCramps({username})'), False) and memory.get(expr(f'FeverAndHeadache({username})'),
                                                                            False):
            agenda.add_to_agenda("diagnosis", expr(f'Gastroenteritis({username})'))
        if memory.get(expr(f'Diarrhea({username})'), False) and memory.get(expr(f'Vomiting({username})'),
                                                                           False) and memory.get(
                expr(f'AbdominalCramps({username})'), False) and memory.get(expr(f'NauseaAndFatigue({username})'),
                                                                            False):
            agenda.add_to_agenda("diagnosis", expr(f'Gastroenteritis({username})'))
        if memory.get(expr(f'Diarrhea({username})'), False) and memory.get(expr(f'Vomiting({username})'),
                                                                           False) and memory.get(
                expr(f'AbdominalCramps({username})'), False) and memory.get(expr(f'DehydrationAndWeakness({username})'),
                                                                            False):
            agenda.add_to_agenda("diagnosis", expr(f'Gastroenteritis({username})'))
        if memory.get(expr(f'BurningUrination({username})'), False) and memory.get(
                expr(f'FrequentUrination({username})'),
                False) and memory.get(expr(f'PelvicPain({username})'),
                                      False) and memory.get(
            expr(f'BloodInUrine({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'UTI({username})'))
        if memory.get(expr(f'BurningUrination({username})'), False) and memory.get(
                expr(f'FrequentUrination({username})'),
                False) and memory.get(expr(f'PelvicPain({username})'),
                                      False) and memory.get(
            expr(f'StrongUrineSmel({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'UTI({username})'))
        if memory.get(expr(f'BurningUrination({username})'), False) and memory.get(
                expr(f'FrequentUrination({username})'),
                False) and memory.get(expr(f'PelvicPain({username})'),
                                      False) and memory.get(
            expr(f'BackPain({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'UTI({username})'))
        if memory.get(expr(f'SevereHeadache({username})'), False) and memory.get(expr(f'NauseaAndVomiting({username})'),
                                                                                 False) and memory.get(
            expr(f'SensitivityToLightAndSound({username})'), False) and memory.get(expr(f'AuraSymptoms({username})'),
                                                                                   False):
            agenda.add_to_agenda("diagnosis", expr(f'Migraine({username})'))
        if memory.get(expr(f'SevereHeadache({username})'), False) and memory.get(expr(f'NauseaAndVomiting({username})'),
                                                                                 False) and memory.get(
            expr(f'SensitivityToLightAndSound({username})'), False) and memory.get(expr(f'PulsatingPain({username})'),
                                                                                   False):
            agenda.add_to_agenda("diagnosis", expr(f'Migraine({username})'))
        if memory.get(expr(f'SevereHeadache({username})'), False) and memory.get(expr(f'NauseaAndVomiting({username})'),
                                                                                 False) and memory.get(
            expr(f'SensitivityToLightAndSound({username})'), False) and memory.get(
            expr(f'TemporalTenderness({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Migraine({username})'))
        if memory.get(expr(f'ExcessiveThirst({username})'), False) and memory.get(
                expr(f'ExcessiveUrination({username})'),
                False) and memory.get(
            expr(f'ExtremeHunger({username})'), False) and memory.get(expr(f'UnexplainedWeightLoss({username})'),
                                                                      False):
            agenda.add_to_agenda("diagnosis", expr(f'Diabetes({username})'))
        if memory.get(expr(f'ExcessiveThirst({username})'), False) and memory.get(
                expr(f'ExcessiveUrination({username})'), False) and memory.get(expr(f'ExtremeHunger({username})'),
                                                                               False) and memory.get(
                expr(f'FatigueAndWeakness({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Diabetes({username})'))
        if memory.get(expr(f'ExcessiveThirst({username})'), False) and memory.get(
                expr(f'ExcessiveUrination({username})'), False) and memory.get(expr(f'ExtremeHunger({username})'),
                                                                               False) and memory.get(
                expr(f'BlurredVision({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Diabetes({username})'))
        if memory.get(expr(f'JointPain({username})'), False) and memory.get(expr(f'JointStiffness({username})'),
                                                                            False) and memory.get(
                expr(f'Swelling({username})'), False) and memory.get(expr(f'RedHotJoints({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Arthritis({username})'))
        if memory.get(expr(f'JointPain({username})'), False) and memory.get(expr(f'JointStiffness({username})'),
                                                                            False) and memory.get(
                expr(f'Swelling({username})'), False) and memory.get(expr(f'ReducedRangeOfMotion({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Arthritis({username})'))
        if memory.get(expr(f'JointPain({username})'), False) and memory.get(expr(f'JointStiffness({username})'),
                                                                            False) and memory.get(
                expr(f'Swelling({username})'), False) and memory.get(expr(f'FatigueAndWeakness({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Arthritis({username})'))
        if memory.get(expr(f'ChestPain({username})'), False) and memory.get(expr(f'ShortBreath({username})'),
                                                                            False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'IrregularHeartbeat({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'HeartDisease({username})'))
        if memory.get(expr(f'ChestPain({username})'), False) and memory.get(expr(f'ShortBreath({username})'),
                                                                            False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'SwollenLegs({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'HeartDisease({username})'))
        if memory.get(expr(f'ChestPain({username})'), False) and memory.get(expr(f'ShortBreath({username})'),
                                                                            False) and memory.get(
                expr(f'Fatigue({username})'), False) and memory.get(expr(f'DizzinessAndFainting({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'HeartDisease({username})'))
        if memory.get(expr(f'ExcessiveWorry({username})'), False) and memory.get(
                expr(f'RestlessnessFatigue({username})'), False) and memory.get(
                expr(f'IrritabilityAndMuscleTension({username})'), False) and memory.get(
                expr(f'SleepDisturbance({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'AnxietyDisorder({username})'))
        if memory.get(expr(f'ExcessiveWorry({username})'), False) and memory.get(
                expr(f'RestlessnessFatigue({username})'), False) and memory.get(
                expr(f'IrritabilityAndMuscleTension({username})'), False) and memory.get(
                expr(f'DifficultyConcentrating({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'AnxietyDisorder({username})'))
        if memory.get(expr(f'ExcessiveWorry({username})'), False) and memory.get(
                expr(f'RestlessnessFatigue({username})'), False) and memory.get(
                expr(f'IrritabilityAndMuscleTension({username})'), False) and memory.get(
                expr(f'PanicAttacks({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'AnxietyDisorder({username})'))
        if memory.get(expr(f'SadOrDepressedMood({username})'), False) and memory.get(
                expr(f'LossOfInterest({username})'), False) and memory.get(expr(f'AppetiteChanges({username})'),
                                                                           False) and memory.get(
                expr(f'SleepDisturbance({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Depression({username})'))
        if memory.get(expr(f'SadOrDepressedMood({username})'), False) and memory.get(
                expr(f'LossOfInterest({username})'), False) and memory.get(expr(f'AppetiteChanges({username})'),
                                                                           False) and memory.get(
                expr(f'FatigueOrLowEnergy({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Depression({username})'))
        if memory.get(expr(f'SadOrDepressedMood({username})'), False) and memory.get(
                expr(f'LossOfInterest({username})'), False) and memory.get(expr(f'AppetiteChanges({username})'),
                                                                           False) and memory.get(
                expr(f'LowSelfEsteem({username})'), False):
            agenda.add_to_agenda("diagnosis", expr(f'Depression({username})'))

    return agenda


def get_treatment(kb, memory, agenda, username):
    p = agenda.remove_from_agenda(f'disease')

    if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
            print('memory check----', f'{memory}')
            # Check for treatment expressions and add to agenda
            if p == expr(f'Flu({username})'):
                agenda.add_to_agenda("treatment", expr(f'TakeOverTheCounterMedications({username})'))
                agenda.add_to_agenda("treatment2", expr(f'GetRestAndFluids({username})'))
            elif p == expr(f'CommonCold({username})'):
                agenda.add_to_agenda("treatment", expr(f'TakeOverTheCounterDecongestants({username})'))
                agenda.add_to_agenda("treatment2", expr(f'GetRestAndHydrate({username})'))
            elif p == expr(f'Bronchitis({username})'):
                agenda.add_to_agenda("treatment", expr(f'TakeBronchodilators({username})'))
                agenda.add_to_agenda("treatment2", expr(f'UseHumidifier({username})'))

    return agenda
