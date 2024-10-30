from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask

def build_knowledge_base():
    kb = FolKB()
    # Define variables

    # Add rules to the knowledge base
    # Flu rules
    kb.tell(expr('Fever(x) & Cough(x) & BodyAches(x) & Fatigue(x) ==> Flu(x)'))
    kb.tell(expr('Fever(x) & Chills(x) & Headache(x) & BodyAches(x) ==> Flu(x)'))
    kb.tell(expr('Fever(x) & Snictitation(x) & SoreThroat(x) & Fatigue(x) ==> Flu(x)'))

    # Common Cold rules
    kb.tell(expr('SoreThroat(x) & RunnyNose(x) & Sneezing(x) & MildFever(x) ==> CommonCold(x)'))
    kb.tell(expr('StuffyNose(x) & Coughing(x) & Sneezing(x) & MildFever(x) ==> CommonCold(x)'))
    kb.tell(expr('SoreThroat(x) & RunnyNose(x) & Headache(x) & MildFever(x) ==> CommonCold(x)'))

    # Bronchitis rules
    kb.tell(expr('Cough(x) & MucusProduction(x) & ChestDiscomfort(x) & Fatigue(x) ==> Bronchitis(x)'))
    kb.tell(expr('Cough(x) & WheezeBreathing(x) & ChestDiscomfort(x) & LowFever(x) ==> Bronchitis(x)'))
    kb.tell(expr('Cough(x) & MucusProduction(x) & ChestDiscomfort(x) & Headache(x) ==> Bronchitis(x)'))

    # Pneumonia rules
    kb.tell(expr('Cough(x) & ChestPain(x) & Fatigue(x) & HighFever(x) & ShortBreath(x) ==> Pneumonia(x)'))
    kb.tell(expr('Cough(x) & ChestPain(x) & Fatigue(x) & HighFever(x) & ChillsAndShivering(x) ==> Pneumonia(x)'))
    kb.tell(expr('Cough(x) & ChestPain(x) & Fatigue(x) & HighFever(x) & NauseaAndVomiting(x) ==> Pneumonia(x)'))

    # Asthma rules
    kb.tell(expr('WheezeBreathing(x) & ChestTightness(x) & CoughingAndWheezing(x) & ShortBreath(x) ==> Asthma(x)'))
    kb.tell(expr('WheezeBreathing(x) & ChestTightness(x) & CoughingAndWheezing(x) & SleepDisturbance(x) ==> Asthma(x)'))
    kb.tell(expr('WheezeBreathing(x) & ChestTightness(x) & CoughingAndWheezing(x) & ActivityLimitation(x) ==> Asthma(x)'))

    # Allergic Rhinitis rules
    kb.tell(expr('RunnyNose(x) & Sneezing(x) & NasalCongestion(x) & ItchyEyes(x) ==> AllergicRhinitis(x)'))
    kb.tell(expr('RunnyNose(x) & Sneezing(x) & NasalCongestion(x) & NosalItching(x) ==> AllergicRhinitis(x)'))
    kb.tell(expr('RunnyNose(x) & Sneezing(x) & NasalCongestion(x) & ThroatIrritation(x) ==> AllergicRhinitis(x)'))

    # Sinusitis rules
    kb.tell(expr('FacialPain(x) & FacialPressure(x) & NasalCongestion(x) & FeverAndFatigue(x) ==> Sinusitis(x)'))
    kb.tell(expr('FacialPain(x) & FacialPressure(x) & NasalCongestion(x) & ToothPain(x) ==> Sinusitis(x)'))
    kb.tell(expr('FacialPain(x) & FacialPressure(x) & NasalCongestion(x) & BadBreath(x) ==> Sinusitis(x)'))

    # Strep Throat rules
    kb.tell(expr('SevereThroatPain(x) & DifficultySwallowing(x) & FeverAndHeadache(x) & SwollenLymphNodes(x) ==> StrepThroat(x)'))
    kb.tell(expr('SevereThroatPain(x) & DifficultySwallowing(x) & FeverAndHeadache(x) & RedSwollenTonsils(x) ==> StrepThroat(x)'))
    kb.tell(expr('SevereThroatPain(x) & DifficultySwallowing(x) & FeverAndHeadache(x) & WhitePatches(x) ==> StrepThroat(x)'))

    # Gastroenteritis rules
    kb.tell(expr('Diarrhea(x) & Vomiting(x) & AbdominalCramps(x) & FeverAndHeadache(x) ==> Gastroenteritis(x)'))
    kb.tell(expr('Diarrhea(x) & Vomiting(x) & AbdominalCramps(x) & NauseaAndFatigue(x) ==> Gastroenteritis(x)'))
    kb.tell(expr('Diarrhea(x) & Vomiting(x) & AbdominalCramps(x) & DehydrationAndWeakness(x) ==> Gastroenteritis(x)'))

    # Urinary Tract Infection (UTI) rules
    kb.tell(expr('BurningUrination(x) & FrequentUrination(x) & PelvicPain(x) & BloodInUrine(x) ==> UTI(x)'))
    kb.tell(expr('BurningUrination(x) & FrequentUrination(x) & PelvicPain(x) & StrongUrineSmel(x) ==> UTI(x)'))
    kb.tell(expr('BurningUrination(x) & FrequentUrination(x) & PelvicPain(x) & BackPain(x) ==> UTI(x)'))

    # Migraine rules
    kb.tell(expr('SevereHeadache(x) & NauseaAndVomiting(x) & SensitivityToLightAndSound(x) & AuraSymptoms(x) ==> Migraine(x)'))
    kb.tell(expr('SevereHeadache(x) & NauseaAndVomiting(x) & SensitivityToLightAndSound(x) & PulsatingPain(x) ==> Migraine(x)'))
    kb.tell(expr('SevereHeadache(x) & NauseaAndVomiting(x) & SensitivityToLightAndSound(x) & TemporalTenderness(x) ==> Migraine(x)'))

    # Diabetes rules
    kb.tell(expr('ExcessiveThirst(x) & ExcessiveUrination(x) & ExtremeHunger(x) & UnexplainedWeightLoss(x) ==> Diabetes(x)'))
    kb.tell(expr('ExcessiveThirst(x) & ExcessiveUrination(x) & ExtremeHunger(x) & FatigueAndWeakness(x) ==> Diabetes(x)'))
    kb.tell(expr('ExcessiveThirst(x) & ExcessiveUrination(x) & ExtremeHunger(x) & BlurredVision(x) ==> Diabetes(x)'))

    # Arthritis rules
    kb.tell(expr('JointPain(x) & JointStiffness(x) & Swelling(x) & RedHotJoints(x) ==> Arthritis(x)'))
    kb.tell(expr('JointPain(x) & JointStiffness(x) & Swelling(x) & ReducedRangeOfMotion(x) ==> Arthritis(x)'))
    kb.tell(expr('JointPain(x) & JointStiffness(x) & Swelling(x) & FatigueAndWeakness(x) ==> Arthritis(x)'))

    # Heart Disease rules
    kb.tell(expr('ChestPain(x) & ShortBreath(x) & Fatigue(x) & IrregularHeartbeat(x) ==> HeartDisease(x)'))
    kb.tell(expr('ChestPain(x) & ShortBreath(x) & Fatigue(x) & SwollenLegs(x) ==> HeartDisease(x)'))
    kb.tell(expr('ChestPain(x) & ShortBreath(x) & Fatigue(x) & DizzinessAndFainting(x) ==> HeartDisease(x)'))

    # Anxiety Disorder rules
    kb.tell(expr('ExcessiveWorry(x) & RestlessnessFatigue(x) & IrritabilityAndMuscleTension(x) & SleepDisturbance(x) ==> AnxietyDisorder(x)'))
    kb.tell(expr('ExcessiveWorry(x) & RestlessnessFatigue(x) & IrritabilityAndMuscleTension(x) & DifficultyConcentrating(x) ==> AnxietyDisorder(x)'))
    kb.tell(expr('ExcessiveWorry(x) & RestlessnessFatigue(x) & IrritabilityAndMuscleTension(x) & PanicAttacks(x) ==> AnxietyDisorder(x)'))

    # Depression rules
    kb.tell(expr('SadOrDepressedMood(x) & LossOfInterest(x) & AppetiteChanges(x) & SleepDisturbance(x) ==> Depression(x)'))
    kb.tell(expr('SadOrDepressedMood(x) & LossOfInterest(x) & AppetiteChanges(x) & FatigueOrLowEnergy(x) ==> Depression(x)'))
    kb.tell(expr('SadOrDepressedMood(x) & LossOfInterest(x) & AppetiteChanges(x) & LowSelfEsteem(x) ==> Depression(x)'))

    # Flu treatments
    kb.tell(expr('Flu(x) ==> (TakeOverTheCounterMedications(x) & GetRestAndFluids(x))'))

    # Common Cold treatments
    kb.tell(expr('CommonCold(x) ==> (TakeOverTheCounterDecongestants(x) & GetRestAndHydrate(x))'))

    # Bronchitis treatments
    kb.tell(expr('Bronchitis(x) ==> (TakeBronchodilators(x) & UseHumidifier(x))'))

    # Pneumonia treatments
    kb.tell(expr('Pneumonia(x) ==> (TakeAntibiotics(x) & GetRestAndHydrate(x))'))

    # Asthma treatments
    kb.tell(expr('Asthma(x) ==> (UseInhaledCorticosteroids(x) & AvoidTriggers(x))'))

    # Allergic Rhinitis treatments
    kb.tell(expr('AllergicRhinitis(x) ==> (TakeAntihistamines(x) & AvoidAllergens(x))'))

    # Sinusitis treatments
    kb.tell(expr('Sinusitis(x) ==> (TakeDecongestants(x) & UseNasalSalineSprays(x))'))

    # Strep Throat treatments
    kb.tell(expr('StrepThroat(x) ==> (TakeAntibiotics(x) & GargleWithSaltWater(x))'))

    # Gastroenteritis treatments
    kb.tell(expr('Gastroenteritis(x) ==> (StayHydrated(x) & EatBlandDiet(x))'))

    # Urinary Tract Infection (UTI) treatments
    kb.tell(expr('UTI(x) ==> (TakeAntibiotics(x) & DrinkPlentyOfFluids(x))'))

    # Migraine treatments
    kb.tell(expr('Migraine(x) ==> (TakeTriptanMedications(x) & RestInDarkQuietRoom(x))'))

    # Diabetes treatments
    kb.tell(expr('Diabetes(x) ==> (MonitorBloodSugarLevels(x) & FollowDiabeticDiet(x))'))

    # Arthritis treatments
    kb.tell(expr('Arthritis(x) ==> (TakeAntiInflammatoryMedications(x) & DoLowImpactExercises(x))'))

    # Heart Disease treatments
    kb.tell(expr('HeartDisease(x) ==> (TakeMedicationsAsPrescribed(x) & MakeLifestyleChanges(x))'))

    # Anxiety Disorder treatments
    kb.tell(expr('AnxietyDisorder(x) ==> (TryTherapyOrCounseling(x) & PracticeRelaxationTechniques(x))'))

    # Depression treatments
    kb.tell(expr('Depression(x) ==> (TakeAntidepressantMedications(x) & GetPsychotherapy(x))'))
    return kb
