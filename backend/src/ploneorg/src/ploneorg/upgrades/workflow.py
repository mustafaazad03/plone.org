from plone import api
from ploneorg import logger


def update_security(context):
    # Update workflow security
    wf_tool = api.portal.get_tool("portal_workflow")
    wf_tool.updateRoleMappings()
    logger.info("Updated security")