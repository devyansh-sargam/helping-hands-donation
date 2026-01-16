// Script to update index.html with required changes
// Run this in browser console on the GitHub edit page

const updates = {
  // Reset donation stats to 0
  stats: [
    { find: '<div class="stat-number">12,543</div>', replace: '<div class="stat-number">0</div>' },
    { find: '<div class="stat-number">8,921</div>', replace: '<div class="stat-number">0</div>' },
    { find: '<div class="stat-number">₹45.2L</div>', replace: '<div class="stat-number">₹0</div>' },
    { find: '<div class="stat-number">156</div>', replace: '<div class="stat-number">0</div>' }
  ],
  
  // Make phone optional in signup
  signup: [
    { 
      find: '<label>Phone Number</label>\n                    <input type="tel" id="signupPhone" required placeholder="+91 XXXXX XXXXX">',
      replace: '<label>Phone Number (Optional)</label>\n                    <input type="tel" id="signupPhone" placeholder="+91 XXXXX XXXXX">'
    }
  ],
  
  // Make contact optional in request form
  request: [
    {
      find: '<label>Contact Number</label>\n                    <input type="tel" required placeholder="+91 XXXXX XXXXX">',
      replace: '<label>Contact Number (Optional)</label>\n                    <input type="tel" placeholder="+91 XXXXX XXXXX">'
    },
    {
      find: '<label>Location</label>\n                    <input type="text" required placeholder="City, State">',
      replace: '<label>Location</label>\n                    <input type="text" placeholder="Default: Bhopal, Madhya Pradesh">'
    }
  ],
  
  // Update footer location
  footer: [
    { find: '<li>📍 Mumbai, India</li>', replace: '<li>📍 Bhopal, Madhya Pradesh, India</li>' }
  ],
  
  // Update JavaScript for optional phone
  javascript: [
    {
      find: 'const phone = document.getElementById(\'signupPhone\').value;',
      replace: 'const phone = document.getElementById(\'signupPhone\').value || null; // Phone is optional'
    }
  ]
};

// Function to apply all updates
function applyUpdates(content) {
  let updated = content;
  
  // Apply stats updates
  updates.stats.forEach(u => {
    updated = updated.replace(u.find, u.replace);
  });
  
  // Apply signup updates
  updates.signup.forEach(u => {
    updated = updated.replace(u.find, u.replace);
  });
  
  // Apply request updates
  updates.request.forEach(u => {
    updated = updated.replace(u.find, u.replace);
  });
  
  // Apply footer updates
  updates.footer.forEach(u => {
    updated = updated.replace(u.find, u.replace);
  });
  
  // Apply JavaScript updates
  updates.javascript.forEach(u => {
    updated = updated.replace(u.find, u.replace);
  });
  
  return updated;
}

console.log('Updates ready to apply:');
console.log('- Reset donation stats to 0');
console.log('- Make phone optional in signup');
console.log('- Make contact optional in request');
console.log('- Update location to Bhopal');
console.log('- Update footer location');
console.log('- Update JavaScript for optional phone');
console.log('\nTo apply: Copy index.html content, run applyUpdates(content), paste result back');
