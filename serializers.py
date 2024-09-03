def mapping_serializer(mapping):
    if not isinstance(mapping, list):
        mapping = [mapping]
    return [
        {
            'id': record.id,
            'crm_name': record.crm_name,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'phone': record.phone,
            'email': record.email,
            'company_name': record.company_name,
            'phone_consent': record.phone_consent,
            'email_consent': record.email_consent
        }
        for record in mapping
    ]