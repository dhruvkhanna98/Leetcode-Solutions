class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        # Base case
        if len(emails) == 0: 
            return 0
        
        email_set = set()
        
        for email in emails: 
            local, domain = email.split("@")
            local = local.replace(".", "")
            if "+" in local: 
                local = local.split("+")[0]
            
            e = local + "@" + domain
            email_set.add(e)
            
        
        return len(email_set)
            
            
            
           
        