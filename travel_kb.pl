% ============================================================================
% PAKISTANI TRAVEL & VISA EXPERT SYSTEM - KNOWLEDGE BASE
% ============================================================================
% Author: Travel Expert System
% Purpose: Advise Pakistani citizens on travel destinations
% Scope: 5 destinations (Maldives, Nepal, Turkey, UK, Dubai)
% ============================================================================

% ============================================================================
% FACTS: VISA STATUS
% ============================================================================
% visa_status(Destination, Status)
% Status types: visa_free, visa_on_arrival, e_visa, visa_required

visa_status(maldives, visa_free).
visa_status(nepal, visa_on_arrival).
visa_status(turkey, e_visa).
visa_status(uk, visa_required).
visa_status(dubai, visa_required).


% ============================================================================
% FACTS: BUDGET LEVELS
% ============================================================================
% budget_level(Destination, Level)
% Level types: low, medium, high

budget_level(maldives, high).
budget_level(nepal, low).
budget_level(turkey, medium).
budget_level(uk, high).
budget_level(dubai, high).


% ============================================================================
% FACTS: INTERESTS MATCHING
% ============================================================================
% interest_match(Destination, Interest)
% Interest types: beach, nature, history, shopping, city

interest_match(maldives, beach).
interest_match(nepal, nature).
interest_match(turkey, history).
interest_match(turkey, beach).
interest_match(uk, city).
interest_match(dubai, shopping).
interest_match(dubai, city).


% ============================================================================
% FACTS: MINIMUM BUDGET (in USD)
% ============================================================================
% min_budget(Destination, Amount)

min_budget(maldives, 2000).
min_budget(nepal, 500).
min_budget(turkey, 1000).
min_budget(uk, 2500).
min_budget(dubai, 1800).


% ============================================================================
% FACTS: VISA DOCUMENTS REQUIRED
% ============================================================================
% visa_documents(Destination, DocumentsList)

visa_documents(maldives, 'Valid passport (6 months validity), Return ticket, Hotel booking confirmation').
visa_documents(nepal, 'Valid passport (min 6 months), 2 passport photos, Visa fee $30 USD').
visa_documents(turkey, 'E-visa (apply online at evisa.gov.tr), Valid passport, Travel insurance recommended').
visa_documents(uk, 'UK visa application (online), Bank statements (6 months), Employment letter, Travel itinerary, Accommodation proof').
visa_documents(dubai, 'UAE visa (via travel agent/airline), Valid passport (6 months), Passport photocopy, Passport-size photo').


% ============================================================================
% FACTS: BEST TRAVEL SEASON
% ============================================================================
% best_season(Destination, Season)

best_season(maldives, 'November to April (Dry season)').
best_season(nepal, 'September to November (Clear skies, trekking season)').
best_season(turkey, 'April to October (Warm weather)').
best_season(uk, 'May to September (Summer, fewer crowds)').
best_season(dubai, 'November to March (Cooler weather)').


% ============================================================================
% RULES: BUDGET MATCHING LOGIC
% ============================================================================
% budget_matches(UserBudget, DestinationBudget)
% Logic: User with higher budget can visit lower budget destinations

budget_matches(low, low).
budget_matches(medium, low).
budget_matches(medium, medium).
budget_matches(high, low).
budget_matches(high, medium).
budget_matches(high, high).


% ============================================================================
% RULES: CAN VISIT (Main Decision Rule)
% ============================================================================
% can_visit(Destination, UserBudget, UserInterest)
% A destination is suitable if:
%   1. User's interest matches destination's offerings
%   2. User's budget matches destination's budget requirement

can_visit(Dest, Budget, Interest) :-
    interest_match(Dest, Interest),
    budget_level(Dest, Level),
    budget_matches(Budget, Level).


% ============================================================================
% RULES: COMPLETE DESTINATION INFO
% ============================================================================
% destination_info(Dest, Budget, Interest, Visa, Docs, Season, MinBudget)
% Returns all relevant information for matching destinations

destination_info(Dest, Budget, Interest, Visa, Docs, Season, MinBudget) :-
    can_visit(Dest, Budget, Interest),
    visa_status(Dest, Visa),
    visa_documents(Dest, Docs),
    best_season(Dest, Season),
    min_budget(Dest, MinBudget).


% ============================================================================
% HELPER RULES: VISA DIFFICULTY
% ============================================================================
% visa_difficulty(Destination, Difficulty)
% Difficulty levels: easy, moderate, difficult

visa_difficulty(Dest, easy) :-
    visa_status(Dest, visa_free).

visa_difficulty(Dest, easy) :-
    visa_status(Dest, visa_on_arrival).

visa_difficulty(Dest, moderate) :-
    visa_status(Dest, e_visa).

visa_difficulty(Dest, difficult) :-
    visa_status(Dest, visa_required).


% ============================================================================
% HELPER RULES: BUDGET RANGE
% ============================================================================
% in_budget_range(Destination, UserBudget)
% Check if user can afford the destination

in_budget_range(Dest, UserBudgetAmount) :-
    min_budget(Dest, MinRequired),
    UserBudgetAmount >= MinRequired.


% ============================================================================
% QUERY EXAMPLES (for testing in SWI-Prolog)
% ============================================================================
% ?- can_visit(Dest, medium, beach).
% ?- destination_info(Dest, high, shopping, Visa, Docs, Season, MinBudget).
% ?- visa_difficulty(maldives, Difficulty).
% ?- findall(Dest, interest_match(Dest, beach), Beaches).
% ============================================================================