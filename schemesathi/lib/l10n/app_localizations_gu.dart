// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Gujarati (`gu`).
class AppLocalizationsGu extends AppLocalizations {
  AppLocalizationsGu([String locale = 'gu']) : super(locale);

  @override
  String get languageName => 'ગુજરાતી';

  @override
  String get appName => 'યોજના સાથી એઆઈ';

  @override
  String get appSlogan => 'Empowering citizens with clarity';

  @override
  String get skip => 'Skip';

  @override
  String get next => 'Next';

  @override
  String get getStarted => 'Get Started';

  @override
  String get onboardingTitle1 => 'AI-Powered Discovery';

  @override
  String get onboardingDesc1 =>
      'Find the perfect government schemes tailored just for you using our advanced AI analysis.';

  @override
  String get onboardingTitle2 => 'How It Works';

  @override
  String get onboardingDesc2 =>
      'Simply tell us a bit about yourself. Our AI scans thousands of schemes to find your best matches.';

  @override
  String get onboardingTitle3 => 'Trusted & Transparent';

  @override
  String get onboardingDesc3 =>
      'We use official sources and verify every scheme. Your data is safe and used only for finding benefits.';

  @override
  String get loginWelcome => 'Welcome Back';

  @override
  String get loginSubtitle => 'Sign in to accurate scheme predictions';

  @override
  String get emailLabel => 'Email Address';

  @override
  String get passwordLabel => 'Password';

  @override
  String get signIn => 'Sign In';

  @override
  String get noAccount => 'Don\'t have an account?';

  @override
  String get signUp => 'Sign Up';

  @override
  String get continueGuest => 'Continue as Guest';

  @override
  String get userDetailsTitle => 'User Details';

  @override
  String get ageLabel => 'Age';

  @override
  String get ageHint => 'Years';

  @override
  String get incomeLabel => 'Annual Income';

  @override
  String get incomeHint => 'INR';

  @override
  String get casteLabel => 'Caste Category';

  @override
  String get stateLabel => 'State/UT';

  @override
  String get occupationLabel => 'Occupation';

  @override
  String get disabilityLabel => 'Differently Abled?';

  @override
  String get findMyBenefits => 'Find My Benefits';

  @override
  String get chipSchemes => '1000+ Schemes';

  @override
  String get chipVerified => 'AI Verified';

  @override
  String get chipOfficial => 'Official Sources';

  @override
  String get trustOfficial => 'Uses official government documents';

  @override
  String get trustLogin => 'No login required';

  @override
  String get trustSecure => 'Secure & private';

  @override
  String get microAi =>
      'AI-powered eligibility check based on official schemes';

  @override
  String get analyzingProfile => 'Analyzing Profile...';

  @override
  String get analyzingDesc =>
      'Checking eligibility against 1000+ official government schemes...';

  @override
  String get aiTrust => 'Based on official government documents';

  @override
  String get resultsTitle => 'Best Matches for You';

  @override
  String confidenceScore(String score) {
    return '$score% Confidence';
  }

  @override
  String get viewDetails => 'View Details';
}
