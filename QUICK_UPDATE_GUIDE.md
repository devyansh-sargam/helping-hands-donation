# 🚀 Quick Update Guide - Copy/Paste Ready

## Method 1: GitHub Web Editor (Easiest)

1. Go to: https://github.com/devyansh-sargam/helping-hands-donation/edit/main/index.html
2. Use Ctrl+F (Find) and Ctrl+H (Replace if available) or manually find and replace:

### Update 1: Reset Stats (Lines ~790-810)

**Find:**
```html
<div class="stat-number">12,543</div>
```
**Replace with:**
```html
<div class="stat-number">0</div>
```

**Find:**
```html
<div class="stat-number">8,921</div>
```
**Replace with:**
```html
<div class="stat-number">0</div>
```

**Find:**
```html
<div class="stat-number">₹45.2L</div>
```
**Replace with:**
```html
<div class="stat-number">₹0</div>
```

**Find:**
```html
<div class="stat-number">156</div>
```
**Replace with:**
```html
<div class="stat-number">0</div>
```

---

### Update 2: Make Phone Optional in Signup (Line ~972)

**Find:**
```html
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" id="signupPhone" required placeholder="+91 XXXXX XXXXX">
                </div>
```

**Replace with:**
```html
                <div class="form-group">
                    <label>Phone Number (Optional)</label>
                    <input type="tel" id="signupPhone" placeholder="+91 XXXXX XXXXX">
                </div>
```

---

### Update 3: Make Contact Optional in Request (Line ~1178)

**Find:**
```html
                <div class="form-group">
                    <label>Contact Number</label>
                    <input type="tel" required placeholder="+91 XXXXX XXXXX">
                </div>
```

**Replace with:**
```html
                <div class="form-group">
                    <label>Contact Number (Optional)</label>
                    <input type="tel" placeholder="+91 XXXXX XXXXX">
                </div>
```

---

### Update 4: Update Location Placeholder (Line ~1186)

**Find:**
```html
                <div class="form-group">
                    <label>Location</label>
                    <input type="text" required placeholder="City, State">
                </div>
```

**Replace with:**
```html
                <div class="form-group">
                    <label>Location</label>
                    <input type="text" placeholder="Default: Bhopal, Madhya Pradesh">
                </div>
```

---

### Update 5: Update Footer Location (Line ~1222)

**Find:**
```html
                    <li>📍 Mumbai, India</li>
```

**Replace with:**
```html
                    <li>📍 Bhopal, Madhya Pradesh, India</li>
```

---

### Update 6: Update JavaScript for Optional Phone (Line ~1310)

**Find:**
```javascript
        const phone = document.getElementById('signupPhone').value;
```

**Replace with:**
```javascript
        const phone = document.getElementById('signupPhone').value || null; // Phone is optional
```

---

## Method 2: Command Line (For Developers)

```bash
# Clone the repo
git clone https://github.com/devyansh-sargam/helping-hands-donation.git
cd helping-hands-donation

# Make a backup
cp index.html index.html.backup

# Apply updates using sed (Mac/Linux)
sed -i '' 's/<div class="stat-number">12,543<\/div>/<div class="stat-number">0<\/div>/g' index.html
sed -i '' 's/<div class="stat-number">8,921<\/div>/<div class="stat-number">0<\/div>/g' index.html
sed -i '' 's/<div class="stat-number">₹45.2L<\/div>/<div class="stat-number">₹0<\/div>/g' index.html
sed -i '' 's/<div class="stat-number">156<\/div>/<div class="stat-number">0<\/div>/g' index.html
sed -i '' 's/<label>Phone Number<\/label>/<label>Phone Number (Optional)<\/label>/g' index.html
sed -i '' 's/id="signupPhone" required/id="signupPhone"/g' index.html
sed -i '' 's/<label>Contact Number<\/label>/<label>Contact Number (Optional)<\/label>/g' index.html
sed -i '' 's/placeholder="City, State"/placeholder="Default: Bhopal, Madhya Pradesh"/g' index.html
sed -i '' 's/Mumbai, India/Bhopal, Madhya Pradesh, India/g' index.html
sed -i '' "s/const phone = document.getElementById('signupPhone').value;/const phone = document.getElementById('signupPhone').value || null; \/\/ Phone is optional/g" index.html

# Commit and push
git add index.html
git commit -m "Reset stats, make phone optional, update location to Bhopal"
git push origin main
```

For Linux (remove the '' after -i):
```bash
sed -i 's/pattern/replacement/g' index.html
```

---

## Method 3: Download, Edit, Upload

1. Download: https://raw.githubusercontent.com/devyansh-sargam/helping-hands-donation/main/index.html
2. Open in your favorite text editor (VS Code, Sublime, Notepad++)
3. Use Find & Replace (Ctrl+H) to make all 6 updates above
4. Save the file
5. Go to: https://github.com/devyansh-sargam/helping-hands-donation/upload/main
6. Drag and drop the updated index.html
7. Commit changes

---

## ✅ Verification Checklist

After updating, check:

- [ ] Stats section shows all zeros
- [ ] Signup form says "Phone Number (Optional)"
- [ ] Signup phone field has no red asterisk
- [ ] Request form says "Contact Number (Optional)"
- [ ] Location placeholder shows "Default: Bhopal, Madhya Pradesh"
- [ ] Footer shows "Bhopal, Madhya Pradesh, India"
- [ ] Can signup without entering phone
- [ ] Can create request without phone

---

## 🎯 Expected Result

Visit: https://devyansh-sargam.github.io/helping-hands-donation/

You should see:
- ✅ All donation stats reset to 0
- ✅ Phone fields marked as optional
- ✅ Bhopal as default location
- ✅ Forms work without phone number

---

**Time to complete**: 5-10 minutes
**Difficulty**: Easy (just copy/paste)
**Impact**: Immediate (GitHub Pages deploys in 1-2 minutes)
