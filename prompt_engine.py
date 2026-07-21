import random

def generate_summary(role, experience_level, skills, goal):
    """
    Generate an AI-powered professional summary based on user inputs
    using advanced prompt engineering techniques
    """
    
    experience_profiles = {
        "Fresher": {
            "descriptors": ["motivated", "enthusiastic", "detail-oriented", "eager to learn"],
            "achievements": [
                "ready to contribute fresh perspectives",
                "committed to rapid skill development",
                "prepared to make immediate impact",
                "driven to prove technical capabilities"
            ],
            "approach": [
                "with strong fundamentals in",
                "bringing solid foundation in",
                "equipped with knowledge in",
                "specialized in"
            ]
        },
        "Experienced": {
            "descriptors": ["results-driven", "skilled", "proven", "accomplished", "innovative"],
            "achievements": [
                "with track record of successful implementations",
                "demonstrating consistent delivery",
                "delivering measurable business value",
                "driving technical excellence"
            ],
            "approach": [
                "with extensive experience in",
                "proficient in",
                "specialized in",
                "expert in"
            ]
        },
        "Senior": {
            "descriptors": ["strategic", "accomplished", "visionary", "influential", "thought leader"],
            "achievements": [
                "with proven leadership capabilities",
                "driving organizational transformation",
                "delivering enterprise-scale solutions",
                "mentoring high-performing teams"
            ],
            "approach": [
                "with deep expertise in",
                "leading initiatives in",
                "architecting solutions in",
                "pioneering advances in"
            ]
        }
    }
    
    profile = experience_profiles.get(experience_level, experience_profiles["Experienced"])
    
    descriptor = random.choice(profile["descriptors"])
    achievement = random.choice(profile["achievements"])
    approach = random.choice(profile["approach"])
    
    # Clean up skills for better formatting
    skills_list = [s.strip() for s in skills.split(",")][:5]  # Take top 5 skills
    skills_text = ", ".join(skills_list)
    
    # Construct the summary
    templates = [
        f"{descriptor.capitalize()} {role} {achievement}, {approach} {skills_text}. Seeking to {goal.lower()} while maintaining high standards of excellence.",
        
        f"{descriptor.capitalize()} and skilled {role} with {achievement}. {approach.capitalize()} {skills_text}, committed to {goal.lower()}.",
        
        f"Results-focused {role} bringing {achievement}. {approach.capitalize()} {skills_text} with passion for {goal.lower()}. Dedicated to continuous growth and innovation.",
        
        f"{descriptor.capitalize()} {role} {achievement}. Specialized {approach} {skills_text}. Motivated to {goal.lower()} through technical excellence and collaborative teamwork.",
        
        f"Accomplished {role} combining {achievement} with expertise in {skills_text}. Seeking to leverage experience to {goal.lower()}. Known for delivering innovative solutions."
    ]
    
    return random.choice(templates)

