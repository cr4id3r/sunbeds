import logging


def check_actual_urls(app):
    # Print out all mapped routes
    logging.info(" ")
    logging.info("ROUTES IN PROJECT ================================================")
    logging.info(" ")
    all_rules = [rule for rule in app.url_map.iter_rules()]
    all_rules.sort(key=lambda x: x.rule)
    for rule in all_rules:
        rule_methods = set(rule.methods)
        rule_methods.discard('OPTIONS')
        rule_methods.discard('HEAD')
        logging.info('%s %s ----> %s', rule.rule, rule_methods, rule.endpoint)
    logging.info(" ")
    logging.info("==================================================================")
    logging.info(" ")