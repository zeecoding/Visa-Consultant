"""
Pakistani Travel & Visa Expert System - Enhanced Material Design UI
Run this file after creating travel_kb.pl
"""

from pyswip import Prolog
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

class TravelExpertSystem:
    def __init__(self, kb_file="travel_kb.pl"):
        self.prolog = Prolog()
        self.kb_file = kb_file
        self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        """Load Prolog knowledge base from .pl file"""
        if not os.path.exists(self.kb_file):
            raise FileNotFoundError(
                f"Prolog knowledge base '{self.kb_file}' not found!\n"
                f"Please create the travel_kb.pl file first."
            )
        
        try:
            self.prolog.consult(self.kb_file)
            print(f"✓ Loaded knowledge base: {self.kb_file}")
        except Exception as e:
            raise Exception(f"Error loading Prolog file: {e}")
    
    def get_recommendations(self, budget, interest):
        """Query Prolog for travel recommendations"""
        query = f"destination_info(Dest, {budget}, {interest}, Visa, Docs, Season, MinBudget)"
        results = []
        
        try:
            for solution in self.prolog.query(query):
                results.append({
                    'destination': solution['Dest'],
                    'visa_status': solution['Visa'],
                    'documents': solution['Docs'],
                    'best_season': solution['Season'],
                    'min_budget': solution['MinBudget']
                })
        except Exception as e:
            print(f"Prolog query error: {e}")
        
        return results


