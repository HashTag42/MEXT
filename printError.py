import sys      # Needed to write to stderr

################################################################################
def printError(msg):
    sys.stderr.write(f"[ERROR] {msg}\n")
################################################################################