#!/usr/bin/env python3
"""
Automatic Frontend Updater for Helping Hands Donation Platform
This script updates index.html with all required changes:
- Reset donation stats to 0
- Make phone optional in signup
- Make contact optional in request
- Update location to Bhopal
- Update footer location
- Update JavaScript for optional phone
"""

import re

def update_index_html(content):
    """Apply all updates to index.html content"""
    
    # 1. Reset donation stats to 0
    content = content.replace('<div class="stat-number">12,543</div>', '<div class="stat-number">0</div>')
    content = content.replace('<div class="stat-number">8,921</div>', '<div class="stat-number">0</div>')
    content = content.replace('<div class="stat-number">₹45.2L</div>', '<div class="stat-number">₹0</div>')
    content = content.replace('<div class="stat-number">156</div>', '<div class="stat-number">0</div>')
    
    # 2. Make phone optional in signup form
    content = content.replace(
        '<label>Phone Number</label>\n                    <input type="tel" id="signupPhone" required placeholder="+91 XXXXX XXXXX">',
        '<label>Phone Number (Optional)</label>\n                    <input type="tel" id="signupPhone" placeholder="+91 XXXXX XXXXX">'
    )
    
    # 3. Make contact optional in request form
    content = content.replace(
        '<label>Contact Number</label>\n                    <input type="tel" required placeholder="+91 XXXXX XXXXX">',
        '<label>Contact Number (Optional)</label>\n                    <input type="tel" placeholder="+91 XXXXX XXXXX">'
    )
    
    # 4. Update location placeholder
    content = content.replace(
        '<label>Location</label>\n                    <input type="text" required placeholder="City, State">',
        '<label>Location</label>\n                    <input type="text" placeholder="Default: Bhopal, Madhya Pradesh">'
    )
    
    # 5. Update footer location
    content = content.replace(
        '<li>📍 Mumbai, India</li>',
        '<li>📍 Bhopal, Madhya Pradesh, India</li>'
    )
    
    # 6. Update JavaScript for optional phone
    content = content.replace(
        "const phone = document.getElementById('signupPhone').value;",
        "const phone = document.getElementById('signupPhone').value || null; // Phone is optional"
    )
    
    return content

def main():
    """Main function to read, update, and write index.html"""
    
    print("🚀 Helping Hands Frontend Updater")
    print("=" * 50)
    
    # Read the file
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        print("✅ Read index.html successfully")
    except FileNotFoundError:
        print("❌ Error: index.html not found in current directory")
        print("   Please run this script from the repository root")
        return
    
    # Apply updates
    print("\n📝 Applying updates...")
    updated_content = update_index_html(content)
    
    # Count changes
    changes = 0
    if '<div class="stat-number">0</div>' in updated_content:
        changes += 4
        print("   ✓ Reset donation stats to 0")
    
    if 'Phone Number (Optional)' in updated_content:
        changes += 1
        print("   ✓ Made phone optional in signup")
    
    if 'Contact Number (Optional)' in updated_content:
        changes += 1
        print("   ✓ Made contact optional in request")
    
    if 'Default: Bhopal, Madhya Pradesh' in updated_content:
        changes += 1
        print("   ✓ Updated location placeholder")
    
    if 'Bhopal, Madhya Pradesh, India' in updated_content:
        changes += 1
        print("   ✓ Updated footer location")
    
    if '|| null; // Phone is optional' in updated_content:
        changes += 1
        print("   ✓ Updated JavaScript for optional phone")
    
    # Write the updated file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"\n✅ Successfully applied {changes} updates to index.html")
    print("\n📤 Next steps:")
    print("   1. Review changes: git diff index.html")
    print("   2. Commit: git add index.html")
    print("   3. Commit: git commit -m 'Reset stats, make phone optional, update location to Bhopal'")
    print("   4. Push: git push origin main")
    print("\n🌐 Your site will be live at:")
    print("   https://devyansh-sargam.github.io/helping-hands-donation/")
    print("   (Updates deploy in 1-2 minutes)")

if __name__ == "__main__":
    main()
