import 'package:flutter/material.dart';
import '../theme/app_theme.dart';
import 'package:schemesathi/l10n/generated/app_localizations.dart';
import 'scheme_assistant_screen.dart';

class ResultsScreen extends StatelessWidget {
  const ResultsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Mock Data
    final List<Map<String, dynamic>> schemes = [
      {
        "name": "PM Kisan Samman Nidhi",
        "eligible": true,
        "benefit": "₹6,000 / year",
        "reason": "Farmer with < 2 hectares of land",
        "next_step": "Aadhaar eKYC via PMKISAN Portal"
      },
      {
        "name": "Ayushman Bharat (PM-JAY)",
        "eligible": true,
        "benefit": "₹5 Lakh Health Cover",
        "reason": "Family income matches criteria",
        "next_step": "Show Ration Card at empaneled hospital"
      },
      {
        "name": "PM Vishwakarma Yojana",
        "eligible": false,
        "benefit": "Loan up to ₹3 Lakh",
        "reason": "Does not match 'Artisan' occupation profile",
        "next_step": "Update occupation details if incorrect"
      },
    ];

    return Scaffold(
      appBar: AppBar(
        title: Text(AppLocalizations.of(context)!.benefits),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () => Navigator.of(context).popUntil((route) => route.isFirst),
        ),
      ),
      body: Column(
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
            decoration: BoxDecoration(
              color: Colors.white,
              boxShadow: [
                 BoxShadow(
                   color: Colors.black.withValues(alpha: 0.05),
                   blurRadius: 10,
                   offset: const Offset(0, 4),
                 ),
              ],
              borderRadius: const BorderRadius.only(
                bottomLeft: Radius.circular(24),
                bottomRight: Radius.circular(24),
              ),
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: AppTheme.secondaryColor.withValues(alpha: 0.1),
                    shape: BoxShape.circle,
                  ),
                  child: const Icon(Icons.auto_awesome, color: AppTheme.secondaryColor, size: 20),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        AppLocalizations.of(context)!.resultsTitle,
                        style: const TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 16,
                          color: AppTheme.textPrimary,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        "${AppLocalizations.of(context)!.resultsSubtitle} • ${schemes.where((s) => s['eligible'] == true).length} ${AppLocalizations.of(context)!.schemes}",
                        style: TextStyle(
                          fontSize: 13,
                          color: AppTheme.textSecondary.withValues(alpha: 0.8),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(20.0),
              itemCount: schemes.length,
              itemBuilder: (context, index) {
                final scheme = schemes[index];
                return _buildFloatingSchemeCard(scheme, context);
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFloatingSchemeCard(Map<String, dynamic> scheme, BuildContext context) {
    final bool isEligible = scheme['eligible'];
    final Color statusColor = isEligible ? AppTheme.secondaryColor : AppTheme.errorColor;

    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.06),
            blurRadius: 15,
            spreadRadius: 0,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => SchemeAssistantScreen(scheme: scheme),
              ),
            );
          },
          borderRadius: BorderRadius.circular(20),
          child: Column(
            children: [
              // Top Strip (Status Indicator)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                decoration: BoxDecoration(
                  color: statusColor.withValues(alpha: 0.08),
                  borderRadius: const BorderRadius.only(
                    topLeft: Radius.circular(20),
                    topRight: Radius.circular(20),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      isEligible ? Icons.check_circle : Icons.cancel,
                      size: 18,
                      color: statusColor,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      isEligible ? AppLocalizations.of(context)!.youQualify : "Not Eligible", 
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w700,
                        color: statusColor,
                      ),
                    ),
                    const Spacer(),
                    if (isEligible)
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(color: statusColor.withValues(alpha: 0.2)),
                        ),
                        child: Row(
                          children: [
                            Icon(Icons.auto_awesome, size: 12, color: statusColor),
                            const SizedBox(width: 4),
                            Text(
                              "AI Verified",
                              style: TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                color: statusColor,
                              ),
                            ),
                          ],
                        ),
                      ),
                  ],
                ),
              ),
              
              // Main Body
              Padding(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      scheme['name'],
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: AppTheme.textPrimary,
                      ),
                    ),
                    const Padding(
                      padding: EdgeInsets.symmetric(vertical: 16),
                      child: Divider(height: 1),
                    ),
                    _buildDetailRow(Icons.currency_rupee, AppLocalizations.of(context)!.benefits, scheme['benefit'], isHighlight: true),
                    const SizedBox(height: 12),
                    _buildDetailRow(Icons.info_outline, AppLocalizations.of(context)!.eligibility, scheme['reason']),
                    
                    if (isEligible) ...[
                       const SizedBox(height: 20),
                       Container(
                         width: double.infinity,
                         padding: const EdgeInsets.all(16),
                         decoration: BoxDecoration(
                           gradient: LinearGradient(
                             colors: [
                               const Color(0xFFE3F2FD),
                               const Color(0xFFE3F2FD).withValues(alpha: 0.5),
                             ],
                           ),
                           borderRadius: BorderRadius.circular(12),
                           border: Border.all(color: Colors.blue.withValues(alpha: 0.2)),
                         ),
                         child: Column(
                           crossAxisAlignment: CrossAxisAlignment.start,
                           children: [
                             Text(
                               "Next Step",
                               style: TextStyle(
                                 fontSize: 12,
                                 fontWeight: FontWeight.bold,
                                 color: Colors.blue.shade900,
                                 letterSpacing: 0.5,
                               ),
                             ),
                             const SizedBox(height: 4),
                             Row(
                               crossAxisAlignment: CrossAxisAlignment.start,
                               children: [
                                 Expanded(
                                   child: Text(
                                     scheme['next_step'],
                                     style: TextStyle(
                                       fontSize: 14,
                                       color: Colors.blue.shade800,
                                       height: 1.3,
                                     ),
                                   ),
                                 ),
                                 Icon(Icons.arrow_forward_ios, size: 14, color: Colors.blue.shade800),
                               ],
                             ),
                           ],
                         ),
                       ),
                    ],
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildDetailRow(IconData icon, String label, String value, {bool isHighlight = false}) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(
            color: AppTheme.backgroundColor,
            borderRadius: BorderRadius.circular(8),
          ),
          child: Icon(icon, size: 18, color: AppTheme.textSecondary),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                label,
                style: const TextStyle(
                  color: AppTheme.textSecondary,
                  fontSize: 12,
                  fontWeight: FontWeight.w500,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                value,
                style: TextStyle(
                  color: AppTheme.textPrimary,
                  fontSize: 14,
                  fontWeight: isHighlight ? FontWeight.bold : FontWeight.w500,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
