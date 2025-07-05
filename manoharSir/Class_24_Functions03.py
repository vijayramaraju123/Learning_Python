


dbDetails = {}

def getResult(dbName):
    dbDetails['DatabaseName'] =dbName
    dbDetails['ProjectName'] = "ProjectName"
    dbDetails['Size'] = 200
    def inner():
        dbQuota = 100
        diskQuota = 2500
        activeDv = 1000
        history = 20
        total = activeDv + history
        return {
            "dbQuota": dbQuota,
            "diskQuota":diskQuota,
            "activity": activeDv,
            "total": total
        }
    return inner

def run(runEnv = "dev"):
    dbFunction = getResult("Database1")
    result = dbFunction()

    print(f"Envronment: {runEnv}")
    print(f"Database Details: {dbDetails}")
    print(f"COmpute values: {result}")

run()


run("prod")
run("sit")
run("uat")
