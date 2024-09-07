import pickle
import random

#-------- Loading Severe Model --------------------

def load_severe_diet_plans():
    with open('models\severe_model\severe_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\severe_model\severe_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading Moderate Model --------------------

def load_moderate_diet_plans():
    with open('models\moderate_model\moderate_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\moderate_model\moderate_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading Mild Model --------------------

def load_mild_diet_plans():
    with open('models\mild_model\mild_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\mild_model\mild_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading normal Model --------------------

def load_normal_diet_plans():
    with open('models/normal_model/normal_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models/normal_model/normal_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading overweight Model --------------------

def load_overweight_diet_plans():
    with open('models\overweight_model\overweight_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\overweight_model\overweight_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading obese class 1 Model --------------------

def load_obese_class_1_diet_plans():
    with open('models\obese_class1_model\obese_class1_non_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\obese_class1_model\obese_class1_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading obese_class_2 Model --------------------

def load_obese_class_2_diet_plans():
    with open('models\obese_class2_model\obese_class2_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\obese_class2_model\obese_class2_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans

#-------- Loading obese_class_3 Model --------------------

def load_obese_class_3_diet_plans():
    with open('models\obese_class3_model\obese_class3_vegetarian_diet_plans.pkl', 'rb') as f:
        vegetarian_plans = pickle.load(f)
        
    with open('models\obese_class3_model\obese_class3_non_vegetarian_diet_plans.pkl', 'rb') as f:
        non_vegetarian_plans = pickle.load(f)
    
    return vegetarian_plans, non_vegetarian_plans