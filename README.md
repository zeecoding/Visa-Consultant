# Pakistani Travel & Visa Expert System

An intelligent travel advisor system built with Prolog (knowledge base) and Python (user interface) that recommends destinations for Pakistani travelers based on their budget and interests.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Destinations Covered](#destinations-covered)
- [Extending the System](#extending-the-system)
- [Troubleshooting](#troubleshooting)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This expert system helps Pakistani citizens plan international travel by:
- Recommending suitable destinations based on budget and interests
- Providing visa requirements and documentation details
- Suggesting the best travel seasons
- Displaying minimum budget requirements

**Why Prolog?**

Visa rules and travel restrictions are complex logical relationships, making them perfect for Prolog's declarative reasoning. The system uses backward chaining to infer suitable destinations from user preferences.

---

## Features

### Core Functionality
- Smart Recommendations using Prolog-based inference engine
- Budget-Aware matching of destinations to spending capacity
- Interest-Based filtering by travel preferences (Beach, Nature, History, Shopping, City)
- Visa Guidance with complete documentation requirements
- Season Recommendations for best time to visit each destination
- Material Design UI with modern, intuitive interface

### Technical Features
- Separation of Concerns: Logic (Prolog) separate from UI (Python)
- Real-time Querying: Dynamic Prolog queries via PySwip
- Extensible Knowledge Base: Easy to add new destinations
- Error Handling: Graceful failure with user feedback

---

## Architecture

The system follows a 3-tier expert system architecture:

1. **Knowledge Base** - Facts and rules stored in Prolog (travel_kb.pl)
2. **Inference Engine** - Prolog's built-in backward chaining for reasoning
3. **User Interface** - Python GUI for user interaction (main.py)

**Flow:**
```
User Interface (Python/CustomTkinter)
        |
    PySwip Bridge
        |
Inference Engine (SWI-Prolog)
        |
Knowledge Base (travel_kb.pl)
```

---

## Installation

### Prerequisites

1. **Python 3.8 or higher**
   
   Verify installation:
   ```bash
   python --version
   ```

2. **SWI-Prolog** (Required for Prolog reasoning)
   
   **Windows:**
   - Download from https://www.swi-prolog.org/Download.html
   - Run installer and add to PATH
   
   **macOS:**
   ```bash
   brew install swi-prolog
   ```
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get update
   sudo apt-get install swi-prolog
   ```

3. **Python Packages**
   ```bash
   pip install pyswip customtkinter
   ```

### Installation Steps

1. **Download the Project**
   ```bash
   git clone https://github.com/yourusername/travel-expert-system.git
   cd travel-expert-system
   ```

2. **Verify SWI-Prolog Installation**
   ```bash
   swipl --version
   ```

3. **Install Python Dependencies**
   ```bash
   pip install pyswip customtkinter
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

---

## Usage

### Starting the System

```bash
python main.py
```

### Using the Interface

1. **Select Your Budget**
   - Low: $500 - $800
   - Medium: $1000 - $1500
   - High: $2000+

2. **Choose Your Interest**
   - Beach Paradise
   - Nature & Adventure
   - History & Culture
   - Shopping & Leisure
   - City Exploration

3. **Click "Find Destinations"**
   - System queries the Prolog knowledge base
   - Displays matching destinations as cards
   - Shows visa requirements, required documents, and best travel season

### Example Queries

| Budget | Interest | Expected Result |
|--------|----------|-----------------|
| Low | Nature | Nepal |
| High | Beach | Maldives, Turkey |
| Medium | History | Turkey |
| High | Shopping | Dubai |
| High | City | Dubai, UK |

---

## Project Structure

```
travel-expert-system/
|
├── main.py                 # Python GUI application
├── travel_kb.pl            # Prolog knowledge base
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

### File Descriptions

- **main.py**: Contains the Python GUI application using CustomTkinter. Handles user interaction and queries the Prolog knowledge base.
- **travel_kb.pl**: Prolog file containing all facts and rules about destinations, visa requirements, budgets, and interests.
- **README.md**: This documentation file.

---

## How It Works

### Knowledge Representation in Prolog

The system uses Prolog facts and rules to represent travel knowledge:

**Facts:**
```prolog
visa_status(maldives, visa_free).
budget_level(nepal, low).
interest_match(turkey, history).
min_budget(dubai, 1800).
visa_documents(maldives, 'Valid passport, Return ticket, Hotel booking').
```

**Rules:**
```prolog
% Budget matching logic
budget_matches(high, low).    % High budget can afford low-cost destinations
budget_matches(high, medium).
budget_matches(high, high).
budget_matches(medium, low).
budget_matches(medium, medium).
budget_matches(low, low).

% Main decision rule
can_visit(Dest, Budget, Interest) :-
    interest_match(Dest, Interest),
    budget_level(Dest, Level),
    budget_matches(Budget, Level).
```

### Query Execution Example

When a user selects Budget = high and Interest = beach:

1. Python sends query: `destination_info(Dest, high, beach, ...)`
2. Prolog searches the knowledge base:
   - Finds: `interest_match(maldives, beach)` (Match found)
   - Checks: `budget_matches(high, high)` (Budget sufficient)
   - Result: Maldives is suitable
   - Finds: `interest_match(turkey, beach)` (Match found)
   - Checks: `budget_matches(high, medium)` (Budget sufficient)
   - Result: Turkey is suitable
3. Returns: Maldives and Turkey with complete details

---

## Destinations Covered

The system currently supports 5 destinations:

| Destination | Visa Status | Budget Level | Interests | Minimum Budget |
|-------------|------------|--------------|-----------|----------------|
| Maldives | Visa Free | High | Beach | $2000 |
| Nepal | Visa on Arrival | Low | Nature | $500 |
| Turkey | E-Visa | Medium | History, Beach | $1000 |
| UK | Visa Required | High | City | $2500 |
| Dubai | Visa Required | High | Shopping, City | $1800 |

---

## Extending the System

### Adding a New Destination

To add a new destination, edit the `travel_kb.pl` file:

```prolog
% Add these facts for the new destination
visa_status(thailand, visa_on_arrival).
budget_level(thailand, medium).
interest_match(thailand, beach).
interest_match(thailand, city).
min_budget(thailand, 1200).
visa_documents(thailand, 'Valid passport, Return ticket, Visa on arrival $35').
best_season(thailand, 'November to February (Cool season)').
```

No changes to Python code are needed. The system will automatically include the new destination.

### Adding New Interest Categories

**Step 1:** Add facts in `travel_kb.pl`:
```prolog
interest_match(switzerland, skiing).
```

**Step 2:** Update the GUI in `main.py` (around line 140):
```python
interests = [
    # ... existing interests ...
    ("Skiing & Snow", "skiing"),
]
```

### Modifying Budget Levels

To add more budget tiers, modify the `budget_matches/2` rule in `travel_kb.pl`:

```prolog
budget_matches(ultra_high, low).
budget_matches(ultra_high, medium).
budget_matches(ultra_high, high).
budget_matches(ultra_high, ultra_high).
```

---

## Troubleshooting

### Common Issues and Solutions

**Issue 1: SWI-Prolog not found**
```
Error: pyswip.prolog.PrologError: Could not find SWI-Prolog
```
**Solution:**
- Install SWI-Prolog from the official website
- Add SWI-Prolog to system PATH
- Restart your terminal or IDE

**Issue 2: Knowledge base file not found**
```
FileNotFoundError: Prolog knowledge base 'travel_kb.pl' not found!
```
**Solution:**
- Ensure `travel_kb.pl` is in the same directory as `main.py`
- Check file name spelling (case-sensitive on Linux/Mac)

**Issue 3: Module not found error**
```
ModuleNotFoundError: No module named 'customtkinter'
```
**Solution:**
```bash
pip install customtkinter
```

**Issue 4: Prolog query returns no results**
**Solution:**
- Open `travel_kb.pl` in SWI-Prolog terminal
- Test query manually: `?- can_visit(Dest, high, beach).`
- Check for syntax errors in the Prolog file

**Issue 5: GUI doesn't display properly**
**Solution:**
- Update CustomTkinter: `pip install --upgrade customtkinter`
- Verify Python version is 3.8 or higher

---

## Testing

### Testing the Prolog Knowledge Base

You can test the Prolog knowledge base independently:

```bash
swipl
?- consult('travel_kb.pl').
true.

?- can_visit(Dest, low, nature).
Dest = nepal.

?- destination_info(maldives, high, beach, V, D, S, M).
V = visa_free,
D = 'Valid passport (6 months validity), Return ticket, Hotel booking confirmation',
S = 'November to April (Dry season)',
M = 2000.
```

### Testing the Python Application

Run the application and test different scenarios:

```bash
python main.py
```

Test cases:
- Low Budget + Nature = Should return Nepal
- High Budget + Beach = Should return Maldives and Turkey
- Medium Budget + History = Should return Turkey
- Low Budget + City = Should return no results

---

## Educational Value

This project demonstrates several important concepts:

### Software Engineering
- Separation of Concerns (Logic vs Presentation)
- Declarative Programming (Prolog) vs Imperative Programming (Python)
- Expert Systems Architecture
- MVC Pattern implementation

### Artificial Intelligence
- Backward Chaining reasoning
- Unification and pattern matching
- Rule-Based Systems
- Knowledge representation

### Practical Applications
- Travel planning systems
- Visa advisory tools
- Decision support systems
- Recommendation engines

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-destination`
3. Commit your changes: `git commit -m 'Add Malaysia as destination'`
4. Push to the branch: `git push origin feature/new-destination`
5. Open a Pull Request

**Ideas for Contributions:**
- Add more destinations (Malaysia, Sri Lanka, Saudi Arabia, etc.)
- Implement flight cost estimation
- Add hotel recommendations
- Create a web version using Flask or Streamlit
- Add multi-language support (Urdu, English)
- Include travel insurance recommendations

---

## Future Enhancements

Planned features for future versions:
- Real-time flight price integration
- Hotel booking recommendations
- Multi-country trip planning
- Weather forecasts for destinations
- Currency conversion calculator
- User profile saving
- Export recommendations as PDF
- Mobile application version
- Web deployment

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Acknowledgments

- SWI-Prolog: Powerful Prolog implementation
- CustomTkinter: Modern Python GUI framework
- PySwip: Python-Prolog bridge library
- Pakistani Travel Community: Domain knowledge and requirements

---

**Made for Pakistani Travelers**
