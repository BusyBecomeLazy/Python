class IntelligenceQuestionnaireSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.intelligence_test_module = IntelligenceTestModule()
        self.database_manager = DatabaseManager()
        self.frontend_module = FrontendModule()

    def start_questionnaire(self, user_id):
        user_info = self.user_manager.get_user_info(user_id)
        test_difficulty = self.intelligence_test_module.calculate_difficulty(user_info)
        test_questions = self.intelligence_test_module.generate_test(test_difficulty)
        self.frontend_module.display_questions(test_questions)

    def record_user_answer(self, user_id, question_id, answer):
        self.intelligence_test_module.record_answer(question_id, answer)
        self.user_manager.update_user_history(user_id, question_id, answer)

    def finish_questionnaire(self, user_id):
        analysis_report = self.intelligence_test_module.analyze_results()
        self.frontend_module.display_analysis_report(analysis_report)

# Key algorithm for personalized question selection in IntelligenceTestModule
class IntelligenceTestModule:
    def generate_test(self, difficulty):
        selected_questions = self.select_questions(difficulty)
        return selected_questions

    def select_questions(self, difficulty):
        # Simplified algorithm for question selection based on difficulty
        selected_questions = [q for q in self.question_bank if q['difficulty'] == difficulty]
        return random.sample(selected_questions, k=5)

    # Other module methods...

    # Key algorithm for answer analysis in IntelligenceTestModule
    def analyze_results(self):
        total_score = 0
        for question_id, user_answer in self.user_answers.items():
            correct_answer = self.get_correct_answer(question_id)
            if user_answer == correct_answer:
                total_score += 1

        analysis_report = {
            'total_score': total_score,
            'assessment': 'Above average' if total_score >= 5 else 'Average',
            'improvement_suggestions': 'Focus on logical reasoning skills.',
        }

        return analysis_report

    # Other module methods...
