import os

# 创建authors目录（如果不存在）
authors_dir = "content/authors"
os.makedirs(authors_dir, exist_ok=True)

# 团队成员数据
team_members = [
    # PhD Students
    {"name": "Jingjing REN", "role": "PhD Student", "group": "PhD Students", 
     "research": "low-level vision, image/video processing", "start_year": "2022"},
    {"name": "Yijun Yang", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis, low-level vision, Generalizable AI", "start_year": "2022"},
    {"name": "Haoyu Chen", "role": "PhD Student", "group": "PhD Students", 
     "research": "low-level vision, image/video processing", "start_year": "2022"},
    {"name": "Yunlu Yan", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis, Federated Learning", "start_year": "2022"},
    {"name": "Zhaohu Xing", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis", "start_year": "2023"},
    {"name": "Haipeng Zhou", "role": "PhD Student", "group": "PhD Students", 
     "research": "Computer vision and Deep learning, including domain adaption, detection and segmentation, image restoration", "start_year": "2023"},
    {"name": "Hongqiu Wang", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis, Surgical AI", "start_year": "2024"},
    {"name": "Jialu Li", "role": "PhD Student", "group": "PhD Students", 
     "research": "Deep learning, Medical image analysis", "start_year": "2023"},
    {"name": "Yujie Zhou", "role": "PhD Student", "group": "PhD Students", 
     "research": "Computer vision", "start_year": "2024"},
    {"name": "Pengfei Hao", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis, AI in surgical robot", "start_year": "2024"},
    {"name": "Tian Ye", "role": "PhD Student", "group": "PhD Students", 
     "research": "Low-level vision, Image/video generation", "start_year": "2024"},
    {"name": "Sixiang Chen", "role": "PhD Student", "group": "PhD Students", 
     "research": "Low-level vision, Image generation, Prompt learning", "start_year": "2024"},
    {"name": "Wenxue Li", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical Image Analysis; Multimodal Large Language Model", "start_year": "2024"},
    {"name": "Ruiqiang Xiao", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical image analysis, In-context Learning", "start_year": "2025"},
    {"name": "Kecheng Wu", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical Image Analysis; Surgical video processing", "start_year": "2025"},
    {"name": "Shuqi Song", "role": "PhD Student", "group": "PhD Students", 
     "research": "Computer Vision, Image/Video Segmentation", "start_year": "2025"},
    {"name": "Huayu Li", "role": "PhD Student", "group": "PhD Students", 
     "research": "Medical Image analysis; Intelligent Surgery", "start_year": "2025"},
    
    # MPhil Students
    {"name": "Zekai Liu", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image generation and analysis, Deep learning", "start_year": "2024"},
    {"name": "Song Fei", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Computer Vision, Deep learning", "start_year": "2024"},
    {"name": "Jianyu Lai", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Low-level vision, Image generation", "start_year": "2024"},
    {"name": "Ruicheng Ao", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image analysis", "start_year": "2024"},
    {"name": "Xingyu Li", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image analysis", "start_year": "2024"},
    {"name": "Xincheng YAO", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image processing and generation", "start_year": "2024"},
    {"name": "Shuaibo Li", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Media Forensics, Medical image analysis, Generative models", "start_year": "2024"},
    {"name": "Hongri Tian", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Computer Vision, Deep learning", "start_year": "2024"},
    {"name": "Jiarong Zhang", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image processing and 3D reconstruction", "start_year": "2024"},
    {"name": "Sicheng Yang", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical Image Analysis; Multimodal Large Language Model", "start_year": "2025"},
    {"name": "Heming Li", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Computer Vision, Image Generation", "start_year": "2025"},
    {"name": "Jiashu Xu", "role": "MPhil Student", "group": "MPhil Students", 
     "research": "Medical image analysis", "start_year": "2025"},
    
    # Research Assistants
    {"name": "Sihan Yang", "role": "Research Assistant", "group": "Research Assistants", 
     "research": "Medical image analysis, multimodal large language model", "start_year": "2024"},
    {"name": "Jinshan Liu", "role": "Research Assistant", "group": "Research Assistants", 
     "research": "Image Shadow Removal; Multimodal Large Language Model", "start_year": "2024"},
]

# 为每个成员创建文件夹和_index.md文件
for member in team_members:
    # 创建文件夹名（使用英文名，去掉空格）
    folder_name = member["name"].replace(" ", "_")
    member_dir = os.path.join(authors_dir, folder_name)
    os.makedirs(member_dir, exist_ok=True)
    
    # 创建_index.md文件
    index_content = f"""---
# Display name
title: {member["name"]}

# Full name (for SEO)
first_name: {member["name"].split()[0]}
last_name: {member["name"].split()[-1]}

# Username (this should match the folder name)
authors:
  - {folder_name}

# Is this the primary user of the site?
superuser: false

# Role/position
role: {member["role"]}

# Organizations/Affiliations
organizations:
  - name: The Hong Kong University of Science and Technology (Guangzhou)
    url: 'https://hkust-gz.edu.cn/'

# Short bio (displayed in user profile at end of posts)
bio: My research interests include {member["research"]}.

interests:
  - {member["research"]}

education:
  courses:
    - course: {member["role"]} in Artificial Intelligence
      institution: The Hong Kong University of Science and Technology (Guangzhou)
      year: {member["start_year"]} - Present

# Social/Academic Networking
social:
  - icon: envelope
    icon_pack: fas
    link: 'mailto:{member["name"].split()[0].lower()}.{member["name"].split()[-1].lower()}@connect.hkust-gz.edu.cn'
  - icon: github
    icon_pack: fab
    link: 'https://github.com/{folder_name.lower()}'

# Enter email to display Gravatar (if Gravatar enabled in Config)
email: ''

# Organizational groups that you belong to (for People widget)
user_groups:
  - {member["group"]}
---

{member["name"]} is a {member["role"].lower()} at The Hong Kong University of Science and Technology (Guangzhou). His/Her research interests include {member["research"]}.

"""
    
    # 写入文件
    with open(os.path.join(member_dir, "_index.md"), "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"Created: {member_dir}/_index.md")

print("All team member profiles have been created successfully!")