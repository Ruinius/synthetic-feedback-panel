import os
import glob

workspace_root = r"f:\AIML projects\synthetic-feedback-panel"
personas_dir = os.path.join(workspace_root, "personas")
skills_dir = os.path.join(workspace_root, ".agents", "skills")

persona_files = glob.glob(os.path.join(personas_dir, "*.md"))

if not persona_files:
    print("No persona files found to consolidate.")
    exit(0)

count = 0
for persona_path in persona_files:
    filename = os.path.basename(persona_path)
    skill_path = os.path.join(skills_dir, filename)
    
    if not os.path.exists(skill_path):
        print(f"Skill file not found for {filename}, skipping.")
        continue
        
    print(f"Consolidating {filename}...")
    
    with open(persona_path, "r", encoding="utf-8") as f:
        persona_content = f.read()
        
    with open(skill_path, "r", encoding="utf-8") as f:
        skill_content = f.read()
        
    # Update skill content
    updated_skill = skill_content.replace(
        f"You are acting as the persona defined in `personas\\{filename}`.",
        "You are acting as the persona defined below."
    )
    updated_skill = updated_skill.replace(
        f"Adopt the persona defined in `personas\\{filename}`.",
        "Adopt the persona defined below."
    )
    
    # Append persona content
    final_content = updated_skill + "\n\n# Persona Definition\n\n" + persona_content
    
    # Write back to skill file
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    # Delete persona file
    os.remove(persona_path)
    print(f"Deleted {persona_path}")
    count += 1

print(f"Consolidation complete. Processed {count} files.")