class TravelGUI:
    # Material Design Color Palette
    COLORS = {
        'primary': '#006064',        # Deep Teal
        'primary_dark': "#09686e",   # Darker Teal
        'accent': '#FF6F61',         # Coral
        'background': '#F5F5F5',     # Light Grey
        'card': '#FFFFFF',           # White
        'text_primary': '#212121',   # Dark Grey
        'text_secondary': '#757575', # Medium Grey
        'success': '#00897B',        # Teal Green
        'warning': '#FFB300',        # Amber
        'gradient_start': '#00838F', # Cyan
        'gradient_end': '#006064',   # Teal
    }
    
    # Material Icons (Unicode symbols)
    ICONS = {
        'plane': '✈',
        'money': '💰',
        'beach': '🏖',
        'mountain': '⛰',
        'building': '🏛',
        'shop': '🛒',
        'city': '🌆',
        'calendar': '📅',
        'document': '📋',
        'visa': '🎫',
        'search': '🔍',
        'location': '📍',
        'check': '✓',
        'info': 'ℹ',
        'warning': '⚠',
    }
    
    def __init__(self):
        try:
            self.expert_system = TravelExpertSystem("travel_kb.pl")
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
            sys.exit(1)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize system: {e}")
            sys.exit(1)
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the Material Design GUI"""
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Travel & Visa Consultant")
        self.root.geometry("1000x800")
        self.root.configure(fg_color=self.COLORS['background'])
        
        # Main Container with padding
        main_container = ctk.CTkFrame(self.root, fg_color=self.COLORS['background'])
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header Section
        self._create_header(main_container)
        
        # Content Area (Scrollable)
        self.content_frame = ctk.CTkScrollableFrame(
            main_container,
            fg_color=self.COLORS['background']
        )
        self.content_frame.pack(fill="both", expand=True, pady=(10, 0))
        
        # Input Card
        self._create_input_card(self.content_frame)
        
        # Results Area
        self.results_container = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.COLORS['background']
        )
        self.results_container.pack(fill="both", expand=True, pady=10)
        
        # Footer
        self._create_footer(main_container)
    
    def _create_header(self, parent):
        """Create header with gradient effect"""
        header_frame = ctk.CTkFrame(
            parent,
            height=100,
            fg_color=self.COLORS['primary'],
            corner_radius=15
        )
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)
        
        # Icon and Title
        title_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        title_frame.pack(expand=True)
        
        icon_label = ctk.CTkLabel(
            title_frame,
            text=self.ICONS['plane'],
            font=("Segoe UI Emoji", 40),
            text_color="white"
        )
        icon_label.pack(side="left", padx=(0, 15))
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="Travel & Visa Consultant",
            font=("Segoe UI", 32, "bold"),
            text_color="white"
        )
        title_label.pack(side="left")
        
        subtitle = ctk.CTkLabel(
            header_frame,
            text="Expert guidance for Pakistani travelers",
            font=("Segoe UI", 14),
            text_color="#B2EBF2"
        )
        subtitle.pack(pady=(0, 10))
    
    def _create_input_card(self, parent):
        """Create input section as a Material card"""
        card = ctk.CTkFrame(
            parent,
            fg_color=self.COLORS['card'],
            corner_radius=15,
            border_width=0
        )
        card.pack(fill="x", pady=10, padx=5)
        
        # Card padding
        card_content = ctk.CTkFrame(card, fg_color="transparent")
        card_content.pack(fill="x", padx=30, pady=25)
        
        # Budget Section
        budget_header = ctk.CTkFrame(card_content, fg_color="transparent")
        budget_header.pack(fill="x", pady=(0, 15))
        
        budget_icon = ctk.CTkLabel(
            budget_header,
            text=self.ICONS['money'],
            font=("Segoe UI Emoji", 24),
            text_color=self.COLORS['primary']
        )
        budget_icon.pack(side="left", padx=(0, 10))
        
        budget_title = ctk.CTkLabel(
            budget_header,
            text="Select Your Budget",
            font=("Segoe UI", 18, "bold"),
            text_color=self.COLORS['text_primary']
        )
        budget_title.pack(side="left")
        
        # Budget Options
        self.budget_var = ctk.StringVar(value="medium")
        budget_container = ctk.CTkFrame(card_content, fg_color="transparent")
        budget_container.pack(fill="x", pady=(0, 25))
        
        budgets = [
            ("Low Budget", "Under $800", "low"),
            ("Medium Budget", "$1000 - $1500", "medium"),
            ("High Budget", "$2000+", "high")
        ]
        
        for i, (title, desc, value) in enumerate(budgets):
            self._create_option_button(budget_container, title, desc, 
                                      self.budget_var, value, i)
        
        # Separator
        separator = ctk.CTkFrame(card_content, height=2, fg_color=self.COLORS['background'])
        separator.pack(fill="x", pady=20)
        
        # Interest Section
        interest_header = ctk.CTkFrame(card_content, fg_color="transparent")
        interest_header.pack(fill="x", pady=(0, 15))
        
        interest_icon = ctk.CTkLabel(
            interest_header,
            text=self.ICONS['location'],
            font=("Segoe UI Emoji", 24),
            text_color=self.COLORS['primary']
        )
        interest_icon.pack(side="left", padx=(0, 10))
        
        interest_title = ctk.CTkLabel(
            interest_header,
            text="What Interests You?",
            font=("Segoe UI", 18, "bold"),
            text_color=self.COLORS['text_primary']
        )
        interest_title.pack(side="left")
        
        # Interest Options
        self.interest_var = ctk.StringVar(value="beach")
        interest_container = ctk.CTkFrame(card_content, fg_color="transparent")
        interest_container.pack(fill="x", pady=(0, 20))
        
        interests = [
            (self.ICONS['beach'], "Beach Paradise", "beach"),
            (self.ICONS['mountain'], "Nature & Adventure", "nature"),
            (self.ICONS['building'], "History", "history"),
            (self.ICONS['shop'], "Shopping & Leisure", "shopping"),
            (self.ICONS['city'], "City Exploration", "city")
        ]
        
        for i, (icon, title, value) in enumerate(interests):
            self._create_interest_chip(interest_container, icon, title, 
                                      self.interest_var, value, i)
        
        # Search Button
        search_btn = ctk.CTkButton(
            card_content,
            text=f"{self.ICONS['search']}  Find Destinations",
            command=self.search_destinations,
            font=("Segoe UI", 16, "bold"),
            height=50,
            fg_color=self.COLORS['accent'],
            hover_color="#E55D50",
            corner_radius=25
        )
        search_btn.pack(fill="x", pady=(10, 0))
    
    def _create_option_button(self, parent, title, desc, variable, value, index):
        """Create a material-style option button"""
        btn_frame = ctk.CTkFrame(parent, fg_color="transparent")
        btn_frame.pack(side="left", fill="x", expand=True, padx=5)
        
        def select_option():
            variable.set(value)
        
        is_selected = variable.get() == value
        
        btn = ctk.CTkButton(
            btn_frame,
            text=f"{title}\n{desc}",
            command=select_option,
            font=("Segoe UI", 13),
            height=80,
            fg_color=self.COLORS['primary'] if is_selected else self.COLORS['background'],
            hover_color=self.COLORS['primary_dark'],
            text_color="white" if is_selected else self.COLORS['text_primary'],
            corner_radius=10,
            border_width=2,
            border_color=self.COLORS['primary'] if is_selected else self.COLORS['background']
        )
        btn.pack(fill="both", expand=True)
        
        # Update button on variable change
        def update_style(*args):
            is_sel = variable.get() == value
            btn.configure(
                fg_color=self.COLORS['primary'] if is_sel else self.COLORS['background'],
                text_color="white" if is_sel else self.COLORS['text_primary'],
                border_color=self.COLORS['primary'] if is_sel else self.COLORS['background']
            )
        
        variable.trace_add('write', update_style)
    
    def _create_interest_chip(self, parent, icon, title, variable, value, index):
        """Create interest selection chips"""
        is_selected = variable.get() == value
        
        chip = ctk.CTkButton(
            parent,
            text=f"{icon}  {title}",
            command=lambda: variable.set(value),
            font=("Segoe UI", 13),
            height=45,
            fg_color=self.COLORS['primary'] if is_selected else self.COLORS['background'],
            hover_color=self.COLORS['primary_dark'],
            text_color="white" if is_selected else self.COLORS['text_primary'],
            corner_radius=22,
            border_width=2,
            border_color=self.COLORS['primary'] if is_selected else "#E0E0E0"
        )
        chip.pack(side="left", padx=5, fill="x", expand=True)
        
        def update_style(*args):
            is_sel = variable.get() == value
            chip.configure(
                fg_color=self.COLORS['primary'] if is_sel else self.COLORS['background'],
                text_color="white" if is_sel else self.COLORS['text_primary'],
                border_color=self.COLORS['primary'] if is_sel else "#E0E0E0"
            )
        
        variable.trace_add('write', update_style)
    
    def _create_footer(self, parent):
        """Create footer"""
        footer = ctk.CTkFrame(parent, fg_color="transparent", height=30)
        footer.pack(fill="x", pady=(10, 0))
        
        footer_text = ctk.CTkLabel(
            footer,
            text=f"{self.ICONS['info']}  Powered by Prolog Expert System  |  For Pakistani Travelers",
            font=("Segoe UI", 11),
            text_color=self.COLORS['text_secondary']
        )
        footer_text.pack()
    
    def search_destinations(self):
        """Search for destinations and display as cards"""
        budget = self.budget_var.get()
        interest = self.interest_var.get()
        
        # Clear previous results
        for widget in self.results_container.winfo_children():
            widget.destroy()
        
        # Loading indicator
        loading = ctk.CTkLabel(
            self.results_container,
            text=f"{self.ICONS['search']}  Searching for destinations...",
            font=("Segoe UI", 14),
            text_color=self.COLORS['text_secondary']
        )
        loading.pack(pady=20)
        self.root.update()
        
        results = self.expert_system.get_recommendations(budget, interest)
        
        # Remove loading
        loading.destroy()
        
        if not results:
            self._show_no_results()
            return
        
        # Results header
        header = ctk.CTkLabel(
            self.results_container,
            text=f"{self.ICONS['check']}  Found {len(results)} Perfect Destination{'s' if len(results) > 1 else ''} for You",
            font=("Segoe UI", 20, "bold"),
            text_color=self.COLORS['success']
        )
        header.pack(pady=(10, 20))
        
        # Display destination cards
        for dest in results:
            self._create_destination_card(self.results_container, dest)
    
    def _show_no_results(self):
        """Show no results message"""
        no_results_card = ctk.CTkFrame(
            self.results_container,
            fg_color=self.COLORS['card'],
            corner_radius=15
        )
        no_results_card.pack(fill="x", pady=10, padx=5)
        
        content = ctk.CTkFrame(no_results_card, fg_color="transparent")
        content.pack(pady=40, padx=30)
        
        icon = ctk.CTkLabel(
            content,
            text=self.ICONS['warning'],
            font=("Segoe UI Emoji", 48),
            text_color=self.COLORS['warning']
        )
        icon.pack(pady=(0, 10))
        
        title = ctk.CTkLabel(
            content,
            text="No Destinations Found",
            font=("Segoe UI", 18, "bold"),
            text_color=self.COLORS['text_primary']
        )
        title.pack()
        
        subtitle = ctk.CTkLabel(
            content,
            text="Try adjusting your budget or interests",
            font=("Segoe UI", 14),
            text_color=self.COLORS['text_secondary']
        )
        subtitle.pack(pady=(5, 0))
    
    def _create_destination_card(self, parent, dest):
        """Create a beautiful card for each destination"""
        card = ctk.CTkFrame(
            parent,
            fg_color=self.COLORS['card'],
            corner_radius=15,
            border_width=0
        )
        card.pack(fill="x", pady=10, padx=5)
        
        # Card content
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=25, pady=20)
        
        # Header with destination name
        header_frame = ctk.CTkFrame(content, fg_color=self.COLORS['primary'], corner_radius=10)
        header_frame.pack(fill="x", pady=(0, 15))
        
        dest_name = ctk.CTkLabel(
            header_frame,
            text=f"{self.ICONS['location']}  {dest['destination'].upper()}",
            font=("Segoe UI", 22, "bold"),
            text_color="white"
        )
        dest_name.pack(pady=12)
        
        # Info grid
        info_grid = ctk.CTkFrame(content, fg_color="transparent")
        info_grid.pack(fill="x", pady=10)
        
        # Budget info
        self._create_info_row(
            info_grid,
            self.ICONS['money'],
            "Minimum Budget",
            f"${dest['min_budget']} USD",
            0
        )
        
        # Visa status
        visa_text = dest['visa_status'].replace('_', ' ').title()
        visa_color = self._get_visa_color(dest['visa_status'])
        self._create_info_row(
            info_grid,
            self.ICONS['visa'],
            "Visa Status",
            visa_text,
            1,
            value_color=visa_color
        )
        
        # Best season
        self._create_info_row(
            info_grid,
            self.ICONS['calendar'],
            "Best Season",
            dest['best_season'],
            2
        )
        
        # Documents section
        docs_frame = ctk.CTkFrame(content, fg_color=self.COLORS['background'], corner_radius=10)
        docs_frame.pack(fill="x", pady=(15, 0))
        
        docs_content = ctk.CTkFrame(docs_frame, fg_color="transparent")
        docs_content.pack(fill="x", padx=15, pady=15)
        
        docs_header = ctk.CTkLabel(
            docs_content,
            text=f"{self.ICONS['document']}  Required Documents",
            font=("Segoe UI", 14, "bold"),
            text_color=self.COLORS['text_primary'],
            anchor="w"
        )
        docs_header.pack(fill="x", pady=(0, 8))
        
        docs_text = ctk.CTkLabel(
            docs_content,
            text=dest['documents'],
            font=("Segoe UI", 12),
            text_color=self.COLORS['text_secondary'],
            wraplength=800,
            justify="left",
            anchor="w"
        )
        docs_text.pack(fill="x")
    
    def _create_info_row(self, parent, icon, label, value, row, value_color=None):
        """Create an info row in the card"""
        row_frame = ctk.CTkFrame(parent, fg_color="transparent")
        row_frame.grid(row=row, column=0, sticky="ew", pady=8, padx=5)
        parent.grid_columnconfigure(0, weight=1)
        
        # Icon and label
        left_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
        left_frame.pack(side="left")
        
        icon_label = ctk.CTkLabel(
            left_frame,
            text=icon,
            font=("Segoe UI Emoji", 16),
            text_color=self.COLORS['primary']
        )
        icon_label.pack(side="left", padx=(0, 8))
        
        label_text = ctk.CTkLabel(
            left_frame,
            text=label,
            font=("Segoe UI", 13),
            text_color=self.COLORS['text_secondary']
        )
        label_text.pack(side="left")
        
        # Value
        value_label = ctk.CTkLabel(
            row_frame,
            text=value,
            font=("Segoe UI", 13, "bold"),
            text_color=value_color or self.COLORS['text_primary']
        )
        value_label.pack(side="right")
    
    def _get_visa_color(self, visa_status):
        """Get color based on visa difficulty"""
        colors = {
            'visa_free': '#00897B',      # Green
            'visa_on_arrival': '#43A047', # Light Green
            'e_visa': '#FFB300',          # Amber
            'visa_required': '#E53935'    # Red
        }
        return colors.get(visa_status, self.COLORS['text_primary'])
    
    def run(self):
        """Start the GUI"""
        self.root.mainloop()


if __name__ == "__main__":
    try:
        app = TravelGUI()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Created travel_kb.pl file")
        print("2. Installed: pip install pyswip customtkinter")
        print("3. Installed SWI-Prolog on your system")
        sys.exit(1)