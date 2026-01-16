#!/bin/bash

# Helping Hands Frontend Update & Deploy Script
# This script updates index.html and deploys to GitHub Pages

echo "🚀 Helping Hands Frontend Updater & Deployer"
echo "=============================================="
echo ""

# Check if index.html exists
if [ ! -f "index.html" ]; then
    echo "❌ Error: index.html not found"
    echo "   Please run this script from the repository root"
    exit 1
fi

echo "📝 Applying updates to index.html..."

# 1. Reset donation stats
sed -i.bak 's/<div class="stat-number">12,543<\/div>/<div class="stat-number">0<\/div>/g' index.html
sed -i.bak 's/<div class="stat-number">8,921<\/div>/<div class="stat-number">0<\/div>/g' index.html
sed -i.bak 's/<div class="stat-number">₹45.2L<\/div>/<div class="stat-number">₹0<\/div>/g' index.html
sed -i.bak 's/<div class="stat-number">156<\/div>/<div class="stat-number">0<\/div>/g' index.html
echo "   ✓ Reset donation stats to 0"

# 2. Make phone optional in signup
sed -i.bak 's/<label>Phone Number<\/label>/<label>Phone Number (Optional)<\/label>/g' index.html
sed -i.bak 's/id="signupPhone" required/id="signupPhone"/g' index.html
echo "   ✓ Made phone optional in signup"

# 3. Make contact optional in request
sed -i.bak 's/<label>Contact Number<\/label>/<label>Contact Number (Optional)<\/label>/g' index.html
echo "   ✓ Made contact optional in request"

# 4. Update location placeholder
sed -i.bak 's/placeholder="City, State"/placeholder="Default: Bhopal, Madhya Pradesh"/g' index.html
echo "   ✓ Updated location placeholder"

# 5. Update footer location
sed -i.bak 's/Mumbai, India/Bhopal, Madhya Pradesh, India/g' index.html
echo "   ✓ Updated footer location"

# 6. Update JavaScript for optional phone
sed -i.bak "s/const phone = document.getElementById('signupPhone').value;/const phone = document.getElementById('signupPhone').value || null; \/\/ Phone is optional/g" index.html
echo "   ✓ Updated JavaScript for optional phone"

# Remove backup file
rm -f index.html.bak

echo ""
echo "✅ All updates applied successfully!"
echo ""

# Ask if user wants to deploy
read -p "🚀 Deploy to GitHub Pages? (y/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📤 Committing and pushing changes..."
    
    git add index.html
    git commit -m "Reset stats, make phone optional, update location to Bhopal"
    git push origin main
    
    echo ""
    echo "✅ Deployed successfully!"
    echo ""
    echo "🌐 Your site will be live in 1-2 minutes at:"
    echo "   https://devyansh-sargam.github.io/helping-hands-donation/"
    echo ""
else
    echo ""
    echo "📋 Changes applied but not deployed."
    echo "   To deploy later, run:"
    echo "   git add index.html"
    echo "   git commit -m 'Reset stats, make phone optional, update location to Bhopal'"
    echo "   git push origin main"
    echo ""
fi

echo "✨ Done!"
